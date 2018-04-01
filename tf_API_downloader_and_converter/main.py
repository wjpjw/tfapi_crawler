import urllib
import re
import pdfkit

page = urllib.urlopen("https://www.tensorflow.org/api_docs/python/").read()
keywords = re.findall("\"(https://www.tensorflow.org/api_docs/python/[/\w]+)\"", page)
for keyword in keywords:
    pdfnamegp=re.search("(?<=https://www.tensorflow.org/api_docs/python/)[/\w]+",keyword)
    pdfname=pdfnamegp.group(0).replace("/", ".")+".pdf"
    pdfkit.from_url(keyword, pdfname)
