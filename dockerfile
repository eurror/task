# Use a slim Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Expose the port Django uses (default 8000)
EXPOSE 8000

# Set the command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
