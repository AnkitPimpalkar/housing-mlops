# 1. Use official Python slim image
FROM python:3.10-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy requirements first (separate for caching)
COPY ./requirements.txt .

# 3. Copy everything needed into /app

COPY setup.py .
COPY src/ ./src/
COPY main.py ./

# 3. Copy config (separate for caching)
COPY ./config.yaml /app/config.yaml

# 4. Install system dependencies (e.g., git)
RUN apt-get update && apt-get install -y git

# 5. Install Python dependencies
RUN pip install --upgrade pip \
 && pip install -r requirements.txt \
 && pip install -e .

# 6. Create outputs directory
RUN mkdir -p /app/outputs

# 7. List files
RUN ls -la

# 8. Set default command (optional)
CMD ["python", "main.py"]