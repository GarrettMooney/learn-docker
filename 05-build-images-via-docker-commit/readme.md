# Build Images - Docker Commit

## Ways to build images

1. Write a Dockerfile.
2. Commit changes made in a container.

We'll focus on the second way in this section.

## Docker Commit

Steps:

1. Spin up a container.
2. Make changes in the container.
3. Commit the changes to create a new image.


### Example

1. Spin up a container.

```bash
docker run -it debian:buster
```

2. Make changes in the container.

```bash
apt-get update && apt-get install -y git
exit
```

3. Commit the changes to create a new image.

```bash
docker commit <container_id> <new_image_name>
```

Check the new image.

```bash
docker images
```

The new image should be:

* listed as <new_image_name>
* ~100 MB heavier than the `debian:buster` image
