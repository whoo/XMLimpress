#!/usr/bin/env python3

from lxml import etree
import re

xml = etree.parse("content.xml")


namespaces={
"office":"urn:oasis:names:tc:opendocument:xmlns:office:1.0",
"draw":"urn:oasis:names:tc:opendocument:xmlns:drawing:1.0",
"text":"urn:oasis:names:tc:opendocument:xmlns:text:1.0"
}



r = xml.xpath('//draw:page', namespaces=namespaces)

for page in r:
    Npage=page.get("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name")
    print("<step id=",Npage,">")

    for frame in page.xpath("draw:frame", namespaces=namespaces):
        x=frame.get("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x")
        y=frame.get("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y")
        try:
            x=float(re.findall('\d+\.?\d?',x)[0])*100/28
            y=float(re.findall('\d+\.?\d?',y)[0])*100/21
        except:
            x=y=0
            print("<div></div>")

        else:
            print("<div style='position: absolute;left:%d%%;top:%d%%'></div>"%(x,y))

        for test in frame.xpath(".//draw:text-box//*",namespaces=namespaces):
            print(test.tag[len(namespaces['text'])+2:])
            print(test.text)

        for test in frame.xpath(".//draw:image",namespaces=namespaces):
            print(test.tag[len(namespaces['draw'])+2:])
            print(test.get("{http://www.w3.org/1999/xlink}href"))
