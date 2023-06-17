from json  import dump
from httpx import get
from re    import findall

browsers = [
    "chrome",
    "firefox",
    "safari",
    "internet-explorer",
    "edge",
    "opera",
    "vivaldi",
    "yandex-browser",
    "chrome-os",
    "macos",
    "windows",
    "android"
]

user_agents = {} 

try:
    for os in browsers:
        response = get(f"https://www.whatismybrowser.com/guides/the-latest-user-agent/{os}")
        do_response_str = response.text
        print(F"GET {os} STATUS {response.status_code}")

        find_agents = findall(r'Mozilla/5.0[^<]*', do_response_str)
        user_agents[os] = find_agents
except:pass

with open("user_agents.json", "w") as file:
    dump(user_agents, file, indent=4)
