# Use an official Node.js image as a base
FROM node:20-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the entire backend code
COPY . .

# Expose the port your backend listens on
EXPOSE 5000

# Start the backend service
CMD ["npm", "start"]
