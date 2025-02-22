[locked run cache in buildkit](https://yuki-nakamura.com/2024/03/08/use-a-locked-run-cache-between-builds-in-buildkit/)

> What does `RUN --mount=type=cache,sharing=locked` do?

Seems like it helps cache the `RUN` command for things like `apt-get install` and `uv pip install` using a cache.

Having it locked means that there aren't concurrent builds that can access the cache at the same time.

Sounds useful for local development, but I'm not sure how useful it is for CI/CD.
