# Discord Webhook Ban Monitor

This script monitors a file named `miscmod_bans.dat` sends a log to a specified Discord webhook. The script is designed to format the message and mention an admin role.

## Features

- Monitors `miscmod_bans.dat`.
- Formats the ban log with details about the banned player, reason, and admin.
- Sends the ban log to a specified Discord webhook.
- Mentions an admin role in each message.
- Remembers the last processed line to avoid duplicate messages after restarting.

## Setup

1. **Install dependencies:**
    - This script requires the `requests` library. Install it using pip:
    ```sh
    pip3 install requests
    ```

2. **Configure the script:**
    - Open `ban.py` and replace `your_webhook_url_here` with your Discord webhook URL.
    - Replace `1253270854792380479` with the ID of the admin role you want to mention.

## Usage

1. **Run the script:**
    ```sh
    python3 ban.py
    ```

2. **Output:**
    - It will monitor `miscmod_bans.dat` and send new ban logs to the specified Discord webhook.
