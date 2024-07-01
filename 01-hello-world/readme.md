# Hello World

## First command

> What images do we have?

```bash
docker images
```

> Let's run a container with the `busybox` image and print `Hello World`

`busybox` is a lightweight image that contains a minimal Linux distribution.
It will be downloaded for the first time here

```bash
docker run busyboxy:1.24 echo "Hello World"
```

> Now what images do we have?

```bash
docker images
```

> Re-run the container with the `busybox` image and print `Hello World`

```bash
docker run busybox:1.24 echo "Hello World"
```

This was much faster because the image was already downloaded.

> List files in the container at the root directory

```bash
docker run busybox:1.24 ls /
```

This was much faster because the image was already downloaded.

## Interactive Mode

* `-i`: starts an interactive container
* `-t`: creates a pseudo-TTY that attaches `stdin` and `stdout`

```bash
docker run -it busybox:1.24
```
