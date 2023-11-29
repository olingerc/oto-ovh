# Install
Get secrets.json from password manager
Install ovh: `pip install ovh`

(after git clone, do git pull --rebase origin master)

# Usage
Run by giving new ip as only argument
OR give `test` to set curernt IP again


# Dev Notes
https://api.ovh.com/

## I created an API key
- application `oto-sslgateway`
- /sslGateway/{serviceName}/server/{id} 

# Get info
https://api.ovh.com/console/#/sslGateway/%7BserviceName%7D/server/%7Bid%7D~GET

# Change IP adress of SSL-gateway
https://api.ovh.com/console/#/sslGateway/%7BserviceName%7D/server/%7Bid%7D~PUT
