---
title: 'ZigBee: Конфигурация'
---

# ZigBee: Конфигурация

Конфигурация _HOMEd ZigBee_ хранится в файле `/etc/homed/homed-zigbee.conf`. Пример файла конфигурации:

```ini
[log]
enabled=false
timestamps=true
file=/var/log/homed.log

[mqtt]
host=localhost
port=1883
username=zigbee
password=secret
prefix=homed
instance=
names=false
debounce=true

[homeassistant]
enabled=true
prefix=homeassistant
status=homeassistant/status
update=false

[default]
discovery=true
cloud=true

[device]
database=/opt/homed-zigbee/database.json
properties=/opt/homed-zigbee/properties.json
options=/opt/homed-zigbee/options.json
ota=/opt/homed-zigbee/ota
external=/opt/homed-zigbee/external
library=/usr/share/homed-zigbee
expose=/usr/share/homed-common/expose.json

[gpio]
status=71
blink=83
boot=109
reset=23

[zigbee]
adapter=znp
port=/dev/ttyUSB0
baudrate=115200
panid=0x1010
channel=11
reset=flow
write=false

[security]
key=0x000102030405060708090a0b0c0d0e0f

[debug]
port=false
adapter=false
zigbee=false
```

!!! info ""

    При изменении содержимого файла конфигурации сервис перезапускается автоматически.

## Параметры

#### `[log]`

| Параметр | Описание |
|----------|----------|
| `enabled`    | включение/выключение записи логов в файл |
| `timestamps` | включение/выключение меток времени при выводе лога в `stdout` |
| `file`       | путь к файлу лога |

#### `[mqtt]`

| Параметр | Описание |
|----------|----------|
| `host`     | адрес брокера |
| `port`     | порт брокера |
| `username` | имя пользователя для авторизации на брокере (может быть пустым) |
| `password` | пароль для авторизации на брокере (может быть пустым) |
| `prefix`   | корневой топик |
| `interval` | интервал публикации топика [доступности](/common/topics/#service) в секундах |
| `instance` | уникальное имя сервиса (может быть пустым), подробности [ниже](#_2) |
| `names`    | использование имен устройств вместо адресов в MQTT-топиках |
| `debounce` | включение/выключение повторной публикации данных, подробности [ниже](#_3) |

#### `[homeassistant]`

| Параметр | Описание |
|----------|----------|
| `enabled` | включение/выключение функции [Home Assistant MQTT Discovery](https://www.home-assistant.io/integrations/mqtt/#mqtt-discovery) |
| `prefix`  | корневой топик для [Home Assistant MQTT Discovery](https://www.home-assistant.io/integrations/mqtt/#mqtt-discovery) |
| `status`  | топик для отслеживания [состояния Home Assistant](https://www.home-assistant.io/integrations/mqtt/#birth-and-last-will-messages) |
| `update`  | включение/выключение автоматического обновления `entity_id` при переименовании устройств |

#### `[default]`

| Параметр | Описание |
|----------|----------|
| `enabled` | состояние функции [Home Assistant MQTT Discovery](https://www.home-assistant.io/integrations/mqtt/#mqtt-discovery) для новых устройств по умолчанию |
| `cloud`   | состояние функции [HOMEd Cloud](/cloud/) для новых устройств по умолчанию |

#### `[device]`

| Параметр | Описание |
|----------|----------|
| `database`   | путь к файлу базы данных устройств |
| `properties` | путь к файлу, в котором будут храниться актуальные (последние известные) состояния устройств |
| `options`    | путь к файлу настройки индивидуальных опций устройств |
| `ota`        | путь к каталогу с файлами обновлений прошивок устройств |
| `external`   | путь к каталогу пользовательских расширений библиотеки устройств |
| `library`    | путь к каталогу библиотеки устройств |
| `expose`     | путь к файлу с [опциями](/common/options/) типовых [способностей](/common/exposes/) устройств |

#### `[gpio]`

| Параметр | Описание |
|----------|----------|
| `status`| порт светодиода для индикации режима добавления устройств |
| `blink` | порт светодиода для индикации активности в сети |
| `boot`  | порт, к которому подключен вход управления режимом загрузки координатора |
| `reset` | порт, к которому подключен вход управления перезагрузкой координатора |

#### `[zigbee]`

| Параметр | Описание |
|----------|----------|
| `adapter`  | тип адаптера, возможные значения: `ezsp`, `zboss`, `zigate`, `znp` |
| `port`     | последовательный порт, к которому подключен координатор или адрес для [сетевого подключения](#_4) |
| `baudrate` | скорость последовательного порта (при подключении через локальный порт) |
| `panid`    | идентификатор сети (в шестнадцатеричном формате, 2 байта)<br>___если значение не указано, оно будет сгенерировано автоматически___ |
| `channel`  | номер канала ZigBee |
| `power`    | максимальная мощность передатчика адаптера в __dBm__ |
| `reset`    | способ управления перезагрузкой координатора, возможные значения: `gpio`, `flow`, `soft` |
| `write`    | разрешение/запрет перезаписывать конфигурацию координатора, подробности [ниже](#_5) |

!!! warning ""

    Во избежание проблем, связанных с конфликтами сетей, обязательно используйте уникальное значение параметра `panid` для каждой сети в пределах одной локации, если эти сети работают на одном канале.

#### `[security]`

| Параметр | Описание |
|----------|----------|
| `key` | ключ сети (в шестнадцатеричном формате, 16 байт)<br>___если значение не указано, оно будет сгенерировано автоматически___ |

#### `[debug]`

| Параметр | Описание |
|----------|----------|
| `port`    | вывод в лог дампов сырых данных последовательного порта |
| `adapter` | вывод в лог дампов обмена данными с координатором |
| `zigbee`  | вывод в лог дампов входящих данных от устройств |

## Кластеризация

_HOMEd ZigBee_ позволяет использовать несколько "инстансов" сервиса внутри одного корневого топика, это нужно, например, для централизованного управления всеми "инстансами" из одного [веб-интерфейса](/web/) или для организации перекрестных [автоматизаций](/automation/) между "инстансами".

Для корректной работы этих функций _необходимо_, чтобы у каждого "инстанса" было свое уникальное имя, при этом имя _одного_ из "инстансов" может быть пустым. Остальные сервисы устроены так, что смена уникальных имен для "инстансов" не должна влиять на их работу, однако не стоит забывать, что некоторые MQTT-топики сервисов публикуются с флагом __retain__, поэтому переименование "инстансов" без ручной зачистки таких топиков может привести к нежелательным последствиям.

!!! warning ""

    Уникальное имя "инстанса" может быть строкой, состоящей из любых символов, за исключением спец-символов, используемых в MQTT-топиках: `#`, `+` и `/`.

    Тем не менее, во избежание потенциальных проблем, рекомендуется использовать строки без пробелов, состоящие только из латинских букв и цифр, например: `guestHouse`.

## Повторная публикация данных

Параметр `debounce` в секции `[mqtt]` отвечает за поведение сервиса в случае, если данные, полученные от устройства, не отличаются от данных, полученных ранее.

Если параметр настроен как `true`, сервис будет игнорировать такие данные и публиковать только изменения, это позволяет снизить нагрузку на брокер и на другие сервисы. Такой режим работы используется по умолчанию.

Если же он настроен как `false`, данные будут публиковаться каждый раз при получении сообщений от устройства, даже если они не изменились. Кроме того, в этом случае для каждого устройства будет добавлено специальное свойство `messageCount`, отображающее количество сообщений, полученных от устройства с момента запуска сервиса, что позволяет выявить устройства, создающие большую нагрузку на сеть.

## Работа с GPIO

Управление _GPIO_ осуществляется через драйвер `/sys/class/gpio`. В качестве значения для каждого параметра в секции `[gpio]` может быть указан либо номер порта, либо путь к файлу управления портом, например: `/sys/class/gpio/gpio32/value`. Если используется путь к файлу управления, порт должен быть _заведомо_ инициализирован.

При необходимости инвертировать логику управления _GPIO_ нужно добавить к значению параметра суффикс `|invert`. В этом случае при передаче логической `1` на порт будет фактически подаваться `0` и наоборот. Допускается использование суффикса как с номерами портов, так и с путями к файлам управления, например: `32|invert` или `/sys/class/gpio/gpio32/value|invert`.

Параметры `status` и `blink` могут содержать одинаковое значение, в этом случае для обоих функций будет использоваться один и тот же светодиод.

В случае, когда управление _GPIO_ не поддерживается системой или просто не требуется, нужно либо указать специальное значение `-1` для ненужного порта, либо удалить из файла конфигурации соответствующие строки.

## Сетевое подключение

_HOMEd ZigBee_ поддерживает работу с координатором по сети, через TCP сокет, например, через [ser2net](https://linux.die.net/man/8/ser2net) в режиме RAW.

Для использования этой функции в качестве значения параметра `port` в секции `[zigbee]` нужно указать строку в формате `tcp://address:port`, например:

```ini
[zigbee]
...
port=tcp://192.168.1.23:4832
...
```

## Конфигурация координатора

При каждом запуске _HOMEd ZigBee_ проверяет настройки координатора и сравнивает их с настройками, заданными в файле конфигурации. В случае, если настройки ___не___ совпадают, дальнейшее поведение сервиса определяется параметром `write` в секции `[zigbee]`.

Если параметр настроен как `true`, сервис перезапишет настройки координатора и продолжит запуск, в противном случае в логе появится запись о несовпадении параметров и работа сервиса будет остановлена:

```
...
2025.09.29 11:52:58.237 (wrn) zigbee: Adapter configuration can't be changed, write protection enabled
2025.09.29 11:52:58.237 (wrn) zigbee: Coordinator startup failed
...
```

!!! warning ""

    Не рекомендуется оставлять параметр `write` настроенным как `true`, поскольку это может привести к случайному изменению настроек координатора и необходимости повторного добавления всех устройств в сеть.

## Примеры конфигурации

=== "HOMEd Gateway Nano"

    ```ini
    [log]
    enabled=false
    file=/var/log/homed.log

    [mqtt]
    host=localhost
    port=1883
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
    database=/opt/homed-zigbee/database.json
    properties=/opt/homed-zigbee/properties.json
    options=/opt/homed-zigbee/options.json
    external=/opt/homed-zigbee/external
    library=/usr/share/homed-zigbee

    [gpio]
    status=/sys/class/leds/amber:act/brightness
    blink=/sys/class/leds/blue:zb/brightness
    boot=/sys/class/gpio/zb:boot/value
    reset=/sys/class/gpio/zb:reset/value

    [zigbee]
    adapter=znp
    port=/dev/ttyS0
    baudrate=115200
    panid=
    channel=11
    reset=gpio
    write=true

    [security]
    key=

    [debug]
    port=false
    adapter=false
    zigbee=false
    ```

=== "HOMEd Gateway Pico"

    ```ini
    [log]
    enabled=false
    file=/var/log/homed.log

    [mqtt]
    host=localhost
    port=1883
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
    database=/opt/homed-zigbee/database.json
    properties=/opt/homed-zigbee/properties.json
    options=/opt/homed-zigbee/options.json
    external=/opt/homed-zigbee/external
    library=/usr/share/homed-zigbee

    [gpio]
    status=/sys/class/leds/amber:status/brightness

    [zigbee]
    adapter=znp
    port=/dev/ttyS2
    baudrate=115200
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

=== "Geniatech GTW360"

    ```ini
    [log]
    enabled=false
    file=/var/log/homed.log

    [mqtt]
    host=localhost
    port=1883
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
    database=/opt/homed-zigbee/database.json
    properties=/opt/homed-zigbee/properties.json
    options=/opt/homed-zigbee/options.json
    external=/opt/homed-zigbee/external
    library=/usr/share/homed-zigbee

    [gpio]
    status=/sys/class/leds/amber/brightness
    boot=/sys/class/gpio/zigbee-boot/value
    reset=/sys/class/gpio/zigbee-reset/value

    [zigbee]
    adapter=zboss
    port=/dev/ttymxc3
    baudrate=115200
    panid=
    channel=11
    reset=gpio
    write=true

    [security]
    key=

    [debug]
    port=false
    adapter=false
    zigbee=false
    ```

=== "Perenio PEACG01"

    ```ini
    [log]
    enabled=false
    file=/var/log/homed.log

    [mqtt]
    host=localhost
    port=1883
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
    database=/opt/homed-zigbee/database.json
    properties=/opt/homed-zigbee/properties.json
    options=/opt/homed-zigbee/options.json
    external=/opt/homed-zigbee/external
    library=/usr/share/homed-zigbee

    [gpio]
    status=/sys/class/leds/white:power/brightness
    blink=/sys/class/leds/white:wlan/brightness
    reset=/sys/class/gpio/zigbee:reset/value

    [zigbee]
    adapter=ezsp
    port=/dev/ttyUSB0
    baudrate=115200
    panid=
    channel=11
    reset=gpio
    write=true

    [security]
    key=

    [debug]
    port=false
    adapter=false
    zigbee=false
    ```

=== "Xiaomi DGNWG05LM"

    ```ini
    [log]
    enabled=false
    file=/var/log/homed.log

    [mqtt]
    host=localhost
    port=1883
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
    database=/opt/homed-zigbee/database.json
    properties=/opt/homed-zigbee/properties.json
    options=/opt/homed-zigbee/options.json
    external=/opt/homed-zigbee/external
    library=/usr/share/homed-zigbee

    [gpio]
    boot=40
    reset=41

    [zigbee]
    adapter=zigate
    port=/dev/ttymxc1
    baudrate=115200
    panid=
    channel=11
    reset=gpio
    write=true

    [security]
    key=

    [debug]
    port=false
    adapter=false
    zigbee=false
    ```

## Что дальше?

После настройки _HOMEd ZigBee_ можно приступать к добавлению устройств в сеть, при помощи [веб-интерфейса](/web/) или [вручную](/zigbee/commands/).
