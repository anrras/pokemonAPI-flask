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

- For call the pokemon API call the next url:

```
localhost:8000/pokemon
```

- You can add parameters of key and value for search in the API:

```
localhost:8000/pokemon?key=name&value=pikachu
```

- the following keys are available to perform the search:

```
#
name
type 1
type 2
total
hp
attack
defense
sp. atk
sp. def
speed
generation
legendary
```
