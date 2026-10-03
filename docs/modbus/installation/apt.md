---
title: 'Modbus: APT'
---

# Modbus: APT

Перед установкой сервиса необходимо добавить в систему APT репозиторий _HOMEd_, если он еще не был добавлен.

Инструкция по добавлению репозитория находится [здесь](/common/apt/).

## Установка сервиса

```bash
sudo apt update && sudo apt install homed-modbus
```

## Что дальше?

После успешной установки _HOMEd Modbus_ можно переходить к [конфигурации](/modbus/configuration/).
