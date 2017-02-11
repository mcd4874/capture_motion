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
result = cloudinary.uploader.upload("/Users/jessecochran/Documents/brickhack/capture_motion/test.jpg")


url = str(result['url'])
image_url = {"url": url}

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '9af8ddbf990f47b79733d388e18299ab',
}
print(image_url)
params = urllib.urlencode({
})

conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
conn.request("POST", "/emotion/v1.0/recognize?%s", str(image_url), headers)
response = conn.getresponse()
data = response.read()
print(data)
conn.close()
#except Exception as e:
   # print("[Errno {0}] {1}".format(e.errno, e.strerror))
