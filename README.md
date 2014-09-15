xenserver-patch
===============

Apply hotfixes and service packs to Xenserver 6.2 without Xencenter 

This script applies the most current patches to Xenserevr 6.2 via command line, you won't need the paid version of Xencenter to patch your hosts.

Install
-------
1. git clone
2. copy the xen-patch.py file to your xenserver (via scp or whatever)
3. ssh into xenserver as root and run the script

Usage
-----
Everything in red are patches not yet applied, and everything in green are patches already installed. If you run the SP patches, they will install the hotfixes automatically



Drew Rogers <drogers@chariotsolutions.com> 
