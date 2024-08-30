# Use the official Python image as the base image
FROM python:3.11-alpine

# Set the working directory
WORKDIR /usr/src/app

# Copy application code
COPY . .

# Install dependencies

# Create a group and user
RUN addgroup -S mygroup && adduser -S myuser -G mygroup

# Change ownership of the application files to the non-root user
RUN chown -R myuser:mygroup /usr/src/app

# Switch to non-root user
USER myuser

# Default command to run Gunicorn for Django
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:8000 --timeout 0 barbing_salon.wsgi:application"]
