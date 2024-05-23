FROM python:3.10-alpine

ENV DB_USER=postgres
ENV DB_PASSWORD=postgres
ENV DB_HOST=postgres
ENV DB_PORT=5432
ENV DB_NAME=ecommerce_docker
ENV REDIS_HOST=redis
ENV REDIS_PORT=6379

WORKDIR /app

COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir psycopg2-binary redis


# Run app.py when the container launches
CMD ["python3", "consumer_app.py"]
