# Cloudflare DNS Updater

This project is a Python script that updates a Cloudflare DNS record with your current public IP address. It is designed to run periodically and ensure your DNS record stays up-to-date.

## Features
- Automatically fetches your public IP address using `api.ipify.org`.
- Updates a specified DNS record on Cloudflare if the public IP changes.
- Uses Cloudflare's API for DNS management.
- Easy deployment with Docker.

## Requirements

### Environment Variables
Set the following environment variables before running the script:

- `CLOUDFLARE_API_TOKEN`: Your Cloudflare API token.
- `ZONE_ID`: The Zone ID for your Cloudflare domain.
- `RECORD_ID`: The Record ID for the specific DNS record to update.

### Python Dependencies
- `requests`

## Running Locally

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Install dependencies:
   ```bash
   pip install requests
   ```

3. Set environment variables:
   ```bash
   export CLOUDFLARE_API_TOKEN="your-cloudflare-api-token"
   export ZONE_ID="your-zone-id"
   export RECORD_ID="your-record-id"
   ```

4. Run the script:
   ```bash
   python update_dns.py
   ```

## Running with Docker

1. Build the Docker image:
   ```bash
   docker build -t dns-updater .
   ```

2. Run the Docker container:
   ```bash
   docker run -d \
     --name dns-updater \
     -e CLOUDFLARE_API_TOKEN="your-cloudflare-api-token" \
     -e ZONE_ID="your-zone-id" \
     -e RECORD_ID="your-record-id" \
     dns-updater
   ```

3. (Optional) Ensure the container restarts automatically:
   ```bash
   docker run -d --restart always \
     --name dns-updater \
     -e CLOUDFLARE_API_TOKEN="your-cloudflare-api-token" \
     -e ZONE_ID="your-zone-id" \
     -e RECORD_ID="your-record-id" \
     dns-updater
   ```

## Customization
- Update the `DNS_RECORD_NAME` variable in the Python script to set your desired DNS record name.
- Modify the `TTL` value to adjust the time-to-live for the DNS record.

## Troubleshooting
- Ensure your API token has the required permissions to manage DNS records.
- Verify the Zone ID and Record ID are correct for your domain and DNS record.
- Check the logs by running:
  ```bash
  docker logs dns-updater
  ```

## License
This project is licensed under the MIT License.

