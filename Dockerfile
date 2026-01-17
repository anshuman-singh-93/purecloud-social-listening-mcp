# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install uv for fast dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy project definition files
COPY pyproject.toml .
COPY uv.lock .

# Install dependencies using uv
# We use --system to install into the system python environment
RUN uv pip install --system .

# Copy the rest of the application code
COPY . .

# Make the start script executable
RUN chmod +x start.sh

# Expose the port the app runs on
EXPOSE 8000

# Set environment variables if needed (can be overridden at runtime)
# ENV PYTHONUNBUFFERED=1

# Command to run the application
CMD ["./start.sh"]
