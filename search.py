#!/usr/bin/python
#Created by jiexian@asuri.co
#Require the shodan module,use "easy_install shodan" to install it
#The SHODAN API is paid, just enjoy it 
#
#This is the special version created for the girl I love
#Well, she might not notice this nor me

import sys
import shodan

SHODAN_API_KEY = "JstnfwY31xZvyYCOj0cW8moPEgbkpN3n"

api = shodan.Shodan(SHODAN_API_KEY)
# Wrap the request in a try/ except block to catch errors
if len(sys.argv) < 2:
    print("Please give me some option, so I can give you accurate data.")
    print("Options:")
    print("        keyword  : This is banner or keyword you want to search, such as: mysql,cisco, or you can use it like google")
    print("        port     : Set the port number to search, such as: 3389")
    print("        country  : Set the range of country to search, such as: cn,en,etc")
    print("        city     : Set the range of city to search, such as: nanjing,New York,etc")
    print("")
    print("Samples:python search.py wordpress country:'en' city:'New York' port:80")
    print("")
else:
    try:
        # Search Shodan
        results = api.search(sys.argv)

        # Show the results
        
        print('Results found:   %s' %results['total'])
        print('')
        
        for result in results['matches']:
                print( 'TIME:    %s' %result['timestamp'])
                print( 'IP:      %s' %result['ip_str'])
                #print( 'HOST     %s' %result['hostnames'])
                print( 'PORT:    %s' %result['port'])
                print( 'OS:      %s' %result['os'])
                print( result['data'])
                print( '' )
    except shodan.APIError as e:
        print( 'Error: %s' % e)
