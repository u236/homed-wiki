---
title: 'APK репозиторий'
---

# APK репозиторий

APK репозиторий позволяет устанавливать сервисы _HOMEd_ на оборудование, работающее под управлением [OpenWRT](https://openwrt.org) версии 25.12 и выше.

## Поддерживаемые архитектуры

- `aarch64_generic`
- `arm_cortex-a7_neon-vfpv4`
- `arm_cortex-a9_neon`
- `mips_24kc`
- `mipsel_24kc`

## Добавление APK-ключа

```sh
wget -O /etc/apk/keys/homed.pem https://apk.homed.dev/apk.key
```

## Добавление репозитория

```sh
echo "https://apk.homed.dev/$(cat /etc/apk/arch)/packages.adb" > \
  /etc/apk/repositories.d/homed.list
```
