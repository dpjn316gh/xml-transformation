<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:xs="http://www.w3.org/2001/XMLSchema"
                xmlns:fn="http://www.w3.org/2005/xpath-functions"
                version="1.0">
    <xsl:output method="text" encoding="UTF-8"/>

    <!--
    <xsl:template match="project-structure">
        <xsl:apply-templates/>
        <xsl:value-of select="root/@name"/>
    </xsl:template>

    <xsl:template match="folder">
        <xsl:apply-templates/>
        <xsl:value-of select="@name"/>
    </xsl:template>

    <xsl:template match="file">
        <xsl:apply-templates/>
        -
        <xsl:value-of select="@name"/>
        <xsl:value-of select="name()"/>
    </xsl:template>
-->

    <xsl:template match="project-structure">
                <xsl:apply-templates/>
        <xsl:value-of select="root/@name"/>
    </xsl:template>


    <xsl:template match="*">
        <xsl:for-each select="//node()">

            - <xsl:value-of select="name()"/>
            - <xsl:value-of select="@name"/>
        </xsl:for-each>
    </xsl:template>


</xsl:stylesheet>