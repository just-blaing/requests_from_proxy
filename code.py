import random
import requests
import time

# задайте свой юрл и файлик с прокси (в файле должно быть так: ip:port и так через строчку)
url = "https://example.com/"
proxy_file = "proxy.txt"


def check_proxies():
    with open(proxy_file, "r") as f:
        proxies = [line.strip() for line in f]
    for proxy in proxies:
        try:
            if "@" in proxy:
                username_password, ip_port = proxy.split("@")
                username, password = username_password.split(":")
                ip, port = ip_port.split(":")
                proxy_dict = {
                    # если у вас HTTPS запросы, то тыкай так в файле и убери комментирование:
                    # "https": f"http://{username}:{password}@{ip}:{port}",
                    "http": f"http://{username}:{password}@{ip}:{port}",
                }
            else:
                ip, port = proxy.split(":")
                proxy_dict = {
                    # если у вас HTTPS запросы, то тыкай так в файле и убери комментирование:
                    # "https": f"http://{username}:{password}@{ip}:{port}",
                    "http": f"http://{ip}:{port}",
                }
            print(f"тестим прокси {proxy}")
            response = requests.get(url, proxies=proxy_dict, timeout=5)
            if response.status_code == 200:
                print(f"отлично! статус код - 200")
                # делаем кд запросов с разных прокси
                time.sleep(random.uniform(0.1, 0.5))
            else:
                print(f"чота не так. статус код от сайта: {response.status_code}")
        except Exception as e:
            print({e})

if __name__ == "__main__":
    check_proxies()
