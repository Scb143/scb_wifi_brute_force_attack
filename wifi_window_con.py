import os
import tempfile
ssid=input("Enter ssid :")
#ssid="JioFiber-mmz0P"
def connect_windows(ssid, password):
    profile = f"""<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>{ssid}</name>
    <SSIDConfig>
        <SSID>
            <name>{ssid}</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>{password}</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>
"""

    # Save temporary profile file
    temp_path = tempfile.gettempdir() + "\\wifi_profile.xml"
    with open(temp_path, 'w') as file:
        file.write(profile)

    os.system(f'netsh wlan add profile filename="{temp_path}"')
    os.system(f'netsh wlan connect name="{ssid}" ssid="{ssid}"')
    print(f"Connecting with {password} on Windows...", end="", flush=True)
    