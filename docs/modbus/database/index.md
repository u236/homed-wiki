---
title: 'Modbus: База данных'
---

# Modbus: База данных

База данных это файл, в котором хранится описание устройств. По умолчанию это `/opt/homed-modbus/database.json`.

Путь к файлу базы данных может быть изменен в [конфигурации](/modbus/configuration/). Не обязательно редактировать базу данных устройств вручную, намного проще настраивать устройства через [веб-интерфейс](/web/).

## Структура базы данных

База данных _HOMEd Modbus_ это JSON-объект. Структура базы данных выглядит так:

```json
{
  "devices":
  [
    {
      "active": true,
      "type": "homedRelayController",
      "portId": 1,
      "slaveId": 11,
      "baudRate": 115200,
      "pollInterval": 1000,
      "requestTimeout": 1000,
      "replyTimeout": 5,
      "name": "Relay Controller",
      "cloud": true,
      "discovery": false
    },
    {
      "active": true,
      "type": "customController",
      "portId": 2,
      "slaveId": 25,
      "baudRate": 9600,
      "pollInterval": 1000,
      "requestTimeout": 1000,
      "replyTimeout": 10,
      "name": "Custom Controller",
      "cloud": false,
      "discovery": true,
      "items":
      [
        ...
      ],
      "options":
      {
        ...
      }
    }
  ]
}
```

## Параметры устройств

### `active`

Включение/выключение устройства.

### `type`

Тип устройства. Список доступных типов устройств можно посмотреть [здесь](/modbus/devices/).

### `portId`

Номер порта к которому подключено устройство, в соответствии с [конфигурацией](/modbus/configuration/#port-n).

### `slaveId`

Адрес устройства.

### `baudRate`

Скорость обмена данными с устройством.

### `pollInterval`

Период опроса устройства в миллисекундах.

### `requestTimeout`

Время ожидания ответа от устройства в миллисекундах.

### `replyTimeout`

Время ожидания окончания приема данных от устройства в миллисекундах.

### `name`

Уникальное читаемое имя устройства.

### `cloud`

Включение/выключение проброса устройств в [Умный дом Яндекса](https://alice.yandex.ru/smart-home) при помощи [HOMEd Cloud](/cloud/).

### `discovery`

Включение/выключение функции [Home Assistant MQTT Discovery](https://www.home-assistant.io/integrations/mqtt/#mqtt-discovery) для устройства.

### `items`

Объект с [картой регистров](/modbus/database/items) устройства. Актуально только для [устройств](/modbus/devices/) типа `customController`.

### `options`

Объект с [опциями](/common/options) устройства. Актуально только для [устройств](/modbus/devices/) типа `customController`.
