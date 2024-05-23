FROM python:3.10-alpine

ENV REDIS_HOST=redis
ENV REDIS_PORT=6379

WORKDIR /app

COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir redis


# Run app.py when the container launches
CMD ["python3", "producer_app.py"]
