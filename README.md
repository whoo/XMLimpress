#OdpToXml
============

Create your presentation with Impress odp, and share it in html format.
* print.css is available for pdf sharing
* you can customize css to add background/effect


# Original >> XMLimpress.js
=============

Generates [impress.js](https://github.com/impress/impress.js/wiki)
presentations with predesigned transitions from an XML file like prezi (but free !)

Addon
-----
* OdpToXml.py (to convert ooimpress to xml compatible file)
* Use style.css to customize your presentation
* Sorry only htmltags are used (not stylesheet)


Usage
-----

The XML file can be viewed directly in a browser by including the XSL stylesheet in it:

> <?xml-stylesheet href="impress.xsl" type="text/xsl"?>

HTML file can be generated with the command:

> xsltproc impress.xsl file.xml > file.html

XHTML file can be generated executing the same command after changing
the `output method` to `xml` in the fifth line of `impress.xsl`.

To avoid malfunctions is better to save the xml or html file, `impress.xsl` and `impress.js`
in the same directory.



Structure of XML file
---------------------

The structure of the XML file must be like in the following example:

```xml
<?xml version="1.0" encoding="UTF-8"?>

<impress numbered="yes|no">

<increment x="1000" y="1000" angle="45" length="4" />
<!--
Where:
'x' is the horizontal distance between slides
'y' is the vertical distance between slides
'angle' is the angle between two slides
'lenth' is the loop length
-->

<title>
<!--The title of the document-->
</title>

<style>
<!--Specify style options as in CSS-->
 .step {
	width: 1000px;
}
<!--at least slide width must be specified-->
</style>

<step>
<!--xhtml code for the first slide-->
</step>

<step>
<!--xhtml code for the second slide-->
</step>

<step>
<!--xhtml code for the third slide-->
</step>


</impress>

```
