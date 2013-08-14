#!/usr/bin/python

from datetime import datetime

def create_new_post_as_now(title, comments):
    date = datetime.now()
    title_in_filename = title.replace(' ','-').lower() 
    filename = date.strftime("%Y-%m-%d-{0}.markdown".format(title_in_filename))
    
    file = open("_posts/" + filename, 'w')
    fileheader = """---
layout: post
title: {0}
comments: {1}
---\n""".format(title, comments)
    file.write(fileheader)
    file.close()
    print "Done! created new file: <{0}> with appended YAML front matter".format(filename) 

if __name__ == "__main__":
    title = raw_input("Name your new post: ")
    comments = raw_input("Set true/false on comments: ")
    create_new_post_as_now(title, comments)
    
