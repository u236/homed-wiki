---
title: 'Custom: База данных'
---

# Custom: База данных

База данных это файл, в котором хранится описание устройств. По умолчанию это `/opt/homed-custom/database.json`.

Путь к файлу базы данных может быть изменен в [конфигурации](/custom/configuration/). Не обязательно редактировать базу данных устройств вручную, намного проще настраивать устройства через [веб-интерфейс](/web/).

## Структура базы данных

База данных _HOMEd Custom_ это JSON-объект. Структура базы данных выглядит так:

```json
{
  "devices":
  [
    {
      "active": true,
      "id": "myCustomDevice1",
      "name": "My Custom Device",
      "real": false,
      "cloud": true,
      "discovery": true,
      "exposes":
      [
        ...
      ],
      "options":
      {
        ...
      }
    },
    {
      "active": true,
      "id": "myCustomDevice2",
      "name": "Other Custom Device",
      "real": true,
      "cloud": true,
      "discovery": true,
      "exposes":
      [
        ...
      ],
      "bindings":
      {
        ...
      },
      "availabilityTopic": "myCustomDevice/isOnline",
      "availabilityPattern": "{{ online if value == true else offline }}"
    }
  ]
}
```

## Параметры устройств

### `active`

Включение/выключение устройства.

### `id`

Уникальный идентификатор устройства.

### `name`

Уникальное читаемое имя устройства.

### `note`

Произвольное примечание к устройству.

### `real`

Если значение этого поля установлено как `false`, устройство будет считаться виртуальным и данные из топика [`td`](/common/topics/#td-to-device) будут автоматически дублироваться в топик [`fd`](/common/topics/#fd-from-device), в противном случае сервис будет ожидать данных от реального устройства или другого сервиса.

### `cloud`

Включение/выключение проброса устройств в [Умный дом Яндекса](https://alice.yandex.ru/smart-home) при помощи [HOMEd Cloud](/cloud/).

### `discovery`

Включение/выключение функции [Home Assistant MQTT Discovery](https://www.home-assistant.io/integrations/mqtt/#mqtt-discovery) для устройства.

### `exposes`

Список [способностей](/common/exposes/) устройства.

### `options`

Объект с [опциями](/common/options/) устройства.

### `bindings`

Объект с [биндингами](/custom/database/bindings/) устройства. Актуально только для устройств с включенным параметром `real`.

### `availabilityTopic`

MQTT-топик для определения доступности устройства. Если этот параметр отсутствует, устройство всегда будет считаться доступным. Актуально только для устройств с включенным параметром `real`.

### `availabilityPattern`

<!-- TODO: добавить якорь-->
Шаблон для определения доступности устройства. Шаблон должен возвращать строку `online` в случае, если устройство доступно, иначе устройство будет считаться недоступным. Актуально только для устройств с включенным параметром `real`.

Подробнее о шаблонах можно почитать [здесь](/custom/database/bindings/).
