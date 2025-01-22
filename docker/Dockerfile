# Use official Python image
FROM python:3.10-slim

# Set working directory in the container
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose a port for live trading APIs (if needed)
EXPOSE 5000

# Set the entry point to the simulator
CMD ["python", "src/main.py"]
