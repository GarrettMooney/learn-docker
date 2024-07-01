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

Docker will cache the results of each build step.

Aggressive caching can lead to stale results.

One solution is to chain commands together.

```Dockerfile
RUN apt-get update && apt-get install -y \
  git \
  vim
```

Another solution is to use `--no-cache` to force Docker to rebuild the image.

```bash
docker build --no-cache .
```

## Copy

`COPY` copies files from the host to the container.

1. create a file

```bash
touch abc.txt
```

2. add the file to the Dockerfile

```Dockerfile
COPY abc.txt /src/abc.txt
```

3. build the image

```bash
docker build -t <my_image> .
```

4. run the container

```bash
docker run -it <my_image> ls /src/abc.txt
```

## Add

`ADD` is similar to `COPY` but can also:

* fetch files from the internet
* automatically unpack compressed files

`COPY` is preferred since it is more transparent.
