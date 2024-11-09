# Step 1: Use the official Node.js image as a build environment
FROM node: 20-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the source code to the container
COPY . .

# Build the React application
RUN npm run build

# Use a simple web server like serve to serve the static files
RUN npm install -g serve

# Expose the port
EXPOSE 3000

# Start the React app
CMD ["serve", "-s", "build"]
