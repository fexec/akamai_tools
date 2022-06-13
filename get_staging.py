#!/var/bin/python3

# Flow

import os   # to expose command line functions
import sys, getopt
# Function: query_dns()
#   * dig command:  get $hostname CNAME *.edgekey.net
#   * store dig output
#   * parse output:  get edgekey.net CNAME *.akamaiedge.net
#   * add string: "-staging" to ${*.akamaiedge.net} --> *.akamaiedge-staging.net
#   * dig command: get *.akamaiedge-staging.net A ${staging-ip}
#   * return ${staging-ip}

# Function is_admin()

def usage():
    print("options:")
    print("-h     Print this Help menu.")
    print("-v     Verbose mode.")
    print("     Hostname (i.e: www.google.com).")
    print("-f     File to read from.")
    print("-o     File to output to")




def query_dns(hostname) -> str:

    hostname = hostname
    # First dns query
    dig_string = f"dig +noadditional +noquestion +nocomments +nocmd +nostats {hostname}" + " | awk '{print $1, $4, $5, \"\\n\"}'"

    #cmd_string = dig_string + awk_string 
    cmd = os.system(dig_string)   # Execute
    
    print(cmd)


def get_opt():
    outputFile = "" # expect String
    filePath = ""  # expect String
    verbose = False  # expect Bool

    try:
        opt_list, args = getopt.getopt(sys.argv[1:], "hvo:f:", ["help", "verbose", "output=", "file="])
    except getopt.GetoptError as err:
        usage()
        #sys.exit(2)
        pass
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

def main():
    get_opt()
    
        
if __name__ == '__main__':
    main()

