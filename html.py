def return_html(c1, c2, c3, s1, s2, s3):
    return f"""
    <html>
        <head>
            <title>Temperatura</title>
            <meta http-equiv="refresh" content="1">
        </head>
        <body>
            <div style="font-size: 60px; text-align: center; margin-top: 100px;">
                Temperaturos
            </div>
            <div style="font-size: 48px; border: 3px solid grey; margin-top: 100px; padding: 10px">
                <div style="margin-top: 50px;">Zidinys: <span style="font-weight: bold;">{c1} C°</span></div>
                <div style="margin-top: 50px;">Paduodamas i grindis: <span style="font-weight: bold;">{c2} C°</span></div>
                <div style="margin-top: 50px; margin-bottom: 50px;">Gryztamas is grindu: <span style="font-weight: bold;">{c3} C°</span></div>
            </div>
            
            <div style="font-size: 60px; text-align: center; margin-top: 100px;">
                Sistemos busena
            </div>
            
            <div style="font-size: 48px; border: 3px solid grey; margin-top: 100px; padding: 10px">
                <div style="margin-top: 50px;">Zidinys siurblys: <span style="font-weight: bold; color: green">{s1}</span></div>
                <div style="margin-top: 50px;">Grindu siurblys: <span style="font-weight: bold; color: green">{s2}</span></div>
                <div style="margin-top: 50px; margin-bottom: 50px;">Avarinis ausinimas: <span style="font-weight: bold; color: green">{s3}</span></div>
            </div>

        </body>
    </html>
    """


class html:
    pass
