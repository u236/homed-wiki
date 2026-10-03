---
title: 'Recorder: Компиляция'
---

# Recorder: Компиляция

Перед компиляцией исходного кода _HOMEd Recorder_ необходимо подготовить окружение, включающее в себя нужный компилятор и библиотеки _Qt 5_.

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
git clone https://github.com/u236/homed-service-recorder.git \
  homed/homed-recorder
```

```sh
cd homed/homed-recorder
```

```sh
/my/qt/location/bin/qmake homed-recorder.pro && \
  make -j $(nproc)
```
