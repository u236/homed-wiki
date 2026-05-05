import requests

fileURL = "https://raw.githubusercontent.com/u236/homed-service-zigbee/refs/heads/master/deploy/data/usr/share/homed-zigbee"
linkURL = "https://github.com/u236/homed-service-zigbee/blob/master/deploy/data/usr/share/homed-zigbee"

files = {
    "Aqara/Xiaomi": "lumi",
    "Philips": "hue",
    "GLEDOPTO": "gledopto",
    "GS": "gs",
    "Konke": "konke",
    "Life Control": "lifecontrol",
    "ORVIBO": "orvibo",
    "Perenio": "perenio",
    "Yandex": "yandex",
    "Sonoff": "sonoff",
    "IKEA": "ikea",
    "TUYA (TS0601)": "ts0601",
    "TUYA": "tuya",
    "HOBEIAN": "hobeian",
    "Efekta": "efekta",
    "Modkam": "modkam",
    "Bacchus": "bacchus",
    "Slacky": "slacky",
    "PushOk": "pushok",
    "...": "other",
}

for key, file in files.items():

    response = requests.get(f"{fileURL}/{file}.json")

    if response.status_code != 200:
        continue

    print(f"\n## {key}\n")

    for index, data in enumerate(response.iter_lines()):
        line = data.decode("utf-8").strip()
        if not line.startswith('"description":'):
            continue
        print(f"- [{line.split('"')[3].strip()}]({linkURL}/{file}.json#L{index + 1})")
