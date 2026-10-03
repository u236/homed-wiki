---
title: 'Automation: База данных'
---

# Automation: База данных

База данных это файл, в котором хранится описание автоматизаций. По умолчанию это `/opt/homed-automation/database.json`.

Путь к файлу базы данных может быть изменен в [конфигурации](/automation/configuration/). Не обязательно редактировать базу данных автоматизаций вручную, намного проще настраивать автоматизации через [веб-интерфейс](/web).

## Элементы автоматизаций

* [Триггеры](/automation/database/triggers/)
* [Условия](/automation/database/conditions/)
* [Действия](/automation/database/actions/)

## Структура базы данных

База данных _HOMEd Automation_ это JSON-объект. Структура базы данных выглядит так:

```json
{
  "automations":
  [
    {
      "active": true,
      "mode": "single",
      "name": "my automation 1",
      "triggers":
      [
        ...
      ],
      "conditions":
      [
        ...
      ],
      "actions":
      [
        ...
      ]
    },
    {
      "active": true,
      "mode": "queued",
      "name": "my automation 2",
      "debounce": 10,
      "triggers":
      [
        ...
      ],
      "actions":
      [
        ...
      ]
    }
  ],
  "states":
  {
    ...
  }
}
```

## Параметры автоматизаций

### `active`

Включение/выключение автоматизации.

### `log`

Включение/выключение логов о процессе работы автоматизации.

### `mode`

Режим работы в случае повторного срабатывания триггера, когда действия автоматизации еще выполняются.

[![HOMEd Automation](/assets/img/diagram/automation-light.png#only-light)](/assets/img/diagram/automation-light.png)
[![HOMEd Automation](/assets/img/diagram/automation-dark.png#only-dark)](/assets/img/diagram/automation-dark.png)

Возможные значения:

| Режим | Действие |
|-------|----------|
| single   | ничего не делать |
| restart  | прервать выполнение и выполнить новый набор действий |
| queued   | не прерывать выполнение, а по окончании выполнить новый набор действий |
| parallel | не прерывать выполнение и выполнить новый набор действий параллельно с текущим |

### `name`

Название автоматизации, чтобы было проще отличать автоматизации друг от друга.

### `debounce`

Минимальный допустимый интервал между срабатываниями автоматизации в секундах.

### `triggers`

Массив [триггеров](/automation/database/triggers/) автоматизации.

Триггеры это события, которые вызывают срабатывание автоматизации, такие как изменение состояния устройства или выход какого-то параметра за заданный предел.

### `conditions`

Массив [условий](/automation/database/conditions/) автоматизации.

Автоматизация сработает только в случае, если заданные условия выполнены. Данное поле не является обязательным.

### `actions`

Массив [действий](/automation/database/actions/) автоматизации.

Действия это итоговый результат автоматизации, например, действие может изменить состояние устройства или отправить сообщение в Telegram.

## Состояния

<!-- TODO: добавить якоря -->
Состояния это способ обмена данными между автоматизациями. У каждого состояния есть свое название. Состояния могут быть установлены или удалены соответствующими [действиями](/automation/database/actions/) и могут использоваться в [условиях](/automation/database/conditions/).

В базе данных состояния хранятся во вложенном объекте `states`:

```json
{
  "states":
  {
    "windowIsOpen": true,
    "mySpecialState": "hello",
    "numericData": 24.2,
    ...
  }
}
```

## Примеры

```json
{
  "automations":
  [
    {
      "active": true,
      "name": "управление лампой на столе",
      "triggers":
      [
        {
          "type": "property",
          "endpoint": "zigbee/freePad/1",
          "property": "action",
          "equals": "singleClick"
        }
      ],
      "conditions":
      [
        {
          "type": "property",
          "endpoint": "zigbee/roomLight/2",
          "property": "status",
          "equals": "off"
        }
      ],
      "actions":
      [
        {
          "type": "property",
          "endpoint": "zigbee/tableLight",
          "property": "status",
          "value": "toggle"
        }
      ]
    },

    {
      "active": true,
      "name": "управление светом в комнате",
      "triggers":
      [
        {
          "type": "property",
          "endpoint": "zigbee/freePad/2",
          "property": "action",
          "equals": "singleClick"
        },
        {
          "type": "telegram",
          "message": "включи свет в комнате"
        }
      ],
      "actions":
      [
        {
          "type": "property",
          "endpoint": "zigbee/roomLight/2",
          "property": "status",
          "value": "on"
        }
      ]
    },

    {
      "active": true,
      "name": "уведомление о похолодании",
      "triggers":
      [
        {
          "type": "property",
          "endpoint": "zigbee/outdoorTemperature",
          "property": "temperature",
          "below": 10
        }
      ],
      "actions":
      [
        {
          "type": "telegram",
          "message": "на улице холодно"
        }
      ]
    }
  ]
}
```
