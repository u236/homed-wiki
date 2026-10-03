---
title: 'HOMEd'
---

# HOMEd

!!! info ""

    Сама идея заняться всем этим, как и большинство хороших идей, возникла по причине банальной лени - в один прекрасный день мне не захотелось вставать с кровати, чтобы перед сном выключить во всем доме свет, _и тут началось_. Это история проб и ошибок длиной в несколько лет, прошедшая все этапы развития от кучи проводов и изоленты, развешенных по стенам, до вполне приличного, на мой взгляд, результата.

_HOMEd_ это набор маленьких и быстрых сервисов для организации системы умного дома, среди которых есть сервисы для работы с ZigBee-сетью, веб-интерфейс, рекордер статистики, служба автоматизаций и многое другое, включая возможность интеграции с [Home Assistant](https://www.home-assistant.io) и [Умным домом Яндекса](https://alice.yandex.ru/smart-home).

Все сервисы написаны на C++ с использованием фреймворка [_Qt 5_](https://doc.qt.io/qt-5) и общаются друг с другом при помощи MQTT-брокера. Выглядит это приблизительно так:

[![HOMEd Services](/assets/img/diagram/service-light.png#only-light)](/assets/img/diagram/service-light.png)
[![HOMEd Services](/assets/img/diagram/service-dark.png#only-dark)](/assets/img/diagram/service-dark.png)

## Сервисы

- [ZigBee](/zigbee/)
- [Modbus](/modbus/)
- [Custom](/custom/)
- [Automation](/automation/)
- [Recorder](/recorder/)
- [Web](/web/)
- [Cloud](/cloud/)

## Общие сведения

- [Способности устройств](/common/exposes/)
- [Опции устройств](/common/options/)
- [MQTT-топики](/common/topics/)

## Способы установки

- [APT репозиторий](/common/apt/)
- [OPKG репозиторий](/common/opkg/)
- [Аддоны Home Assistant](/common/addons/)

## Для разработчиков

- [Окружение для компиляции](/common/build/)

## Полезные ссылки

- [Сборник пользовательских рецептов](https://community.homed.dev)
- [Страница разработчика на GitHub](https://github.com/u236)
- [Канал проекта в Telegram](https://t.me/homed_info)
- [Первая версия этой Wiki](https://mediawiki.homed.dev) - _не обновляется с осени 2025 года_

<!-- - [HOMEd Gateway Nano](/hardware/nano/) -->
<!-- - [HOMEd Gateway Pico](/hardware/pico/) -->
<!-- - [HOMEd Lua](/misc/lua/) -->

