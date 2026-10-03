---
title: 'OPKG репозиторий'
---

# OPKG репозиторий

OPKG репозиторий позволяет устанавливать сервисы _HOMEd_ на оборудование, работающее под управлением [OpenWRT](https://openwrt.org).

## Поддерживаемые архитектуры

- `aarch64_generic`
- `arm_cortex-a7_neon-vfpv4`
- `arm_cortex-a9_neon`
- `mips_24kc`
- `mipsel_24kc`

## Добавление OPKG-ключа

```sh
wget https://opkg.homed.dev/opkg.key && \
  opkg-key add opkg.key && \
  rm opkg.key
```

## Добавление репозитория

Для добавления репозитория необходимо добавить строку в файл `/etc/opkg/customfeeds.conf`, заменив `{architecture}` на соответствующую системе архитектуру:
```
src/gz homed_packages https://opkg.homed.dev/{architecture}
```

Например:
```
src/gz homed_packages https://opkg.homed.dev/arm_cortex-a7_neon-vfpv4
```
