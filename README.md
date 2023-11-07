# Flix-Task Fibonacci API

## Setup & Run
- Build the Docker image:
  `docker build -t flix-task .`
- Run the container:
  `docker run -d -p 5000:5000 flix-task`

## Testing
Run tests with pytest:
`docker exec -it <container_id> pytest /code/tests`
