<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" exclude-result-prefixes="xs" version="1.0">
    <xsl:output indent="yes"/>
    <xsl:template match="/">
        <TEI>
            <teiHeader>
                <fileDesc>
                    <titleStmt>
                        <title type="main">Fackel-Texte Personenregister</title>

                        <title type="sub">Digitale Edition der Fackel-Texte</title>
                    </titleStmt>
                    <publicationStmt>
                        <p>Publication Information</p>
                    </publicationStmt>
                    <sourceDesc>
                        <p>Information about the source</p>
                    </sourceDesc>
                </fileDesc>
            </teiHeader>
            <text>
                <body>
                    <listPerson>
                        <xsl:for-each select=".//person">
                            <person>
                                <xsl:attribute name="xml:id">
                                    <xsl:value-of select="concat('fk__', @code)"/>
                                </xsl:attribute>
                                <persName>
                                    <xsl:value-of select="./name/text()"/>
                                </persName>
                                <xsl:for-each select="./event[@type='birth']">
                                    <birth>
                                        <xsl:for-each select="./date/text()"><date><xsl:value-of select="."/></date></xsl:for-each>
                                        <xsl:for-each select="./place/text()"><place><xsl:value-of select="."/></place></xsl:for-each>
                                    </birth>
                                </xsl:for-each>
                                <xsl:for-each select="./event[@type='death']">
                                    <death>
                                        <xsl:for-each select="./date/text()"><date><xsl:value-of select="."/></date></xsl:for-each>
                                        <xsl:for-each select="./place/text()"><place><xsl:value-of select="."/></place></xsl:for-each>
                                    </death>
                                </xsl:for-each>
                                <xsl:for-each select=".//denom">
                                    <occupation><xsl:value-of select="./text()"/></occupation>
                                </xsl:for-each>
                                <xsl:for-each select=".//comment">
                                    <note type="comment">
                                        <xsl:value-of select="."/>
                                    </note>
                                </xsl:for-each>
                            </person>
                        </xsl:for-each>
                    </listPerson>
                </body>
            </text>
        </TEI>
    </xsl:template>
</xsl:stylesheet>
