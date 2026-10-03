---
title: 'Аддоны Home Assistant'
---

# Аддоны Home Assistant

Некоторые сервисы _HOMEd_ можно использовать как [аддоны](https://www.home-assistant.io/addons) для операционной системы [Home Assistant OS](https://www.home-assistant.io/installation/). На данный момент аддоны доступны для следующих сервисов:

- [ZigBee](/zigbee/)
- [Modbus](/modbus/)
- [Custom](/custom/)
- [Automation](/automation/)
- [Recorder](/recorder/)
- [Web](/web/)
- [Cloud](/cloud/)

## Репозиторий

Адрес репозитория с аддонами _HOMEd_:
```
https://github.com/u236/homed-ha-addons
```

## Конфигурация

Файлы конфигурации сервисов хранятся на хосте, в каталогах `/addon_configs/<addon slug>`.

Для редактирования файлов конфигурации можно использовать аддон [File Editor](https://github.com/home-assistant/addons/blob/master/configurator/README.md) с ___выключенной___ опцией "Enforce Basepath".
