# istio-example

This project contains two basic webservices `app` and `lib` that allow to play around with Prometheus monitoring in Kubernetes and Istio.

To build the respective Docker images [proksch/istio-example-lib](https://hub.docker.com/repository/docker/proksch/istio-example-lib) and [proksch/istio-example-app](https://hub.docker.com/repository/docker/proksch/istio-example-app), build and push the two respective images.

```
$ cd lib
docker buildx build \
	--platform linux/amd64,linux/arm64 \
    -t docker.io/proksch/istio-example-lib:0.0.2 \
    -t docker.io/proksch/istio-example-lib:latest \
    .
$ docker push --all-tags docker.io/proksch/istio-example-lib
```

And the same for the app.

```
$ cd app
docker buildx build \
	--platform linux/amd64,linux/arm64 \
	-t docker.io/proksch/istio-example-app:0.0.2 \
	-t docker.io/proksch/istio-example-app:latest \
	.
$ docker push --all-tags docker.io/proksch/istio-example-app
```

You can test the application by starting the Docker compose setup in the `operation` folder.

To release another version, run `bump-version.sh <from> <to>` to auto-update the version update in ...

- the respective `.py` files
- the build command in the `README.md`
- `docker-compose.yml`

... to keep everything consistent.
