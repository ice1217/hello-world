#!/bin/sh

docker stop hello-world || true
docker rm hello-world || true
docker run -d --name hello-world -p 5000:5000 hello-world