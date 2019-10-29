<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:xs="http://www.w3.org/2001/XMLSchema"
                version="1.0">

    <!-- <xsl:import href="http://www.xsltfunctions.com/xsl/functx-1.0-doc-2007-01.xsl"/> -->
    <xsl:output method="text"/>

    <xsl:template name="to-lower-case">
        <xsl:param name="str"></xsl:param>
        <xsl:variable name="lcletters">abcdefghijklmnopqrstuvwxyz</xsl:variable>
        <xsl:variable name="ucletters">ABCDEFGHIJKLMNOPQRSTUVWXYZ</xsl:variable>
        <xsl:variable name="name" select="translate($str,$ucletters,$lcletters)"/>
        <xsl:value-of select="$name"/>
    </xsl:template>

    <xsl:template name="to-upper-case">
        <xsl:param name="str"></xsl:param>
        <xsl:variable name="lcletters">abcdefghijklmnopqrstuvwxyz</xsl:variable>
        <xsl:variable name="ucletters">ABCDEFGHIJKLMNOPQRSTUVWXYZ</xsl:variable>
        <xsl:variable name="name" select="translate($str,$lcletters,$ucletters)"/>
        <xsl:value-of select="$name"/>
    </xsl:template>

    <xsl:template name="to-lower-initial-letter">
        <xsl:param name="str"></xsl:param>
        <xsl:param name="index">1</xsl:param>
        <xsl:param name="length">1</xsl:param>
        <xsl:variable name="lcletters">abcdefghijklmnopqrstuvwxyz</xsl:variable>
        <xsl:variable name="ucletters">ABCDEFGHIJKLMNOPQRSTUVWXYZ</xsl:variable>
        <xsl:variable name="name"
                      select="concat(translate(substring($str,$index,$length),$ucletters,$lcletters),substring($str,$index+1))"/>
        <xsl:value-of select="$name"/>
    </xsl:template>





</xsl:stylesheet>

