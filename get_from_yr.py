import requests
from bs4 import BeautifulSoup

# Here is the xml data
sthlm_xml_source_url = "https://www.yr.no/place/Sweden/Stockholm/Stockholm/forecast.xml"

# Fetch the data
r = requests.get(sthlm_xml_source_url)

xml_raw = r.content

# Read in the xml data using BeautifulSoup
soup = BeautifulSoup(xml_raw, "xml")

# All forecast data will be in a <time> tag
# E.g.
"""
<time from="2020-05-10T18:00:00" to="2020-05-11T00:00:00" period="3">
<!--
 Valid from 2020-05-10T18:00:00 to 2020-05-11T00:00:00 
 -->
 <symbol number="9" numberEx="9" name="Rain" var="09"/>
 <precipitation value="3.3" minvalue="1.1" maxvalue="3.4"/>
 <!--  Valid at 2020-05-10T18:00:00  -->
 <windDirection deg="268.8" code="W" name="West"/>
 <windSpeed mps="3.7" name="Gentle breeze"/>
 <temperature unit="celsius" value="13"/>
 <pressure unit="hPa" value="1001.3"/>
 </time>
"""

times = soup.find_all("time")
for t in times:
    from_time = t.get("from")
    to_time = t.get("to")
    print("from_time: {}".format(from_time))
    print("to_time: {}".format(to_time))
    temp = t.find("temperature")
    print(temp.get("value"))
    print("")
