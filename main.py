from flask import Flask, request
import caesar
import helpers
import vigenere

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>
        <html>
            <head>
                <style>
                    form {{
                        background-color: #eee;
                        padding: 20px;
                        margin: 0 auto;
                        width: 540px;
                        font: 16px sans-serif;
                        border-radius: 10px;
                    }}
                    textarea {{
                        margin: 10px 0;
                        width: 540px;
                        height: 120px;
                    }}
                </style>
            </head>
            <body>
              <form method="post">
                <label for="rot">Rotate by:</label>
                <input id="rot" type="number" name="rot" value="{0}" step="1">
                <br>
                <textarea name="text" rows="4" cols="20" placeholder="Message to Encrypt" required>{1}</textarea>
                <input type="submit" value="Encrypt">
            </body>
        </html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    message = request.form['text']
    secret = caesar.encrypt(message, rot)
    return form.format(rot,secret)

@app.route("/")
def index():
    return form.format(1,"")

app.run()
