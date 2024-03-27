from flask import Flask

app = Flask(__name__)

#/ nozīmē sākums
@app.route("/")
def hello_world():
    return "Sveika, Pasaule!"

@app.route("/user/<name>")
def hello_user(name):
    return "Sveiki " + str(name) + "!"

@app.route("/admin")
def hello_admin():
    return "Sveiki, ADMINISTRATOR!"

@app.errorhandler(404)
def page_not_found(error):
    return "Lapa netika atrasta"

app.run()

#press ctrl + click on the link to see result of the code 

#to see the user output type /user into the end of the first link when the page opens

#to see user name write /user/(name you want to see)