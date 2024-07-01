# Docker Containers

## Detached Mode

Use the `-d` flag to run a container in detached mode.

> Have the container run in the background.

```bash
docker run -d busybox:1.24 sleep 1000
```

## Find all running docker containers

```bash
docker ps
```

> Find all running docker containers and ones that have stopped

```bash
docker ps -a
```

## Automatically remove the container when it stops

```bash
docker run --rm busybox:1.24 sleep 1
```

## Give the container a name

```bash
docker run --name hello_world busybox:1.24
```

## Docker inspect

```bash
docker inspect hello_world
```

The results are json.

Some
