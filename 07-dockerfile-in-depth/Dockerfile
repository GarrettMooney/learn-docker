FROM debian:buster
RUN apt-get update && apt-get install -y \
  git \
  python \
  vim
COPY abc.txt /src/abc.txt
CMD ["echo", "Hello, World!"]
