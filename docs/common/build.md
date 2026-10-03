---
title: 'Окружение для компиляции'
---

# Окружение для компиляции

## Компиляторы

Данные компиляторы [GCC](https://ru.wikipedia.org/wiki/GNU_Compiler_Collection) предназначены для работы в среде `Linux` на процессорах с архитектурой `amd64`.

| Платформа | Целевая архитектура | Компилятор |
|-----------|---------------------|------------|
| Linux   | aarch64                  | [gcc-aarch64-none-linux-gnu-10.2.0.tar.xz](https://sandbox.u236.org/toolchain/gcc/gcc-aarch64-none-linux-gnu-10.2.0.tar.xz) |
| Linux   | armhf                    | [gcc-arm-linux-gnuebihf-9.4.0.tar.xz](https://sandbox.u236.org/toolchain/gcc/gcc-arm-linux-gnuebihf-9.4.0.tar.xz) |
| OpenWRT | aarch64_generic          | [gcc-aarch64_generic-openwrt-linux-8.4.0-musl.tar.xz](https://sandbox.u236.org/toolchain/gcc/gcc-aarch64_generic-openwrt-linux-8.4.0-musl.tar.xz) |
| OpenWRT | arm_cortex-a7_neon-vfpv4 | [gcc-arm_cortex-a7_neon-vfpv4-openwrt-linux-8.4.0-musl.tar.xz](https://sandbox.u236.org/toolchain/gcc/gcc-arm_cortex-a7_neon-vfpv4-openwrt-linux-8.4.0-musl.tar.xz) |
| OpenWRT | arm_cortex-a9_neon       | [gcc-arm_cortex-a9_neon-openwrt-linux-8.4.0-musl.tar.xz](https://sandbox.u236.org/toolchain/gcc/gcc-arm_cortex-a9_neon-openwrt-linux-8.4.0-musl.tar.xz) |
| OpenWRT | mips_24kc                | [gcc-mips_24kc-openwrt-linux-8.4.0-musl.tar.xz](https://sandbox.u236.org/toolchain/gcc/gcc-mips_24kc-openwrt-linux-8.4.0-musl.tar.xz) |
| OpenWRT | mipsel_24kc              | [gcc-mipsel_24kc-openwrt-linux-8.4.0-musl.tar.xz](https://sandbox.u236.org/toolchain/gcc/gcc-mipsel_24kc-openwrt-linux-8.4.0-musl.tar.xz) |
| Entware | aarch64                  | [gcc-aarch64-openwrt-linux-gnu-8.4.0.tar.xz](https://sandbox.u236.org/toolchain/gcc/gcc-aarch64-openwrt-linux-gnu-8.4.0.tar.xz) |
| Entware | mips                     | [gcc-mips-openwrt-linux-gnu-8.4.0.tar.xz](https://sandbox.u236.org/toolchain/gcc/gcc-mips-openwrt-linux-gnu-8.4.0.tar.xz) |
| Entware | mipsel                   | [gcc-mipsel-openwrt-linux-gnu-8.4.0.tar.xz](https://sandbox.u236.org/toolchain/gcc/gcc-mipsel-openwrt-linux-gnu-8.4.0.tar.xz) |

## Готовые сборки _Qt 5_

Данные сборки [_Qt 5_](https://doc.qt.io/qt-5) предназначены для использования в среде `Linux` на процессорах с архитектурой `amd64`.

| Платформа | Целевая архитектура | Сборка |
|-----------|---------------------|--------|
| Linux   | amd64                    | [qt-amd64-linux-5.15.4-shared.tar.xz](https://sandbox.u236.org/toolchain/qt/qt-amd64-linux-5.15.4-shared.tar.xz) |
| Linux   | aarch64                  | [qt-aarch64-linux-gnu-5.15.4-shared.tar.xz](https://sandbox.u236.org/toolchain/qt/qt-aarch64-linux-gnu-5.15.4-shared.tar.xz) |
| Linux   | armhf                    | [qt-arm-linux-gnueabihf-5.15.4-shared.tar.xz](https://sandbox.u236.org/toolchain/qt/qt-arm-linux-gnueabihf-5.15.4-shared.tar.xz) |
| OpenWRT | aarch64_generic          | [qt-aarch64_generic-openwrt-linux-5.15.4-shared.tar.xz](https://sandbox.u236.org/toolchain/qt/qt-aarch64_generic-openwrt-linux-5.15.4-shared.tar.xz) |
| OpenWRT | arm_cortex-a7_neon-vfpv4 | [qt-arm_cortex-a7_neon-vfpv4-openwrt-linux-5.15.4-shared.tar.xz](https://sandbox.u236.org/toolchain/qt/qt-arm_cortex-a7_neon-vfpv4-openwrt-linux-5.15.4-shared.tar.xz) |
| OpenWRT | arm_cortex-a9_neon       | [qt-arm_cortex-a9_neon-openwrt-linux-5.15.4-shared.tar.xz](https://sandbox.u236.org/toolchain/qt/qt-arm_cortex-a9_neon-openwrt-linux-5.15.4-shared.tar.xz) |
| OpenWRT | mips_24kc                | [qt-mips_24kc-openwrt-linux-5.15.4-shared.tar.xz](https://sandbox.u236.org/toolchain/qt/qt-mips_24kc-openwrt-linux-5.15.4-shared.tar.xz) |
| OpenWRT | mipsel_24kc              | [qt-mipsel_24kc-openwrt-linux-5.15.4-shared.tar.xz](https://sandbox.u236.org/toolchain/qt/qt-mipsel_24kc-openwrt-linux-5.15.4-shared.tar.xz) |
| Entware | aarch64                  | [qt-aarch64-openwrt-linux-gnu-5.15.4-shared.tar.xz](https://sandbox.u236.org/toolchain/qt/qt-aarch64-openwrt-linux-gnu-5.15.4-shared.tar.xz) |
| Entware | mips                     | [qt-mips-openwrt-linux-gnu-5.15.4-shared.tar.xz](https://sandbox.u236.org/toolchain/qt/qt-mips-openwrt-linux-gnu-5.15.4-shared.tar.xz) |
| Entware | mipsel                   | [qt-mipsel-openwrt-linux-gnu-5.15.4-shared.tar.xz](https://sandbox.u236.org/toolchain/qt/qt-mipsel-openwrt-linux-gnu-5.15.4-shared.tar.xz) |


## Компиляция _Qt 5_

Минимальный набор исходников _Qt 5_ для компиляции сервисов _HOMEd_, собранный из официального пакета `qt-everywhere-opensource-src-5.15.4.tar.xz`, включающий в себя модуль [qtmqtt](https://github.com/qt/qtmqtt) и несколько важных исправлений:

> [qt-src-5.15.4-homed-minimal.tar.xz](https://sandbox.u236.org/toolchain/qt-src-5.15.4-homed-minimal.tar.xz)

### Подготовка к компиляции

```sh
./configure -v \
  -opensource \
  -confirm-license \
  -release \
  -optimize-size \
  -shared \
  -prefix /my/qt/location \
  -xplatform my-qt-target \
  -c++std c++17 \
  -no-gui \
  -no-widgets \
  -no-opengl \
  -no-sql-sqlite2 \
  -no-sql-psql \
  -no-sql-mysql \
  -no-sql-odbc \
  -no-sql-oci \
  -no-sql-ibase \
  -no-sql-db2 \
  -no-freetype \
  -no-harfbuzz \
  -no-libjpeg \
  -no-libpng \
  -no-zlib \
  -nomake examples \
  -nomake tests
```

Важные параметры:

| Параметр | Описание |
|----------|----------|
| `-shared`    | динамическая линковка, для статической линковки нужно заменить на `-static` |
| `-prefix`    | путь для установки после компиляции |
| `-xplatform` | целевая архитектура |

Выбор целевой платформы:

| Платформа | Целевая архитектура | Значение `-xplatform` |
|-----------|---------------------|-----------------------|
| Linux   | aarch64 | `linux-aarch64-gnu-g++` |
| Linux   | armhf   | `linux-arm-gnueabihf-g++` |
| OpenWRT | aarch64 | `openwrt-aarch64-linux-g++` |
| OpenWRT | arm     | `openwrt-arm-linux-g++` |
| OpenWRT | i486    | `openwrt-i486-linux-g++` |
| OpenWRT | mips    | `openwrt-mips-linux-g++` |
| OpenWRT | mipsel  | `openwrt-mipsel-linux-g++` |
| Entware | aarch64 | `entware-aarch64-linux-g++` |
| Entware | mips    | `entware-mips-linux-g++` |
| Entware | mipsel  | `entware-mipsel-linux-g++` |
| ... |

### Компиляция и установка:

```sh
make -j $(nproc) && make install
```