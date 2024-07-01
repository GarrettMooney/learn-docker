# Dockerfile - In Depth

## Chain RUN instructions

Each `RUN` creates a new image layer.

Reduce the number of layers by chaining commands together.

```Dockerfile
RUN apt-get update && apt-get install -y \
  git \
  vim
```

Now we only have two build steps instead of three.

## Sort Multi-Line Arguments Alphanumerically

```Dockerfile
RUN apt-get update && apt-get install -y \
  git \
  python \
  vim
```

## CMD Instructions

`CMD` specifies the startup command.

If a `CMD` isn't specified, Docker will use the default command defined in the base image.

`CMD` only runs when the container starts up.

## Docker Cache
