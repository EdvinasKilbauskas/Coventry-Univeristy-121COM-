# Script for working with daily currency data provided by ECB.

# url for ECM data in xml format
url = "http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"

#####################################################################
# In this block of code:
# - Python opens the url
# - reads the data
# - stores it as a string
# - closes the url
import urllib.request
page = urllib.request.urlopen(url)
data_bytes = page.read()
data_string = data_bytes.decode('utf-8')
page.close()
#####################################################################

#####################################################################
# In this block of code:
# - Python converts the string into an element tree
# - Extracts  the data and create variables:
# Each variable name is a currency code and each
#   value is the rate for 1 euro.
import xml.etree.ElementTree as ET
data_tree = ET.fromstring(data_string)
for child in data_tree[2][0]:
    countryD = child.attrib
    exec("%s = %f" % (countryD["currency"], float(countryD["rate"])))
# Note: there is a much better way for Python to handle such data
#   (called a dictionary) but we havn't met that yet. 
#####################################################################

pounds = 200*GBP 
jpy = 200*JPY


#####################################################################
#Example:
print("200 GBP = " + str(200*GBP*JPY) + str("JPY"))

#####################################################################
