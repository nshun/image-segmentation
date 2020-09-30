# flask-test

## Requirement

- [docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
- firewall `80/tcp`
- mount dataset dir to `./dataset`

### dataset dir tree

```
.
└── dataset/
    ├── target          # target dir (to attach)
    └── attributes      # area and class data
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
