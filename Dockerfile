# Use official Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy only requirements first (for better caching)
COPY requirements.txt .

# Create a virtual environment inside the container
RUN python -m venv /opt/venv

# Activate the venv and install dependencies
RUN /opt/venv/bin/pip install --no-cache-dir --upgrade pip \
    && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Add venv to PATH so `python` and `pip` use it automatically
ENV PATH="/opt/venv/bin:$PATH"

# Copy rest of the project files
COPY . .

# Expose port 5000
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]