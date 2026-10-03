---
title: 'Automation: OPKG'
---

# Automation: OPKG

Перед установкой сервиса необходимо добавить в систему OPKG репозиторий _HOMEd_, если он еще не был добавлен.

Инструкция по добавлению репозитория находится [здесь](/common/opkg/).

## Установка и обновление сервиса

```sh
opkg update && opkg install homed-automation
```

## Что дальше?

После успешной установки _HOMEd Automation_ можно переходить к [конфигурации](/automation/configuration/).
