import sys
from clarifai_basic import ClarifaiApi
clarifai_api = ClarifaiApi()
url = sys.argv[1]
result = clarifai_api.tag_image_urls(url)
print result

