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

## Suggestions
Have any suggestions? Something is missing? (😬) You can leave us an issue and we will look into it 😃
