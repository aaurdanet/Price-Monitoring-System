# Price-Monitoring-System
This Python script monitors the price of a specific product on Amazon and notifies the user via email if the price falls below a certain threshold.

## Prerequisites

- Python 3.x installed on your system.
- Libraries: `requests`, `BeautifulSoup` (from `bs4`), and `smtplib`.

## Setup

1. Clone or download the repository to your local machine.
2. Install the required libraries using pip:

```bash
pip install requests beautifulsoup4

    Set up your Gmail account for sending emails:
        Enable "Less Secure Apps" access in your Gmail account settings.
        Optionally, you can use an app password instead of your regular Gmail password for added security.

    Set the following environment variables:
        RECEIVER: The email address where you want to receive notifications.
        SENDER_EMAIL: Your Gmail email address used for sending notifications.
        SENDER_PASSWORD: Your Gmail account app password.

Usage

    Open the main.py file in a text editor.
    Replace the Amazon product URL with the URL of the product you want to monitor.
    Set the desired price threshold in the script (final_price < 180).
    Run the script:

bash

python main.py

Notes

    Ensure that the product page structure on Amazon remains consistent with the code's assumptions.
    Be cautious when using your Gmail password in scripts. Consider using app passwords for increased security.
    Amazon may block automated requests if they detect suspicious activity. Use responsibly and consider Amazon's terms of service.
    This script is provided as-is and may require modifications based on your specific use case.
