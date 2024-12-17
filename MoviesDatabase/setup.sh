docker build -t videostore_db .

docker run --name vs_db --rm -e POSTGRES_PASSWORD=password -p 5456:5432 -d videostore_db