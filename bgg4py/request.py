import requests
import xmltodict
import time

API_VERSION1 = "https://www.boardgamegeek.com/xmlapi"
API_VERSION2 = "https://www.boardgamegeek.com/xmlapi2"


def fetch_api(resouce: str, params: dict = {}, retry=3):

    # geeklist is version1 only.
    if resouce.startswith("geeklist"):
        url = f"{API_VERSION1}/{resouce}"
    else:
        url = f"{API_VERSION2}/{resouce}"

    sleep_time = 5
    while True:
        res = requests.get(url, params)
        if res.status_code == 200:
            print(res.url)
            text = res.text.encode("utf-8")
            dic = xmltodict.parse(text)
            return dic

        retry -= 1
        if retry == 0:
            # TODO
            None

        time.sleep(sleep_time)
        sleep_time = (int)(sleep_time * 1.5)
