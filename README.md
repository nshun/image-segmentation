# image-segmentation

Image segementation tool with flask.

## Requirement

- make
- docker
- docker-componse
- firewall `80/tcp`
- copy dataset dir to `./dataset`

### File tree

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

1. Copy dataset dir

2. Start docker-compose

```
make start
```

2. Access to WEB server

[http://localhost/](http://localhost/)
