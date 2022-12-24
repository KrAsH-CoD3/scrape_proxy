import requests
import json


def main():
    response = requests.get(
        "https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies_geolocation_anonymous/socks5.txt")
    datas: list = response.text.split("\n")

    # Empty the json
    with open("proxy.json", "rb+") as json_file:
        fileee: str = json_file.read()
        file_length: int = len(fileee)
        json_file.seek(0, 2)
        json_file.seek(json_file.tell() - file_length)
        json_file.truncate()
        json_file.close()

    # Write proxy in json
    with open("proxy.json", "a+") as jsonfile:
        jsonfile.write("{\n")

        for idx, data in enumerate(datas):
            proxy, country, region, city = data.split("|")
            proxyaddr: str = f'"Proxy {str(idx+1)}": ' + \
                '{"Proxy": ' + f'"{proxy}", "Country": ' + \
                f'"{country}", "Region": ' + \
                f'"{region}", "City": ' + f'"{city}"' + '}'
            jsonfile.write(f"{proxyaddr}") if idx == len(
                datas)-1 else jsonfile.write(f"{proxyaddr},\n")

        jsonfile.write("\n}")
        jsonfile.seek(0)
        read_file: str = jsonfile.read()
        read_file: json = json.loads(read_file)
        proxy_list: list = []
        for idx in range(len(datas)):
            country: str = read_file[f"Proxy {idx+1}"]["Country"]
            proxy: str = read_file[f"Proxy {idx+1}"]["Proxy"]
            if country == "Canada":
                print(country)
                proxy_list.append(proxy)
        if len(proxy_list) != 0:
            print(proxy_list)


if __name__ == "__main__":
    main()
