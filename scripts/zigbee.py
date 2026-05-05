import time
import requests

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

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
    "...": "other"
}

retry = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504], allowed_methods=["GET"])
session = requests.Session()
session.mount("https://", HTTPAdapter(max_retries=retry))

def fetch(url, attempts):
    for i in range(attempts):
        try:
            return session.get(url, timeout=30)
        except requests.exceptions.RequestException:
            if i == attempts - 1:
                raise
            time.sleep(2 ** i)

for key, file in files.items():

    response = fetch(f"{fileURL}/{file}.json", 5)

    if response.status_code != 200:
        continue

    print(f"\n## {key}\n")

    for index, data in enumerate(response.iter_lines()):
        line = data.decode("utf-8").strip()
        if not line.startswith('"description":'):
            continue
        print(f"- [{line.split('"')[3].strip()}]({linkURL}/{file}.json#L{index + 1})")
