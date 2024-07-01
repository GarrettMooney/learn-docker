# Build Images - Dockerfile

## Ways to build images

1. Write a Dockerfile.
2. Commit changes made in a container.

We'll focus on the first way in this section.

## Dockerfile

```bash
FROM debian:buster
RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y vim
```

## Build an image

```bash
docker build -t <image_name> .
```

Tag is `latest` by default.

## Inspect

```bash
docker images
```

Should see that the image is created and larger than the base image.
