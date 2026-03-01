---
title: 'Custom: Docker'
---

# Custom: Docker

## Поддерживаемые платформы

- `linux/arm64`
- `linux/arm/v7`
- `linux/amd64`

## Подготовка

Для запуска [Docker](https://docker.com) контейнера _HOMEd Custom_ необходимо создать каталог, в котором будут храниться данные и лог сервиса, и поместить в этот каталог файл конфигурации с именем `homed-custom.conf`. Каталог может иметь произвольное имя, в этой статье используется каталог `/opt/homed-custom`.

## Пример конфигурации

```ini
[log]
enabled=true

[mqtt]
host=192.168.12.76
port=1883
username=custom
password=secret
prefix=homed
names=false

[homeassistant]
enabled=false
prefix=homeassistant
status=homeassistant/status
update=false

[device]
database=/data/database.json
properties=/data/properties.json
```

Подробнее о параметрах конфигурации можно почитать [здесь](/custom/configuration/).

## Запуск контейнера

```sh
docker run \
  --detach \
  --volume /opt/homed-custom:/data \
  --name homed-custom \
  docker.u236.org/homed-custom
```

| Параметр | Описание |
|----------|----------|
| `--volume` | проброс каталога `/opt/homed-custom` на хосте в каталог `/data` внутри контейнера |
| `--name`   | название контейнера |

## Что дальше?

После настройки _HOMEd Custom_ можно приступать к добавлению устройств, при помощи [веб-интерфейса](/web/) или [вручную](/custom/database/).
