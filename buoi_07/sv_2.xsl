<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

  <xsl:output method="text" encoding="UTF-8"/>

  <xsl:template match="/">
{
  "students": [
    <xsl:for-each select="school/student">
      {
        "id": "<xsl:value-of select='id'/>",
        "name": "<xsl:value-of select='name'/>",
        "date": "<xsl:value-of select='date'/>"
      }
      <xsl:if test="position() != last()">,</xsl:if>
    </xsl:for-each>
  ]
}
  </xsl:template>

</xsl:stylesheet>
