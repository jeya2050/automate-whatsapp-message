# WhatsApp Bulk Message Sender

This Python project enables you to send unique messages to WhatsApp contacts by automatically detecting whether the provided mobile numbers are registered on WhatsApp. The program takes input data in CSV format containing names and mobile numbers, then checks if each number is associated with a WhatsApp account. If a number is registered on WhatsApp, a unique message along with the customer ID is sent to that contact.

## Requirements
- Python 3.x
- Required packages:
  - pywhatkit
  - pyautogui
  - pandas

## Installation
1. Clone or download this repository to your local machine.
2. Install the required Python packages:
   ```
   pip install pywhatkit pyautogui pandas
   ```

## Usage
1. Prepare your data in CSV format with columns for 'Name', 'Mobile Number' and 'Unique Customer id'.
2. Place your CSV file in the same directory as the Python scripts.
3. Run the `main.py` script.
4. Follow the on-screen prompts to provide necessary information such as the file name, message, and any other required details.
5. The script will automatically send messages to WhatsApp contacts if their numbers are detected.

## Limitations
- The script can currently send messages to a maximum of 1000 contacts due to limitations in WhatsApp's API and usage restrictions of the `pywhatkit` package.
- Ensure you have an active internet connection while running the script to send messages via WhatsApp.

## Important Notes
- This script is for educational and personal use only. Ensure you comply with WhatsApp's terms of service and respect privacy regulations while using this tool.
- Make sure you have the necessary permissions from your contacts before sending automated messages to them.
- Use this tool responsibly and avoid spamming or sending unsolicited messages.

## Contributors
- [Jeyaram]

## License
This project is licensed under the [MIT License](LICENSE).
