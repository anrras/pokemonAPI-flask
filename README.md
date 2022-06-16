# Instructions to run the app

- Build the docker image

```
  docker build --tag pkm-flask-api-docker .
```

- Run the docker image in background exposing the port 8000

```
docker run -d -p 8000:8000 pkm-flask-api-docker
```

- Open the browser with the next url:

```
localhost:8000
```
