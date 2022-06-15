# Akamai Tools

Building tools to manage Akamai CDN and WAF operations.

### get_staging
Normally a host's DNS records point to the Akamai "production" edge network.
This tool allows us to input "Akamaized" hostnames and return the IP address for the Staging network.

This "Staging" IP address would then be added to your system's host file.
This enables developers and engineers to test changes on the Akamai Staging Network before pushing to the Production Network.
