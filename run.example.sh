docker build -t dns-updater .
export CLOUDFLARE_API_TOKEN="your-cloudflare-api-token"
export ZONE_ID="your-zone-id"
export RECORD_ID="your-record-id"
docker run -d --name dns-updater dns-updater
