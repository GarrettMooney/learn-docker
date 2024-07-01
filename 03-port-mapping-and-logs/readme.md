# Port Mapping and Logs

## Port Mapping

`-p` host_port : container_port

```bash
docker run -it --rm -p 8888:8080 tomcat:8.0
```

Open localhost:8888 in browser to access tomcat server.

In a production environment, we would run the container in the background using `-d` flag.

```bash
docker run -it -d -p 8888:8080 tomcat:8.0
```

## Docker Logs

To view the logs of a running container, use the `docker logs` command.

```bash
docker logs <container_id>
```
