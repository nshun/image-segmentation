# image-segmentation

Image segementation tool with flask.

## Requirement

- docker
- docker-componse
- firewall `80/tcp`
- copy dataset dir to `./dataset`

### dataset dir tree

```
.
├── app/
│   ├── app.py
│   ├── static/
│   │   └── dataset/
│   │       ├── target       # target dir (*.png or *.jpg)
│   │       └── annotaions   # annotations (*.txt)
│   ├── Dockerfile
│   ├── requirements.txt
│   └── templates
├── docker-compose.yml
├── Makefile
└── README.md   
```

## How to Use

1. Build docker image

```
docker build ./ -t monitor
```

2. Run as docker container

```
docker run -d -p 80:80 -v "$(pwd)"/src:/src --restart always monitor
```

3. Access to WEB server

[http://localhost/](http://localhost/)
