---
title: 'Modbus: Компиляция'
---

# Modbus: Компиляция

Перед компиляцией исходного кода _HOMEd Modbus_ необходимо подготовить окружение, включающее в себя нужный компилятор и библиотеки _Qt 5_.

Инструкция по подготовке окружения, а также готовые сборки _Qt 5_ и компиляторы, находятся [здесь](/common/build/).

## Компиляция

```sh
mkdir homed
```

```sh
git clone https://github.com/u236/homed-service-common.git \
  homed/homed-common
```

```sh
git clone https://github.com/u236/homed-service-modbus.git \
  homed/homed-modbus
```

```sh
cd homed/homed-modbus
```

```sh
/my/qt/location/bin/qmake homed-modbus.pro && \
  make -j $(nproc)
```
