# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire app
COPY . .

# Expose a dummy port (Railway will still assign dynamic port)
EXPOSE 8000

# Start the app using Railway's injected $PORT
CMD ["sh", "-c", "uvicorn app.main:app --host=0.0.0.0 --port=$PORT"]
