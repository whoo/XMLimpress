#!/bin/bash


unzip -d html test.odp content.xml Pictures/*
cd html
cp ../../Kit/* .
../../OdpToXml.py
xsltproc impress.xsl res.xml > index.html

echo "Open output.html"
