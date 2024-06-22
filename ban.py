import requests
import time
import os

# Replace with your Discord webhook URL
WEBHOOK_URL = 'your_webhook_url_here'

# File to monitor
FILE_PATH = 'miscmod_bans.dat'

# File to store the position of the last processed line
POSITION_FILE = 'last_ban_position.txt'

# ID of the admin role to mention
ADMIN_ROLE_ID = 'admin_role_id'

def format_message(line):
    parts = line.split('%')
    if len(parts) != 4:
        return None  # Invalid format, skip this line
    
    banned_ip = parts[0]
    banned_player = parts[1]
    reason = parts[2]
    admin = parts[3]
    
    message = (
        f"<@&{ADMIN_ROLE_ID}> **New Ban Logged**\n"
        f"**Banned Player:** {banned_player} ({banned_ip})\n"
        f"**Reason:** {reason}\n"
        f"**Admin:** {admin}"
    )
    return message

def send_to_discord(message):
    payload = {'content': message}
    try:
        requests.post(WEBHOOK_URL, json=payload)
    except requests.exceptions.RequestException as e:
        print(f'Error sending message to Discord: {e}')

def get_last_position():
    if os.path.exists(POSITION_FILE):
        with open(POSITION_FILE, 'r') as f:
            return int(f.read().strip())
    return 0

def save_last_position(position):
    with open(POSITION_FILE, 'w') as f:
        f.write(str(position))

def monitor_file():
    print("Watching Bans...")
    last_position = get_last_position()
    while True:
        with open(FILE_PATH, 'r') as file:
            file.seek(last_position)
            lines = file.readlines()
            if lines:
                for line in lines:
                    line = line.strip()
                    if line:
                        message = format_message(line)
                        if message:
                            send_to_discord(message)
                last_position = file.tell()
                save_last_position(last_position)
        time.sleep(1)  # Adjust the interval as needed

if __name__ == '__main__':
    monitor_file()
