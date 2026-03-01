---
title: 'Modbus: Docker'
---

# Modbus: Docker

## Поддерживаемые платформы

- `linux/arm64`
- `linux/arm/v7`
- `linux/amd64`

## Подготовка

Для запуска [Docker](https://docker.com) контейнера _HOMEd Modbus_ необходимо создать каталог, в котором будут храниться данные и лог сервиса, и поместить в этот каталог файл конфигурации с именем `homed-modbus.conf`. Каталог может иметь произвольное имя, в этой статье используется каталог `/opt/homed-modbus`.

## Пример конфигурации

```ini
[log]
enabled=true

[mqtt]
host=192.168.12.76
port=1883
username=modbus
password=secret
prefix=homed
names=false

[homeassistant]
enabled=true
prefix=homeassistant
status=homeassistant/status
update=false

[device]
database=/data/database.json

[port-1]
port=/dev/ttyS1
debug=false

[port-2]
port=/dev/ttyS2
debug=false
```

Подробнее о параметрах конфигурации можно почитать [здесь](/modbus/configuration/).

## Запуск контейнера

```sh
docker run \
  --detach \
  --volume /opt/homed-modbus:/data \
  --device /dev/ttyS1 \
  --device /dev/ttyS2 \
  --name homed-modbus \
  docker.u236.org/homed-modbus
```

| Параметр | Описание |
|----------|----------|
| `--volume` | проброс каталога `/opt/homed-modbus` на хосте в каталог `/data` внутри контейнера |
| `--device` | проброс последовательных портов внутрь контейнера |
| `--name`   | название контейнера |

## Что дальше?

После настройки _HOMEd Modbus_ можно приступать к добавлению устройств, при помощи [веб-интерфейса](/web/) или [вручную](/modbus/database/).
