import requests

xml = requests.get('http://ccu3-webui/config/xmlapi/devicelist.cgi')

print(xml.text)