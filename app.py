import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <meta charset="utf-8">
        <title>My Panel</title>
    </head>
    <body style="font-family:sans-serif; text-align:center;">
        <h1>My Panel</h1>
        <p>Panel is running successfully ✅</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
