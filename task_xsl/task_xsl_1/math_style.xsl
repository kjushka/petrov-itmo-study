<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html lang="ru">
            <head>
                <meta charset="utf-8"/>
                <meta name="viewport" content="width=device-width"/>
                <title>Задание xsl 1.1</title>
                <script id="MathJax-script" async="" src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/mml-svg.js"/>
            </head>
            <body>
                <math xmlns="http://www.w3.org/1998/Math/MathML">
                    <xsl:apply-templates/>
                </math>
            </body>
        </html>
    </xsl:template>

    <xsl:template match="строка">
        <mrow>
            <xsl:apply-templates/>
        </mrow>
    </xsl:template>

    <xsl:template match="операнд">
        <mi>
            <xsl:value-of select="current()"/>
        </mi>
    </xsl:template>

    <xsl:template match="число">
        <mn>
            <xsl:value-of select="current()"/>
        </mn>
    </xsl:template>

    <xsl:template match="оператор">
        <mo>
            <xsl:value-of select="current()"/>
        </mo>
    </xsl:template>

    <xsl:template match="корень">
        <msqrt>
            <xsl:apply-templates/>
        </msqrt>
    </xsl:template>

    <xsl:template match="дробь">
        <mfrac>
            <xsl:apply-templates/>
        </mfrac>
    </xsl:template>

    <xsl:template match="верх">
        <msup>
            <xsl:apply-templates/>
        </msup>
    </xsl:template>

    <xsl:template match="низ">
        <msub>
            <xsl:apply-templates/>
        </msub>
    </xsl:template>

    <xsl:template match="низверх">
        <munderover displaystyle="true">
            <xsl:apply-templates/>
        </munderover>
    </xsl:template>
</xsl:stylesheet>