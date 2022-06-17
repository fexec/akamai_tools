# Akamai Tools

Building tools to manage Akamai CDN and WAF operations.

### get_staging.py
Normally a host's DNS records point to the Akamai "production" edge network.
This tool allows us to input "Akamaized" hostnames and return the IP address for the Staging network.

This "Staging" IP address would then be added to your system's host file.
This enables developers and engineers to test changes on the Akamai Staging Network before pushing to the Production Network.

In it's current build, this tool parses through public dns records with DIG, particularly a series of CNAMEs with an A record at the end.

Zone Apex Mapping is not supported at this time, but will be looked into to increase the tool's effectiveness with varied DNS use cases.
