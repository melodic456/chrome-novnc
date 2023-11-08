#!/usr/bin/env python3
import os
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests

import subprocess

def execute_xdotool_command(command):
    subprocess.run(["xdotool"] + command.split())


from time import sleep
if __name__ == "__main__":
    sleep(30)
    # Activate Chromium window
    window_id = subprocess.check_output(["xdotool", "search", "--onlyvisible", "--name", "Chromium"]).decode().strip()
    execute_xdotool_command(f"windowactivate --sync {window_id}")
    
    # Open and set URL in new tabs
    urls = [
        "https://chrome.google.com/webstore/detail/auto-clicker-autofill/iapifmceeokikomajpccajhjpacjmibe",
        "https://chrome.google.com/webstore/detail/capmonster-cloud-%E2%80%94-automa/pabjfbciaedomjjfelfafejkppknjleh",
        "https://chrome.google.com/webstore/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn",
        "https://chrome.google.com/webstore/detail/free-vpn-zenmate-best-vpn/fdcgdnkidjaadafnichfpabhfomcebme",
        "https://chrome.google.com/webstore/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn",
        "https://chrome.google.com/webstore/detail/auto-refresh-plus-page-mo/hgeljhfekpckiiplhkigfehkdpldcggm"
    ]

    
    for url in urls:
        execute_xdotool_command("key --clearmodifiers ctrl+t")
        execute_xdotool_command("key --clearmodifiers ctrl+l")
        sleep(1)
        execute_xdotool_command(f"type '{url}'")
        execute_xdotool_command("key --clearmodifiers Return")
        sleep(1)
    
    if os.getenv("NO_SLEEP") == "1":
        if "APP_NAME" not in os.environ:
            print("APP_NAME unset, terminating...")
            exit()
        app_name = os.getenv("APP_NAME")
        while True:
            try:
                requests.get(f"https://{app_name}.herokuapp.com")
            except:
                print("Ping failed, retrying...")
                try:
                    requests.get(f"https://{app_name}.herokuapp.com")
                except:
                    print("Cannot ping app, terminating...")
            sleep(25*60)
