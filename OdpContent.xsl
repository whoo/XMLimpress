<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"		xmlns:xsl="http://www.w3.org/1999/XSL/Transform"	  xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0"		xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0"		xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0"		xmlns:presentation="urn:oasis:names:tc:opendocument:xmlns:presentation:1.0"		xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0"		xmlns:xlink="http://www.w3.org/1999/xlink"		 exclude-result-prefixes="text">
		<xsl:output method="xml" encoding="UTF-8" indent="yes"/>
		<xsl:template match="office:presentation">
				<impress>
						<increment x="1000" y="1000" angle="45" length="4" />
						<title>
						</title>
						<style>				body { background-color: gray;  font-family: Arial, Helvetica;}				.step {				width: 800px;				height: 600px;				}				.slide {				background-color: white;				border-radius: 20px;				padding: 10px;				}				.slide div:first-child P {				font-size: 4em;				}			</style>
						<xsl:apply-templates select="draw:page"/>
				</impress>
		</xsl:template>
		<xsl:template match="draw:page">
				<xsl:variable name="name" select="./@draw:name" />
				<step id="{$name}">
						<xsl:apply-templates select="draw:frame"/>
				</step>
		</xsl:template>
		<xsl:template match="draw:frame">
				<xsl:variable name="fstyle" select="./@draw:style-name"/>
				<xsl:variable name="width" select="./@svg:width" />
				<xsl:variable name="height" select="./@svg:height" />
				<!-- div style="{$fstyle}" -->
				<div class="{$fstyle} ">
						<xsl:apply-templates select="draw:image">
								<xsl:with-param name="width" select="$width"/>
								<xsl:with-param name="height" select="$height"/>
						</xsl:apply-templates>
						<xsl:apply-templates select="*/text:p"/>
						<xsl:apply-templates select="*/text:list"/>
				</div>
		</xsl:template>
		<xsl:template match="text:p">
				<p>
						<xsl:value-of select="."/>
				</p>
		</xsl:template>
		<xsl:template match="text:list">
				<ul>
						<xsl:apply-templates select="text:list-item"/>
				</ul>
		</xsl:template>
		<xsl:template match="text:list-item">
				<li>
						<xsl:apply-templates select="text:p"/>
				</li>
		</xsl:template>
		<xsl:template match="draw:image">
				<xsl:param name="width" />
				<xsl:param name="height" />
				<xsl:variable name="img" select="./@xlink:href" />
				<img src="{$img}" width="{$width}" height="{$height}" style="transform:rotate(1.5700981950941);"/>
		</xsl:template>
</xsl:stylesheet>
