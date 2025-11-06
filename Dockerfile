FROM python:3.11-slim

WORKDIR /app

# Copy code
COPY . /app/

# Install dependencies if needed
RUN pip install --no-cache-dir --upgrade pip

# Set timezone environment variable if desired
ENV TZ=Europe/Kyiv

CMD ["python", "main.py"]
