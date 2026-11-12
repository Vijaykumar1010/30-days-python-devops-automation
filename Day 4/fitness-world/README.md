# Fitness World – Docker on AWS EC2

A static HTML/CSS/JavaScript demo login website served by Nginx in Docker.

## Demo login

- Email: `fitness@example.com`
- Password: `Fit@123`

**Security note:** Authentication is only a browser-side demonstration. The credentials are visible in `app.js`; do not use this approach for real users or sensitive data. Production authentication needs a backend, hashed passwords, HTTPS, secure sessions, and proper authorization.

## 1. Run locally without Docker

Open `index.html` in a browser.

## 2. Build and test the Docker image on Windows

Run these commands from the folder containing the Dockerfile:

```powershell
docker build -t fitness-world:v1 .
docker run -d --name fitness-world -p 8080:80 fitness-world:v1
docker ps
```

Open `http://localhost:8080`.

Stop and remove the local container:

```powershell
docker stop fitness-world
docker rm fitness-world
```

## 3. Push the image to Docker Hub

Create a Docker Hub repository named `fitness-world` first. Replace `YOUR_DOCKERHUB_USERNAME` below with your Docker Hub username.

```powershell
docker login
docker tag fitness-world:v1 YOUR_DOCKERHUB_USERNAME/fitness-world:v1
docker push YOUR_DOCKERHUB_USERNAME/fitness-world:v1
```

## 4. Prepare AWS EC2

1. Launch an Amazon Linux 2023 EC2 instance.
2. Create or select a security group with inbound rules:
   - SSH, TCP 22, source: **your public IP only**
   - HTTP, TCP 80, source: `0.0.0.0/0`
3. Connect to the instance using EC2 Instance Connect or SSH.

Do not expose SSH to the entire internet unless you have a specific, temporary reason.

## 5. Install Docker on Amazon Linux 2023

Run on the EC2 instance:

```bash
sudo dnf update -y
sudo dnf install docker -y
sudo systemctl enable --now docker
sudo usermod -aG docker ec2-user
```

Refresh the SSH session (log out and reconnect), then verify:

```bash
docker --version
docker ps
```

If group permissions have not refreshed, use `sudo docker` for the Docker commands.

## 6. Pull and run the image on EC2

Replace `YOUR_DOCKERHUB_USERNAME`:

```bash
docker pull YOUR_DOCKERHUB_USERNAME/fitness-world:v1
docker run -d --name fitness-world --restart unless-stopped -p 80:80 YOUR_DOCKERHUB_USERNAME/fitness-world:v1
```

Check:

```bash
docker ps
docker logs fitness-world
curl -I http://localhost
```

## 7. Open the website

Find the EC2 instance's **Public IPv4 address** in the AWS console and visit:

```text
http://EC2_PUBLIC_IP
```

You should see the Fitness World login page. Sign in with the demo credentials above.

## 8. Useful troubleshooting

| Symptom | Checks |
|---|---|
| Website does not open | EC2 security group allows inbound TCP 80; instance has a public IPv4 address; container is running |
| `docker: command not found` | Install Docker and check `sudo systemctl status docker` |
| Docker permission denied | Reconnect after `sudo usermod -aG docker ec2-user`, or use `sudo docker` |
| Port already allocated | Check `sudo ss -lntp` and stop the conflicting service/container |
| Container exited | Run `docker ps -a` and `docker logs fitness-world` |
| Image pull denied | Check Docker Hub repository name, visibility, and `docker login` if private |

## Architecture

```text
Browser
   |
   | HTTP :80
   v
EC2 Security Group (allow TCP 80)
   |
   v
EC2 Instance
   |
   v
Docker Container
   |
   v
Nginx :80
   |
   v
index.html + style.css + app.js
```

## Cleanup

On EC2:

```bash
docker stop fitness-world
docker rm fitness-world
docker image rm YOUR_DOCKERHUB_USERNAME/fitness-world:v1
```

Terminate the EC2 instance when you have finished the lab to avoid ongoing AWS charges.
