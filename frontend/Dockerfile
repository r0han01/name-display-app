# Use the official Node.js image from Docker Hub
FROM node:16-slim

# Set working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (if exists) for dependency installation
COPY package*.json /app/

# Install frontend dependencies
RUN npm install

# Copy the rest of the application code (including index.html)
COPY . /app

# Expose the port the app will run on
EXPOSE 3000

# Command to run the Node.js server
CMD ["node", "server.js"]
