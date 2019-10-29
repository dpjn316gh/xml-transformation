<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:xs="http://www.w3.org/2001/XMLSchema"
                xmlns:fn="http://www.w3.org/2005/xpath-functions"
                version="1.0">
    <xsl:output method="text" encoding="UTF-8"/>
    <xsl:template match="project">
# --------------------------------------------------------------------
# Copyright (c) <xsl:apply-templates select="company/@year"/> by <xsl:apply-templates select="company/@name"/>
# Project name: <xsl:apply-templates select="@name"/>
        <xsl:for-each select="authors/author">
# Author: <xsl:value-of select="@name" /> <xsl:text disable-output-escaping="yes"> </xsl:text> <xsl:value-of select="@email" />
		</xsl:for-each>
# Version: <xsl:apply-templates select="@version"/>
# --------------------------------------------------------------------
    </xsl:template>
</xsl:stylesheet>