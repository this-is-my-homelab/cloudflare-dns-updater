import requests
import json
import time
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Cloudflare API credentials from environment variables
CLOUDFLARE_API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")
ZONE_ID = os.getenv("ZONE_ID")
RECORD_ID = os.getenv("RECORD_ID")

# DNS Record Details
DNS_RECORD_NAME = "wire.joeriabbo.nl"
DNS_RECORD_TYPE = "A"
TTL = 300  # Time to live in seconds

# Function to get the current public IP
def get_public_ip():
    response = requests.get("https://api.ipify.org?format=json")
    return response.json()["ip"]

# Function to update the DNS record
def update_dns_record(public_ip):
    url = f"https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/dns_records/{RECORD_ID}"
    headers = {
        "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "type": DNS_RECORD_TYPE,
        "name": DNS_RECORD_NAME,
        "content": public_ip,
        "ttl": TTL,
        "proxied": False
    }
    response = requests.put(url, headers=headers, data=json.dumps(data))
    return response.json()

# Main loop to periodically update the DNS record
def main():
    current_ip = None
    while True:
        try:
            new_ip = get_public_ip()
            if new_ip != current_ip:
                logging.info(f"New IP detected: {new_ip}. Updating DNS record...")
                result = update_dns_record(new_ip)
                if result["success"]:
                    logging.info(f"DNS record updated successfully: {new_ip}")
                    current_ip = new_ip
                else:
                    logging.error(f"Failed to update DNS record: {result}")
            else:
                logging.info("IP address has not changed. No update needed.")
        except Exception as e:
            logging.error(f"An error occurred: {e}")
        time.sleep(300)  # Check every 5 minutes

if __name__ == "__main__":
    main()
