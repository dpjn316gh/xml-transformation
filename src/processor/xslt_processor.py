# --------------------------------------------------------------------
# Copyleft (c) 2019
# Author Jorge Porras<dpjn316@gmail.com>
# Version: 0.0.1
# --------------------------------------------------------------------
from lxml import etree
from lxml.etree import XSLT



class XsltProcessor:

    @classmethod
    def transform(cls, xml_filename, xsl_filename, output_filepath):
        """

        Args:
            xml_filename:
            xsl_filename:
            output_filepath:

        Returns:

        """

        dom = etree.parse(xml_filename)
        xslt = etree.parse(xsl_filename)
        transform = XSLT(xslt)
        newdom = transform(dom)
        print(newdom)

