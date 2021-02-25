# requests with upload image file
import argparse
import urllib.request
import json

parser = argparse.ArgumentParser()
parser.add_argument("--image_path", type=str, default="kitten_small.jpg")
parser.add_argument("--ip_address", type=str, default="3.236.97.79")
parser.add_argument("--port", type=str, default="8080")
parser.add_argument("--model_name", type=str, default="densenet161", help="1. alexnet, 2. densenet161")
args = parser.parse_args()

if args.image_path.split(".")[-1] == "jpg":
    ext = "jpg"
elif args.image_path.split(".")[-1] == "png":
    ext = "png"
else:
    ext = "jpeg"
    
url = "http://{}:{}/predictions/{}".format(args.ip_address, args.port, args.model_name)
data = open(args.image_path, "rb")
reqbody = data.read()
data.close()
print(data)
files = {"image_file": data}

req = urllib.request.Request(
    url,
    reqbody,
    method="POST",
    headers={"Content-Type": "application/octet-stream"}   
)

with urllib.request.urlopen(req) as res:
    print(json.loads(res.read()))



