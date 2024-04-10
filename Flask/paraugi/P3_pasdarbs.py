from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def get_tekst():
    response = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=religious&format=txt&type=single")
    if response.status_code == 200:
        joks = response.text
        return render_template('p3.html', teksts=joks)
    else:
        return "Nevar saņemt joku"

if __name__ == '__main__':
    app.run(debug=True)