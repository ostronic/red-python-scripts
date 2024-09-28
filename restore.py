#!/bin/ !python
import time

def restore():
    """ Script to put things in normal after attacking a target through  """
    print("Stopping Deauthentication... \nKilling processes and restoring normal states...")

    # Put wireless in Managed mode
    print("Putting Wifi adapter into managed mode:")
    # This is another way to put it back into managed mode. You can also use iwconfig, or ip link set.
    subprocess.run(["airmon-ng", "stop", hacknic], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # Restarting additional processes makes sure that everything is back to normal with putting controller into managed mode.
    subprocess.run(["systemctl", "restart", "NetworkManager", "wpa_supplicant.service"])
    # Printing the reuslt to standout output to show the WiFi nic in managed mode and active.
    subprocess.run(["systemctl", "status", "NetworkManager", "wpa_supplicant.service"],  stdout=subprocess.STDOUT)
    time.sleep(5)
    subprocess.call("clear", shell=True)