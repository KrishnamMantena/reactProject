# Use an official Node.js image as a base
FROM node:20-alpine AS build

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the entire frontend code
COPY . .

# Build the React app
RUN npm run build

# Serve the app with nginx
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html

# Expose the port the app runs on
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
