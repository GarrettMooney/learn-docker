docker build -f Dockerfile --target base -t circle-base .
docker build -f Dockerfile --target build -t circle-builder .
docker build -f Dockerfile --target runtime -t circle-runner .
