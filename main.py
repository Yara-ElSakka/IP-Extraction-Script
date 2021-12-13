# IP extraction script
# by yara elsakka
# 13.12.21

from socket import *

hostName = gethostname()

print(hostName)

ipAddress = gethostbyname(hostName)

print (ipAddress)

websiteName = "google.com"

websiteIP = gethostbyname(websiteName)

print(websiteIP)

print(f"google ip adress is: {websiteIP}")

# end of code