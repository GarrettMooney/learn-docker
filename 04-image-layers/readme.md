# Image Layers

## View all layers

```bash
docker history busybox:1.24
```

* base layer: adds a file
* 2nd layer: runs a command

## Writable Container Layer

Thin layer on top of the image layers.

All changes made to the running container are stored in this layer.

When the container is deleted, this layer is also deleted.
