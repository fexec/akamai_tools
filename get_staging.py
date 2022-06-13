#!/var/bin/python3

# Flow

import os   # to expose command line tools

# Function: query_dns
#   * dig command:  get $hostname CNAME *.edgekey.net
#   * store dig output
#   * parse output:  get edgekey.net CNAME *.akamaiedge.net
#   * add string: "-staging" to ${*.akamaiedge.net} --> *.akamaiedge-staging.net
#   * dig command: get *.akamaiedge-staging.net A ${staging-ip}
#   * return ${staging-ip}

def query_dns():
    cmd = os.system("dig www.google.com")
    print(cmd)


query_dns()