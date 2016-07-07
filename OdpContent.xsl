<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0"
	xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0"
	xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0"
	 exclude-result-prefixes="text">

<xsl:output method="xml" encoding="UTF-8" indent="yes"/>


		<xsl:template match="office:presentation">
			<impress>
			<increment x="1000" y="1000" angle="45" length="4" />
			<title>
			</title>
			<style>
				.step {
				width: 800px;
				height: 600px;
			}
			</style>

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
<div>
<xsl:apply-templates select="*/text:p"/>
</div>
</xsl:template>

<xsl:template match="text:p">
<p>
<xsl:value-of select="."/>
</p>
</xsl:template>

</xsl:stylesheet>
