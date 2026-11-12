# Docker on AWS EC2 – Troubleshooting Guide

## Project: Pathnex Docker Application

**Environment**
- Cloud: AWS EC2
- Operating System: Amazon Linux
- User: `ec2-user`
- Container Engine: Docker
- Application: Node.js
- Application Port: 3000
- Host Port: 80

---

## 1. Error: Docker daemon permission denied

### Error encountered

When executing:

```bash
docker run -d -p 80:3000 --name pathnex-container-v1 pathnex-app-v1
```

Received:

```text
docker: permission denied while trying to connect
to the Docker daemon socket at unix:///var/run/docker.sock
```

### Root cause

The `ec2-user` did not have permission to access the Docker daemon socket:

```text
/var/run/docker.sock
```

Docker CLI communicates with the Docker daemon through this socket. The user did not have the required permissions.

### Solution 1: Temporary solution

Execute Docker commands using `sudo`:

```bash
sudo docker ps
sudo docker images
sudo docker build -t pathnex-app-v1 -f pathnex-dockerfile-v1 .
sudo docker run -d -p 80:3000 --name pathnex-container-v1 pathnex-app-v1
```

### Solution 2: Permanent solution

Add the EC2 user to the Docker group:

```bash
sudo usermod -aG docker ec2-user
```

Refresh group membership:

```bash
newgrp docker
```

Verify group membership:

```bash
groups
```

Expected output should contain:

```text
ec2-user docker
```

Test Docker access:

```bash
docker ps
```

If permissions are still denied, log out and reconnect to EC2.

**Important:** Docker group membership effectively grants root-level privileges. Only trusted users should be added.

---

## 2. Error: Docker build requires exactly one argument

### Command executed

```bash
docker build -t pathnex-app-v1 -f pathnex-dockerfile-v1
```

### Error received

```text
ERROR: "docker buildx build" requires exactly 1 argument.
```

### Root cause

The Docker build command requires a build context.

The build context tells Docker where to find the files required to build the image.

### Solution

Add `.` at the end:

```bash
docker build -t pathnex-app-v1 -f pathnex-dockerfile-v1 .
```

With sudo, if required:

```bash
sudo docker build -t pathnex-app-v1 -f pathnex-dockerfile-v1 .
```

### Command breakdown

| Command | Purpose |
|---|---|
| `docker build` | Build an image |
| `-t` | Assign image name |
| `pathnex-app-v1` | Image name |
| `-f` | Specify Dockerfile |
| `pathnex-dockerfile-v1` | Dockerfile name |
| `.` | Current directory as build context |

---

## 3. Error: Docker container not found / no containers running

### Commands executed

```bash
docker ps
docker ps -a
```

### Error received

```text
permission denied while trying to connect to the Docker daemon socket
```

### Investigation

Executed:

```bash
sudo docker ps
sudo docker ps -a
```

Output:

```text
CONTAINER ID   IMAGE   COMMAND   CREATED   STATUS   PORTS   NAMES
```

There were no containers.

### Root cause

The Docker image had been built, but the container had not yet been successfully created.

### Solution

First verify the image:

```bash
sudo docker images
```

Then create and start the container:

```bash
sudo docker run -d -p 80:3000 \
--name pathnex-container-v1 \
pathnex-app-v1
```

Verify:

```bash
sudo docker ps
```

---

## 4. Docker image successfully built

### Build command

```bash
sudo docker build -t pathnex-app-v1 -f pathnex-dockerfile-v1 .
```

### Successful output

```text
REPOSITORY       TAG       IMAGE ID
pathnex-app-v1   latest    134c287c43c5
```

### Dockerfile used

```dockerfile
FROM node:18

WORKDIR /pathnex-app

COPY pathnex-app-v1.js .

CMD ["node", "pathnex-app-v1.js"]
```

### Explanation

| Instruction | Purpose |
|---|---|
| `FROM` | Uses Node.js 18 base image |
| `WORKDIR` | Creates/sets application working directory |
| `COPY` | Copies application file into image |
| `CMD` | Starts Node.js application |

---

## 5. Important: Application port configuration

The Docker run command uses:

```bash
-p 80:3000
```

Meaning:

- Host port: 80
- Container port: 3000

The Node.js application must listen on:

```javascript
server.listen(3000, '0.0.0.0');
```

Otherwise, port mapping alone will not make the application accessible.

Also, ensure EC2 Security Group inbound rules allow TCP port 80.

---

## 6. Complete troubleshooting commands

Keep these commands for future EC2 Docker troubleshooting.

| Command | Purpose |
|---|---|
| `sudo systemctl status docker` | Check Docker service |
| `sudo systemctl start docker` | Start Docker |
| `groups` | Check user groups |
| `sudo usermod -aG docker ec2-user` | Add user to Docker group |
| `docker ps` | Show running containers |
| `docker ps -a` | Show all containers |
| `docker images` | List images |
| `docker build` | Build image |
| `docker run` | Create and start container |
| `docker logs CONTAINER` | Check application logs |
| `docker inspect CONTAINER` | Inspect container details |
| `docker port CONTAINER` | Check port mapping |

---

## 7. Real-world Docker deployment flow

```text
Developer writes application
          |
          v
     Dockerfile
          |
          v
   Docker Build
          |
          v
    Docker Image
          |
          v
    Docker Run
          |
          v
   Docker Container
          |
          v
   Port Mapping 80:3000
          |
          v
    AWS EC2 Public IP
          |
          v
     User accesses
     Application
```

---

## 8. What I learned from this troubleshooting

1. Docker CLI needs permission to communicate with the Docker daemon.
2. `sudo` can resolve Docker socket permission issues temporarily.
3. Docker group membership allows non-root Docker access but carries significant privileges.
4. Docker build requires a build context.
5. A Docker image and a Docker container are different things.
6. Building an image does not automatically start a container.
7. Port mapping connects host and container ports.
8. The application must listen on the correct container port and interface.
9. EC2 Security Groups must allow the required inbound traffic.

### Interview questions

**Q1. Why do we get permission denied when executing Docker commands?**

Because the current Linux user does not have permission to access the Docker daemon socket.

**Q2. What is the purpose of `.` in Docker build?**

It specifies the current directory as the Docker build context.

**Q3. What is the difference between `docker images` and `docker ps`?**

`docker images` lists available images, whereas `docker ps` lists running containers.

**Q4. What does `-p 80:3000` mean?**

It maps host port 80 to container port 3000.

**Q5. Does building an image automatically create a container?**

No. We need `docker run` to create and start a container.

---

**Project status:** Docker image build was successful. Container deployment and external application accessibility still need verification.