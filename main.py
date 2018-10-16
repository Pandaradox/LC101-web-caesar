from flask import Flask, request
import caesar
import helpers
import vigenere

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>
        <html class="crt">
            <head>
                <style>
                    * {{
                        background-color: #000000;
                        font: 20px monospace;
                        font-weight: bold;
                    }}
                    .crt::before {{
                      content: " ";
                      display: block;
                      position: fixed;
                      top: 0;
                      left: 0;
                      bottom: 0;
                      right: 0;
                      background: linear-gradient(rgba(20,20,20,0) 50%, rgba(0,0,0,0.25) 50%), linear-gradient(90deg, rgba(255,0,0,0.05), rgba(0,255,0,0.05), rgba(0,0,255,0.05));
                      background-repeat: repeat;
                      z-index: 2;
                      background-size: 500% 2px, 3px 500%;
                      pointer-events: none;
                    }}
                    form {{
                        padding: 20px;
                        margin: 0 auto;
                        width: 540px;
                        border-radius: 10px;
                        color: #35358f;
                    }}
                    select {{
                        color: #35358f;
                    }}
                    textarea {{
                        background-color: #35358f;
                        color: black;
                        margin: 10px 0;
                        width: 540px;
                        height: 120px;
                    }}
                    input {{
                        color: #35358f;
                        font: 20px;
                    }}
                </style>
            </head>
            <body>
              <form method="post">
                <select name="encrypt-type" onchange="this.form.submit()">
                    <option name="Caesar" {caesar}>Caesar</option>
                    <option name="Vigenere" {vigenere}>Vigenere</option>
                </select>
                {encryption}
                <br>
                <textarea name="text" rows="4" cols="20" placeholder="Message to Encrypt" required>{text}</textarea>
                <input background-color = "#055f05" color: "black" type="submit" value="Encrypt">
            </body>
        </html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    type = request.form['encrypt-type']
    message = request.form['text']

# handles Caesar or Vignere, handling also transition where the rot and key may not exist in transition.
    if type == "Caesar":
        try:
            rot = int(request.form['rot'])
        except KeyError:
            rot = 0
        secret = caesar.encrypt(message,rot)
        return form.format(caesar="selected",vigenere="",encryption="""<label for="rot">Rotate by:</label>
        <input type="number" name="rot" value="{}" step="1">""".format(rot),text=secret)

    if type == "Vigenere":
        try:
            key = str(request.form['key'])
            secret = vigenere.encrypt(message,key)
        except KeyError or TyeError:
            secret = message
            key = ""
        return form.format(caesar="",vigenere="selected",encryption="""<label for="rot">Encrypt Key:</label>
        <input type="text" pattern="[A-Za-z]+" name="key" placeholder="key" style="text-transform:uppercase" value="{0}">""".format(key),text=secret)


@app.route("/")
def index():
# Creates default form on Caesar
    return form.format(caesar="",vigenere="",encryption="""<label for="rot">Rotate by:</label>
    <input id="rot" type="number" name="rot" value="0" step="1">""",text="")

app.run()
