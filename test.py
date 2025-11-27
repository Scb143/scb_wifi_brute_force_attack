import pywifi
import os
from pywifi import const
import time

def check_wifi_password_windows(ssid, password):
    """
    Attempts to connect to the specified Wi-Fi network (SSID) 
    using the provided password on a Windows system via pywifi.
    The success of the connection implies the password is correct.
    """
    
    # 1. Initialize Wi-Fi interface
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Get the first Wi-Fi interface

    print(f"🔄 Trying to connect to '{ssid}'",end="", flush=True)
    
    # 2. Configure the connection profile
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK) # Set security to WPA2-PSK
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password
    
    # 3. Remove old profiles and add the new one
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)

    # 4. Attempt to connect
    iface.connect(tmp_profile)
    
    # Give the connection process time to complete
    time.sleep(0.4) # 10 seconds is usually enough for a connection attempt

    # 5. Check the connection status
    if iface.status() == const.IFACE_CONNECTED:
        print(f"\n✅ Connection Successful! The password for '{ssid}' is **CORRECT**.")
        is_correct = True
    else:
        # Note: A failed connection means the password is wrong OR
        # the signal is too weak, the network is out of range, or the AP is rejecting the connection.
        print(f"\n❌ Connection Failed. The password for '{ssid}' is likely **INCORRECT**.\nCurrent Status Code: {iface.status()}",end="", flush=True)
        os.system('cls')

        is_correct = False

    # 6. Disconnect and clean up
    # Note: Disconnecting can take a moment
    #iface.disconnect()
    time.sleep(0)
    #iface.remove_all_network_profiles()

    return is_correct

# --- Configuration ---
# REPLACE these values with the SSID and password you want to test
TARGET_SSID = "SCB" 
TARGET_PASSWORD = "8143902464" 

def remove_leading_zeros_conversion(input_string):
    """
    Removes leading zeros by converting the string to an integer
    and then back to a string.
    """
    try:
        # Step 1: Convert the string to an integer. This discards all leading zeros.
        # Example: '00123' becomes 123
        number = int(input_string)
        
        # Step 2: Convert the integer back to a string.
        # Example: 123 becomes '123'
        return str(number)
    except ValueError:
        # Handles cases where the string isn't a valid number (e.g., "abc")
        return input_string

if __name__ == "__main__":
    # Ensure you run your terminal/command prompt as Administrator
    # to allow the script to manage Wi-Fi connections.
    print("--- Wi-Fi Password Verification Tool ---")
    #check_wifi_password_windows(TARGET_SSID, TARGET_PASSWORD)
    print("---------------------------------------")