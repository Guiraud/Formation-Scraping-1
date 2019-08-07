import socks
import socket
import requests
socks.setdefaultproxy( addr="127.0.0.1", port=9050)

print(requests.get("http://icanhazip.com").text)