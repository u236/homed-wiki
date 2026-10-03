---
title: 'Recorder: OPKG'
---

# Recorder: OPKG

Перед установкой сервиса необходимо добавить в систему OPKG репозиторий _HOMEd_, если он еще не был добавлен.

Инструкция по добавлению репозитория находится [здесь](/common/opkg/).

## Установка и обновление сервиса

```sh
opkg update && opkg install homed-recorder
```

## Что дальше?

После успешной установки _HOMEd Recorder_ можно переходить к [конфигурации](/recorder/configuration/).
