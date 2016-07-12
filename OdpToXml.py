#!/usr/bin/env python3

from lxml import etree
import zipfile
import re


xml = etree.parse("content.xml")

outxml = etree.Element("impress")
inc= etree.Element("increment")
inc.attrib['x']="1000"
inc.attrib['y']="1000"
inc.attrib['angle']="45"
inc.attrib['length']="4"
outxml.append(inc)
outxml.append(etree.Element("title"))
outxml.append(etree.Element("style"))


namespaces={
"office":"urn:oasis:names:tc:opendocument:xmlns:office:1.0",
"draw":"urn:oasis:names:tc:opendocument:xmlns:drawing:1.0",
"text":"urn:oasis:names:tc:opendocument:xmlns:text:1.0",
"svg":"urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0"
}


def shortns(name,ns):
    return name[len(namespaces[ns])+2:]

def recurse(item,el):

    for a in item.iterchildren():
        if (a.tag=="{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}text-box"):
            continue
        tag=shortns(a.tag,"text")

        if (tag=="list"):
            tag="ul"
        if (tag=="list-item"):
            tag="li"

        endnode = etree.Element(tag)
        endnode.text=a.text
        if (a.tag=="step"):
            endnode.attrib['id']=a.get('id')

        if (len(a)>0):
            recurse(a,endnode)
        endnode.tail=a.tail
        el.append(endnode)


### main
r = xml.xpath('//draw:page', namespaces=namespaces)

for page in r:
    Npage=page.get("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}name")
    step = etree.Element("step",id=Npage)

    for frame in page.xpath("draw:frame", namespaces=namespaces):
        div=etree.Element("div")
        x=frame.get("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}x")
        y=frame.get("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}y")
        t=frame.get("{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}transform")
        w=frame.get("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}width")
        h=frame.get("{urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0}height")
        try:
            x=float(re.findall('\d+\.?\d?',x)[0])*100/28
            y=float(re.findall('\d+\.?\d?',y)[0])*100/21
        except:
            x=y=0
#       print("<div></div>")
        else:
            #print("<div style='position: absolute;left:%d%%;top:%d%%'></div>"%(x,y))
            div.attrib['style']="position: absolute;left:%d%%;top:%d%%"%(x,y)

        for test in frame.xpath("draw:text-box",namespaces=namespaces):
            #print(shortns(test.tag,"text"))
            recurse(test,div)

#        print(x)
#        print(y)
#        print(w)
#        print(h)
#        print(t)


        for test in frame.xpath(".//draw:image",namespaces=namespaces):
#            if (t):
#                print("Transform: %s"%t)

            #print(test.tag[len(namespaces['draw'])+2:])
            #print(test.get("{http://www.w3.org/1999/xlink}href"))

            #m=re.match(r"rotate \((?P<rotation>[\-0-9\.]*)\).*",t)
            #rotation=m.group('rotation')
            #m=re.match(r".*translate \((?P<x>[0-9\.]*)cm (?P<y>[0-9\.]*)cm\).*",t)

            w=float(re.findall('\d+\.?\d?',w)[0])
            h=float(re.findall('\d+\.?\d?',h)[0])
            #x=(float(m.group('x'))-float(re.findall('\d+\.?\d?',h)[0]))*100/28
            #y=float(m.group('y'))*100/21
            #rotation=abs(float(rotation))


            img=etree.Element("img")
            img.attrib['src']=test.get("{http://www.w3.org/1999/xlink}href")
            img.attrib['width']="100%"
            img.attrib['height']="100%"
            ##img.attrib['style']="transform: rotate(%frad)"%rotation

            if (t):
                print("Transform")
                m=re.match(r"rotate \((?P<rotation>[\-0-9\.]*)\).*",t)
                rotation=abs(float(m.group('rotation')))
                img.attrib['style']="transform: rotate(-%frad)"%rotation
                m=re.match(r".*translate \((?P<x>[0-9\.]*)cm (?P<y>[0-9\.]*)cm\).*",t)
                x=float(m.group('x'))-(w-h)/2
                y=float(m.group('y'))-h
                x=x*100/28
                y=y*100/21

            w=w*100/28

            div.attrib['style']="position: absolute; left:%d%%;top:%d%%;width:%d%%"%(x,y,w)

            div.append(img)

        step.append(div)

    outxml.append(step)


FILE = open("res.xml","w")
FILE.writelines(etree.tostring(outxml,pretty_print=True, encoding='utf-8').decode('utf-8'))
FILE.close()

#print(etree.tostring(outxml, pretty_print=True, encoding='utf-8').decode('utf-8'))
