---
title: 'Web: Docker'
---

# Web: Docker

## Поддерживаемые платформы

- `linux/arm64`
- `linux/arm/v7`
- `linux/amd64`

## Подготовка

Для запуска [Docker](https://docker.com) контейнера _HOMEd Web_ необходимо создать каталог, в котором будут храниться данные и лог сервиса, и поместить в этот каталог файл конфигурации с именем `homed-web.conf`. Каталог может иметь произвольное имя, в этой статье используется каталог `/opt/homed-web`.

## Пример конфигурации

```ini
[log]
enabled=false

[mqtt]
host=192.168.12.76
port=1883
username=web
password=secret
prefix=homed

[server]
port=8080
database=/data/database.json
username=homed
password=homed
```

Подробнее о параметрах конфигурации можно почитать [здесь](/web/configuration/).

## Запуск контейнера

```sh
docker run \
  --detach \
  --volume /opt/homed-web:/data \
  --publish 8080:8080 \
  --name homed-web \
  docker.u236.org/homed-web
```

| Параметр | Описание |
|----------|----------|
| `--volume`  | проброс каталога `/opt/homed-web` на хосте в каталог `/data` внутри контейнера |
| `--publish` | проброс TCP порта `8080` из контейнера на хост |
| `--name`    | название контейнера |
