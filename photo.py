import cloudinary
import cloudinary.uploader
import cloudinary.api
import json
import httplib
import urllib
import base64

#Configure cloudinary
cloudinary.config(
    cloud_name="dwsxmzrpt",
    api_key="387981548284158",
    api_secret="o-lfpbw-L0mnBnC4B_iVBeV5tzU"
)

#Save json result in result
result = cloudinary.uploader.upload("/Users/jessecochran/Documents/brickhack/capture_motion/a.jpg")


url =  result['url']

headers = {
    #Request headers
    'Content-Type': 'application/son',
    'Ocp-Apim-Subscription-Key': '{subscription key}',
}

params = urllib.urlencode ({})

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, "{body}", headers)
    respose = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print "err"
