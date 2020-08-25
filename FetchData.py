import requests
import json
import jsonpath

URL = 'https://reqres.in/api/users?page=2'

Response = requests.get(URL)
json_Response = json.loads(Response.text)

"""
Take API -- Can read response  status code, header and content
To get content using jsonpath -- Convert response into Jason and use Jason path 
Note: Response of jsonpath is always an Array.
pages = jsonpath.jsonpath(json_Response, "total_pages")
print(pages)
assert pages[0]== 5"""
''
for i in range(0, 3):

    First_Name = jsonpath.jsonpath(json_Response, 'data[' + str(i) + '].first_name')
    print(First_Name[0])
    if First_Name[0] == "Michael":
        print('went inside')



"""
print(Response.status_code)

assert Response.status_code == 200
print(Response.content)

print(Response.headers.get("Date"))

print(Response.cookies)

print(Response.elapsed)
"""
