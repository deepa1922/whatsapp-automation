# whatsapp-automation
## Overview
This script automates sending messages on WhatsApp Web using Selenium. It allows you to:
- Set up a WhatsApp session with your profile.
- Wait for QR code scan.
- Send messages to any contact or group.

## Instructions

1. Install Dependencies:
   - Install Python (3.x recommended)
   - Install required packages: `pip install selenium`

2. Configure Chrome Profile:
   - Open Chrome and enter chrome://version in the address bar.
   - Locate "Profile Path" and update CHROME_PROFILE_PATH in config.py.
   - Adjust the path for your operating system

3. Run the Script:
- Open a terminal in the `whatsapp_automation` folder.
- Run the script: `python main.py`
- Follow the on-screen instructions to scan the QR code and send messages.
 
## Notes
- Keep your Chrome profile path private and do not share it publicly.
- Adjust the `time.sleep()` durations as needed for your system.
