'''
This is a helper script which allows us to make a new course in
edX Studio via AJAX requests. We'd like to script the creation
of the L@S courses. This works, but requires us to manually
pull out the session ID from a log into edX Studio. We'd like
to fix this at some point, but we probably won't.
'''

import json
import os.path
import requests
import shutil
import tempfile

csrf = "HnMvNFTyT5M79oM8QM2uK9x5dXvjcztF"

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

def create_course(course_name, course_slug):
    print "Creating", course_name
    url = "http://localhost:8001/course/"
    payload = {"org": "LAS",
               "number": course_slug,
               "display_name": course_name,
               "run": "2016"}
    return
    r = requests.post(url,
                      data=json.dumps(payload),
                      cookies=cookies,
                      headers=headers)

def add_author_to_course(course_slug, author_email):
    print "Adding", author_email, "to", course_slug
    url = "http://localhost:8001/course_team/course-v1:LAS+{course_slug}+2016/{author_email}"
    url = url.format(course_slug = course_slug, author_email = author_email)
    payload = {"role": "instructor"}
    return
    r = requests.post(url,
                      data=json.dumps(payload),
                      cookies=cookies,
                      headers=headers)

def upload_template_course(course_name, course_slug):
    print "Importing", course_name, course_slug
    base_dir = tempfile.mkdtemp()
    print base_dir
    shutil.copytree("/home/pmitros/src/las-template/", base_dir)
    sys.exit(-1)
    for filename in ['/course/course.xml',
                 '/course/problem/A_quick_quiz.xml']:
        formatted = open(filename+".tmpl").read().format(slug=course_slug)
        f = open(filename, "w")
        f.write(formatted)
        f.close()
    for filename in ["/course/html/Main_Presentation.html",
                 "/course/html/Abstract_0.html",
                 "/course/html/Other_papers_1.html",
                 "/course/html/Our_supplementary_resources_0.html",
                 "/course/html/Intake_0.html",
                 "/course/html/Supplementary_Resources_0.html",
                 "/course/problem/A_quick_quiz.xml"]:
        new_name = os.path.dirname(filename)+course_slug+"_"+os.path.basename(filename)
        shutil.move(filename, new_name)

    url = "http://localhost:8001/import/course-v1:LAS+{course_slug}+2016"
    url.format(course_slug = course_slug)
    return
    r = requests.post(url, data=open("file.tar.gz"))

for line in open("course_list.csv"):
    line = line.split('\t')
    course_slug = line[0]
    course_name = line[1]
    course_authors = [x.strip() for x in line[2].split("\t")]
    create_course(course_name, course_slug)
    create_course("Scratchpad for "+course_name, "SCRATCH_"+course_slug)
    for author_email in course_authors:
        add_author_to_course(course_slug, author_email)
        upload_template_course(course_slug, author_email)
        add_author_to_course("SCRATCH_"+course_slug, author_email)
