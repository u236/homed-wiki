---
title: 'ZigBee: Docker'
---

# ZigBee: Docker

## Поддерживаемые платформы

- `linux/arm64`
- `linux/arm/v7`
- `linux/amd64`

## Подготовка

Для запуска [Docker](https://docker.com) контейнера _HOMEd ZigBee_ необходимо создать каталог, в котором будут храниться данные и лог сервиса, и поместить в этот каталог файл конфигурации с именем `homed-zigbee.conf`. Каталог может иметь произвольное имя, в этой статье используется каталог `/opt/homed-zigbee`.

## Пример конфигурации

```ini
[log]
enabled=true

[mqtt]
host=192.168.12.76
port=1883
username=zigbee
password=secret
prefix=homed
names=false

[homeassistant]
enabled=true
prefix=homeassistant
status=homeassistant/status
update=false

[default]
discovery=true
cloud=true

[device]
database=/data/database.json
properties=/data/properties.json
options=/data/options.json
external=/data/library
ota=/data/ota

[zigbee]
adapter=ezsp
baudrate=115200
port=/dev/ttyUSB0
panid=
channel=11
reset=soft
write=true

[security]
key=

[debug]
port=false
adapter=false
zigbee=false
```

!!! warning ""

    Не рекомендуется оставлять параметр `write` в секции `[zigbee]` настроенным как `true`, поскольку это может привести к случайному изменению настроек координатора и необходимости повторного добавления всех устройств в сеть.

Подробнее о параметрах конфигурации можно почитать [здесь](/zigbee/configuration/).

## Запуск контейнера

```sh
docker run \
  --detach \
  --volume /opt/homed-zigbee:/data \
  --device /dev/ttyUSB0 \
  --name homed-zigbee \
  docker.u236.org/homed-zigbee
```

| Параметр | Описание |
|----------|----------|
| `--volume` | проброс каталога `/opt/homed-zigbee` на хосте в каталог `/data` внутри контейнера |
| `--device` | проброс порта координатора внутрь контейнера |
| `--name`   | название контейнера |

## Что дальше?

После успешной настройки и запуска контейнера _HOMEd ZigBee_ можно переходить к добавлению устройств в сеть, при помощи [веб-интерфейса](/web/) или [вручную](/zigbee/commands/).
