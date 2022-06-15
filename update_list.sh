#!/bin/bash

PARAMS=""

# set positional arguments in their o
Help_Prompt () {
   # Display Help
   echo " "
   echo " "
   echo "Script will perform dns query on a hostname, check if it's Akamized and return Akamai Staging Network IP, and optionally update a hosts file of choice"
   echo " "
   echo "Syntax: update_list www.hostname.com [-h|-v|-u|-f|-o]"
   echo " "
   echo "options:"
   echo "-h     Print this Help menu."
   echo "-v     Verbose mode."
   echo "-u     Hostname (i.e: www.google.com)."
   echo "-f     File to read from."
   echo "-o     File to output to"
}

Param_Switch () {
   while (( "$#" )); do
      case "$1" in
         "-h"|"--help")
            help_menu_flag=1
            Help_Prompt
            exit
            ;;
         "-v"|"--verbose")
            # Make sure flag is global.
            verbose_flag=1
            # Insert Verbose-ify function call here?
            shift
            ;; 
      esac
   done
}

verbose_flag=0
hostname_flag=0
file_read_flag=0

# Checks for positional arguments
hostname=$1

# dig url
query_dns () {
   tmp_hostname=${hostname}
   
  # dig +noadditional +noquestion +nocomments +nocmd +nostats "${tmp_hostname}" | awk '{print $1, $4, $5, "\n"}'

   dig_cmd="dig +noadditional +noquestion +nocomments +nocmd +nostats"

   ## Dig clean output
   first_stage=$(${dig_cmd} "${tmp_hostname}" | grep ${tmp_hostname} | grep CNAME | awk '{print $1, $4, $5, "\n"}')

   result_hostname= "${first_stage}" | awk '{print $1}'
   
   #echo "${first_stage}"

   # if ${tmp_hostname} in line[0] AND line[1] AND NAME 
   #while read -p -r line; do 
    ## then 
     #    echo "SUCCESS";
     # fi
   #done << $first_stage

   #output="$(dig +noadditional +noquestion +nocomments +nocmd +nostats ${tmp_hostname} | awk '{print $1, $4, $5, "\n"}' | grep ${tmp_hostname})" 
   
   #first_cname="(${output})" #| grep ${hostname} #| grep "CNAME")
   
   #echo "${second_stage}"

}

query_dns