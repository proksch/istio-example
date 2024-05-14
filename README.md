# istio-example

This project contains two basic webservices `app` and `lib` that allow to play around with Prometheus monitoring in Kubernetes and Istio.

To build the respective Docker images [proksch/istio-example-lib](https://hub.docker.com/repository/docker/proksch/istio-example-lib) and [proksch/istio-example-app](https://hub.docker.com/repository/docker/proksch/istio-example-app), build and push the two respective images.

```
$ cd lib
$ docker build \
    -t docker.io/proksch/istio-example-lib:0.0.2 \
    -t docker.io/proksch/istio-example-lib:latest \
    .
```

And the same for the app.

```
$ cd ../app
$ docker build \
	-t docker.io/proksch/istio-example-app:0.0.2 \
	-t docker.io/proksch/istio-example-app:latest \
	.
```

You can test the application by starting the Docker compose setup in the `operation` folder.

If you need to release another version, you must bump the version in ...

- the respective `.py` files
- the build command in the `README.md`
- `docker-compose.yml`

... to keep everything consistent.