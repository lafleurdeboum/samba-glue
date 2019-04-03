#!/usr/bin/python3


import os
import sys
import subprocess
#import cgi


#ejecter = "/cgi-bin/ejecter.py"
#ejecter = sys.argv[0]

print("Content-Type: text/html\n\n")

print("<title>Drives</title>")
print("<h1>Mounted removable drives</h1>")


ejecter = os.environ["SCRIPT_NAME"]
media_dir = "/media/"

if "QUERY_STRING" in os.environ:
    query = os.environ["QUERY_STRING"]
    arguments = {
            key: item for (key, item) in 
                    [ string.split("=") for string in query.split("&") ]
    }
    if "eject" in arguments:
        if arguments["eject"] in os.listdir(media_dir):
            eject_command = "sudo -u pi eject /media/%s" % arguments["eject"]
            print("executing command <code>%s</code> :" % eject_command)
            ejection = subprocess.Popen(eject_command.split(),
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = ejection.communicate()
    
            print("<br />")
            if ejection.returncode:
                print("! %s" % err)
            else:
                print("done")
        else:
            print("! %s not mounted" % arguments["eject"])

# Print mounted partitions :
empty = True
print("<ul><br />")
for partition in os.listdir(media_dir):
    print('<li>{0} (<a href="{1}?eject={0}">eject</a>)</li>'.format(
            partition, ejecter
    ))
    empty = False
if empty:
    print("no drive mounted")
print("</ul>")

