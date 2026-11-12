# Use a small, stable Nginx image to serve the static website.
FROM nginx:1.27-alpine

# Replace the default Nginx website with the Fitness World files.
COPY index.html style.css app.js /usr/share/nginx/html/

# Nginx listens on port 80 inside the container.
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
