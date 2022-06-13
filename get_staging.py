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


def main():
    outputFile = "" # expect String
    filePath = ""  # expect String
    verbose = False  # expect Bool

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvo:f:", ["help", "verbose", "output", "file"])
    except getopt.GetoptError as err:
        #usage()
        sys.exit()
    for opt, arg in opts:
        # Help Menu opt
        if opt == "-h" or opt == "--help":
            usage()
        # Verbose opt
        elif opt == "-v" or opt =="--verbose":
            verbose = True
            print("verbose")
        # Output file opt
        elif opt == "-o" or opt == "--output":
            outputFile = arg
            print(f"This is the outputFile: {outputFile}")
        # Input file opt
        elif opt == "-f" or opt == "--file":
            filePath = arg
            print(f"This is the input file path: {filePath}")
        else:
            assert False, "unhandled option"
        
if __name__ == '__main__':
    main()


def main():
    