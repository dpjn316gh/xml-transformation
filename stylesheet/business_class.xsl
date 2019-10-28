<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"

                xmlns:dxmlf="http://www.datypic.com/xmlf"
                xmlns:xs="http://www.w3.org/2001/XMLSchema"
                xmlns:fn="http://www.w3.org/2005/xpath-functions"
                xmlns:local="http://www.datypic.com/local"
                xmlns:functx="http://www.functx.com" exclude-result-prefixes="dxmlf xs"
                xmlns:func="http://www.**.com"
                version="2.0"
                >


    <xsl:import  href="commons.xsl"/>
    <xsl:import  href="copyright.xsl"/>
    <xsl:output method="text" />
    <xsl:template match="crud"  >
        <xsl:apply-templates select="copyright"/>
        <xsl:apply-templates select="import"/>
        <xsl:apply-templates select="testing_functions"/>

namespace <xsl:apply-templates select="class/namespace"/>;
{
	// <xsl:value-of select="class/description/comment" />
	public class <xsl:value-of select="class/description/name" />
	{
		<xsl:for-each select="class/members/member">
			<xsl:value-of select="@scope" /> <xsl:text disable-output-escaping="yes"> </xsl:text> <xsl:value-of select="@type" /> <xsl:text disable-output-escaping="yes"> </xsl:text> <xsl:value-of select="@name" />;
		</xsl:for-each>
	}
}   </xsl:template>

    <xsl:template match="import">
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
    </xsl:template>


<xsl:function name="func:helloWorld">
  <xsl:text>Hello World!</xsl:text>
</xsl:function>

<xsl:template match="/">
<xsl:value-of select="func:helloWorld"/>
</xsl:template>

</xsl:stylesheet>
