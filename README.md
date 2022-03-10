# docker-hub-rss-api

An api for docker images on docker hub

Inspired by https://github.com/TheConnMan/docker-hub-rss

## demo api
https://rss.sam-services.de

## build/start docker container
```
# build
docker build -t docker-hub-rss-api .
# run
docker run -it \
  -p 8000:8000 \
   docker-hub-rss-api

INFO:     Started server process [7]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

## usage

If you want tag from an official repo use "_" in org

## contribute

Pull requests are welcome :-)
