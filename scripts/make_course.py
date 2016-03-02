'''
This is a helper script which allows us to make a new course in
edX Studio via AJAX requests. We'd like to script the creation
of the L@S courses. This works, but requires us to manually
pull out the session ID from a log into edX Studio. We'd like
to fix this at some point, but we probably won't.
'''

import json
import requests

course_name = "A modern approach to MOOC design"
course_slug = "f0_modern"

csrf = "HnMvNFTyT5M79oM8QM2uK9x5dXvjcztF"

url = "http://localhost:8001/course/"
payload = {"org": "LAS",
           "number": course_slug,
           "display_name": course_name,
           "run": "2016"}

cookies = {
    "djdt": "hide",
    "edxloggedin": "true",
    "sessionid": '"1|lepeukn3scbu5dfb84tphmsukiviylj6|NVZe5BsqtyGn|IjFhNDkwMDE3OGE1OGU3YWI4YTQ5YmZjOTk2ZGNiYTI2N2IyMWYwZGU4M2U3ZDM0YTQ5MzA3ZDQ0YjVmOGU0MTYi:1ab5P4:b0Q8U-58SkzcaIVpymk9fLG5aZs"',
    "csrftoken": csrf
}
headers = {
    "X-Requested-With": "XMLHttpRequest",
    "X-CSRFToken": csrf,
    "Content-Type": "application/json; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01"
}

r = requests.post(url,
                  data=json.dumps(payload),
                  cookies=cookies,
                  headers=headers)

print r.text
