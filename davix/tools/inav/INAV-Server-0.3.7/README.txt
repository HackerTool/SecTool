To build the inav server 
You will need libpcap development Libraries installed.

On a Ubuntu machine use the following commands to build

YourUser@YourMachine:~$ sudo aptitude install build-essential
YourUser@YourMachine:~$ sudo aptitude install libpcap-dev
YourUser@YourMachine:~/server$ cd server
YourUser@YourMachine:~/server$ make

Then inavd should appear in your server directory.
Then run ./inavd --help for a list of options.
Remember that in order to put an interface in promisc mode inavd must be run as
root (i.e. sudo ./inavd -i eth0).
