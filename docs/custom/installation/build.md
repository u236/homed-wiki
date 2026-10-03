---
title: 'Custom: Компиляция'
---

# Custom: Компиляция

Перед компиляцией исходного кода _HOMEd Custom_ необходимо подготовить окружение, включающее в себя нужный компилятор и библиотеки _Qt 5_.

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
git clone https://github.com/u236/homed-service-custom.git \
  homed/homed-custom
```

```sh
cd homed/homed-custom
```

```sh
/my/qt/location/bin/qmake homed-custom.pro && \
  make -j $(nproc)
```
