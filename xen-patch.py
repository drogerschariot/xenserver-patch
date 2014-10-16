#!/usr/bin/env python2
#
# xen-patch.py <Drew Rogers drogers@chariotsolutions.com>
#
#

import sys
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

patches = [
  {"name": "XS62ESP1", "url": "http://downloadns.citrix.com.edgesuite.net/akdlm/8707/XS62ESP1.zip"},
  {"name": "XS62ESP1002", "url": "http://downloadns.citrix.com.edgesuite.net/akdlm/8737/XS62ESP1002.zip"},
  {"name": "XS62ESP1003", "url": "http://downloadns.citrix.com.edgesuite.net/akdlm/9031/XS62ESP1003.zip"},
  {"name": "XS62ESP1005", "url": "http://downloadns.citrix.com.edgesuite.net/akdlm/9058/XS62ESP1005.zip"},
  {"name": "XS62ESP1008", "url": "http://downloadns.citrix.com.edgesuite.net/akdlm/9491/XS62ESP1008.zip"},
  {"name": "XS62ESP1009", "url": "http://downloadns.citrix.com.edgesuite.net/akdlm/9617/XS62ESP1009.zip"},
  {"name": "XS62ESP1011", "url": "http://downloadns.citrix.com.edgesuite.net/9698/XS62ESP1011.zip"},
  {"name": "XS62ESP1013", "url": "http://downloadns.citrix.com.edgesuite.net/9703/XS62ESP1013.zip"},
  {"name": "XS62ESP1014", "url": "http://downloadns.citrix.com.edgesuite.net/9708/XS62ESP1014.zip"},
  {"name": "XS62E001", "url": "http://support.citrix.com/servlet/KbServlet/download/34977-102-705578/XS62E001.zip"},
  {"name": "XS62E002", "url": "http://support.citrix.com/servlet/KbServlet/download/35140-102-705624/XS62E002.zip"},
  {"name": "XS62E004", "url": "http://downloadns.citrix.com.edgesuite.net/akdlm/8165/XS62E004.zip"},
  {"name": "XS62E005", "url": "http://downloadns.citrix.com.edgesuite.net/akdlm/8197/XS62E005.zip"},
  {"name": "XS62E009", "url": "http://downloadns.citrix.com.edgesuite.net/akdlm/8452/XS62E009.zip"},
  {"name": "XS62E010", "url": "http://downloadns.citrix.com.edgesuite.net/akdlm/8458/XS62E010.zip"},
  {"name": "XS62E011", "url": "http://downloadns.citrix.com.edgesuite.net/akdlm/8693/XS62E011.zip"},
  {"name": "XS62E012", "url": "http://downloadns.citrix.com.edgesuite.net/akdlm/8694/XS62E012.zip"},
  {"name": "XS62E014", "url": "http://downloadns.citrix.com.edgesuite.net/akdlm/8736/XS62E014.zip"},
  {"name": "XS62E015", "url": "http://downloadns.citrix.com.edgesuite.net/akdlm/9279/XS62E015.zip"},

]


def main(argv):
  # Select patch
  select = 0
  while True:
    print("Select which patch to apply:")
    count = 0
    while count < len(patches):
      exists = ''
      exists =  os.popen("xe patch-list name-label="+patches[count]['name']).read().rstrip()
      if exists != '':
        print(bcolors.OKGREEN + " " + str(count) + ": " + patches[count]['name'] + " " + bcolors.ENDC)
      else:
        print(bcolors.FAIL + " " + str(count) + ": " + patches[count]['name'] + " " + bcolors.ENDC)
      count = count + 1

    select = int(raw_input('Enter your input: '))

    if (select >= 0 and select < len(patches)):
      break

  # download patch
  os.system("wget " + patches[select]['url'])

  # unzip
  os.system("unzip "+ patches[select]['name']+".zip")

  # Add to xe patch-upload
  os.system("xe patch-upload file-name="+patches[select]['name']+".xsupdate")

  # Get host uuid
  uuid = os.popen("xe host-list | awk '/uuid/ {print $5;}'").read().rstrip()

  # Get patch uuid
  puuid = os.popen("xe patch-list name-label="+patches[select]['name']+" | awk '/uuid/ {print $5;}'").read().rstrip()

  # Apply patch
  os.system("xe patch-apply host-uuid="+uuid+" uuid="+puuid)

  # remove patches
  os.system("rm -f "+patches[select]['name']+"*")

if __name__ == "__main__":
  sys.exit(main(sys.argv[1:]))
