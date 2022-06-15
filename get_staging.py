#!/var/bin/python3

# Flow
# Function is_admin()

import sys, getopt, subprocess


# Initialize global variables
outputFile = "" # expect String
filePath = ""  # expect String
verbose = False  # expect Bool
hostname = "" # expect String

# Help Menu
def usage():

    print("./get_staging.py www.google.com -f /tmp/hosts -o /tmp/output")
    print("options:")
    print("-h     Print this Help menu.")
    print("-v     Verbose mode.")
    print("     Hostname (i.e: www.google.com).")
    print("-f     File to read from.")
    print("-o     File to output to")


# Function: query_dns()
    #   * dig command:  get $hostname CNAME *.edgekey.net
    #   * store dig output
    #   * parse output:  get edgekey.net CNAME *.akamaiedge.net
    #   * add string: "-staging" to ${*.akamaiedge.net} --> *.akamaiedge-staging.net
    #   * dig command: get *.akamaiedge-staging.net A ${staging-ip}
    #   * return ${staging-ip}

def query_dns(hostname) -> str:
    host = str(hostname)

    # First dns query
    dig_string = "/usr/bin/dig +noadditional +noquestion +nocomments +nocmd +nostats " + host
    # Split into list for subprocess
    p_args = dig_string.split(' ')
    # Create Subprocess to execute commands.
    proc = subprocess.Popen(p_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # First query results
    out = proc.stdout.read().replace("\t", " ")#.decode("utf-8").rstrip()
    # Creates list of each dns record in query
    split = out.splitlines()
    dns_records = [line.split() for line in split]
    print(dns_records)


def query_dns_init(hostname) -> str:
    
    # Define variables
    host = str(hostname)
    edge_hostname = ""

    # First dns query
    dig_string = "/usr/bin/dig +noadditional +noquestion +nocomments +nocmd +nostats " + host
    # Split into list for subprocess
    p_args = dig_string.split(' ')
    # Create Subprocess to execute commands.
    proc = subprocess.Popen(p_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # First query results
    out = proc.stdout.read().replace("\t", " ")#.decode("utf-8").rstrip()
    
    # Creates list of lines
    split = out.splitlines()
    dns_records = [line.split() for line in split]
    print(dns_records)


    ###### Checks first dns request for hostname to edge_hostname  ######
    print("\nStage 1: \n")
    for record in dns_records:
        # If hostname matches AND the record is cname AND it points to an edgekey / edgesuite host
        if (record[0] == hostname + '.') and (record[3] == "CNAME") and ("edgekey" or "edgesuite" in record[4]):
            print("Hostname validated: " + record[0])
            print("CNAME validated: " + record[4])
            edge_hostname = record[4]
        #except:
        #       print("This hostname is not CNAME'd to akamai")
    
    ###### Stage 2 check will search for edge_hostname to edge server ######
    print("\nStage 2: \n")
    for record in dns_records:
        if (record[0] == edge_hostname) and (record[3] == "CNAME") and ("akamaiedge" or "akadns" in record[4]):
            print("Edge Hostname validated: " + edge_hostname)
            print("Edge Server identified: " + record[4])
            edge_server = record[4]
            # If akadns, we must repeat one more time to find the edge server
            #maybe recurse to take care of this additional factor
            if ("akadns" in edge_server):
                print("\nThis is a Akamai Global Traffic Manager hostname")
                print("Needs an additional iteration to reach edge server")
                continue
            if ("akamaiedge" in edge_server):
                print("Success! This is an edge server")
                continue
            
    ###### Stage 3 will lookup the A record for edge server and return IP address
    
    

def get_opt():

    try:
        opt_list, args = getopt.getopt(sys.argv[1:], "hvo:f:", ["help", "verbose", "output=", "file="])
    except getopt.GetoptError as err:
        usage()
        sys.exit(2)
        
    
    for opt, arg in opt_list:
        # Help Menu opt
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        # Verbose opt
        elif opt in ("-v", "--verbose"):
            verbose = True
            print("Verbose = " + str(verbose))
        # Output file opt
        elif opt in ("-o", "--output"):
            outputFile = arg
            print(f"This is the outputFile: {outputFile}")  # Todo Create create_output_file() function
        # Input file opt
        elif opt in ("-f", "--file"):   # Todo: Create input_file() function
            filePath = arg
            print(f"This is the input file path: {filePath}")
            
        else:
            assert False, "unhandled option"

    if len(args) == 1:
        hostname = args[0]
        return hostname
    else:
        usage()
        

def main():
    hostname = get_opt()
    query_dns_init(hostname)
        
if __name__ == '__main__':
    main()