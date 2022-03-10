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
```

## usage

If you want tag from an official repo use "_" in org

## contribute

Pull requests are welcome :-)
