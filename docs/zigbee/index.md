---
title: 'ZigBee: Описание'
---

# ZigBee: Описание

![HOMEd ZigBee](/assets/img/service/zigbee.png){width=150px}

_HOMEd ZigBee_ это программный мост между [ZigBee](https://ru.wikipedia.org/wiki/Zigbee) сетью и MQTT-брокером, который позволяет обмениваться данными с ZigBee устройствами _любых_ производителей через MQTT без использования официальных шлюзов и приложений для этих устройств.

## Интеграции

_HOMEd ZigBee_ поддерживает функцию [Home Assistant MQTT Discovery](https://www.home-assistant.io/integrations/mqtt/#mqtt-discovery). Это значит, что при добавлении устройств в сеть они могут быть автоматически "проброшены" в _Home Assistant_, если соответствующий параметр включен в [конфигурации](/zigbee/configuration/#homeassistant).

Также устройства могут быть "проброшены" в [Умный дом Яндекса](https://alice.yandex.ru/smart-home) при помощи сервиса [HOMEd Cloud](/cloud/).

## Поддержка устройств

Список поддерживаемых устройств довольно скромен, однако архитектура _HOMEd ZigBee_ позволяет добавлять поддержку новых устройств без перекомпиляции исходного кода. Актуальный список поддерживаемых устройств можно посмотреть [здесь](/zigbee/devices/).

Кроме того, в _HOMEd ZigBee_ реализована функция распознавания неподдерживаемых устройств. В настоящий момент эта функция _может_ автоматически работать со следующими типами устройств:

- Умные выключатели
- Умные розетки
- Умные лампочки
- Моторы для штор
- Датчики открытия двери/окна
- Датчики движения
- Датчики протечки
- Датчики температуры
- Датчики влажности
- Датчики освещенности

!!! info ""

    Функция распознавания ___не гарантирует___, что любые устройства заработают, как по волшебству. Она ориентирована, в первую очередь, на простые устройства, вроде датчиков и реле. Для полноценной и корректной поддержки, в любом случае, требуется добавление устройства в [библиотеку](/zigbee/library/).

## Координатор

_HOMEd ZigBee_ поддерживает координаторы следующих типов:

- На базе чипов Texas Instruments _CC2530/2531/2538/1352/2652_ с прошивками [Z-Stack](https://github.com/Koenkk/Z-Stack-firmware/tree/master/coordinator), включая легаси-версии _1.2.x_
- На базе чипов Silicon Labs _EFR32MG1x/MG2x_ с прошивками _EZSP_
- На базе чипов NXP _JN5168/5169_ с прошивками [ZiGate](https://github.com/openlumi/ZiGate)
- На базе чипов Nordic Semiconductor _NRF52840_ с прошивками _ZBOSS NCP_

!!! warning ""

    Стабильная работа ZigBee сетей под управлением _HOMEd ZigBee_ подтверждена _только_ при использовании координаторов на базе чипов _CC2530/2531/2538/1352/2652_, координаторы на базе других чипов ___могут работать со сбоями___, особенно в сетях с большим количеством устройств. Лучшим выбором на данный момент являются координаторы на базе чипов _CC1352P1_ или _CC2652P1_.

    Для координаторов на базе чипов _EFR32MG1x/MG2x_ поддерживаются прошивки _EZSP_ с версиями не ниже _8_.

## Что дальше?

- [Поддержка устройств](/zigbee/devices/)
- [Установка](/zigbee/installation/)
- [Конфигурация](/zigbee/configuration/)
- [Библиотека устройств](/zigbee/library/)
- [Команды](/zigbee/commands/)

## Полезные ссылки

- [ZigBee Cluster Library Specification](/assets/pdf/ZigBee_Cluster_Library_Specification.pdf)
- [Z-Stack Monitor and Test API](/assets/pdf/Z-Stack_Monitor_and_Test_API.pdf)
- [EZSP Reference Guide](/assets/pdf/EZSP_Reference_Guide.pdf)
- [UART-EZSP Gateway Protocol Reference](/assets/pdf/UART-EZSP_Gateway_Protocol_Reference.pdf)
- [ZBOSS NCP Serial Protocol](/assets/pdf/ZBOSS_NCP_Serial_Protocol.pdf)
- [Репозиторий на GitHub](https://github.com/u236/homed-service-zigbee)
- [Канал проекта в Telegram](https://t.me/homed_info)
