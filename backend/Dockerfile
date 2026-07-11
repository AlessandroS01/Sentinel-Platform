# Use the official lightweight Python image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code to the working directory
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Specify the command to run on container startup
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
