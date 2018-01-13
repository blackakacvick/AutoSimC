from flask import Flask,render_template, flash, Response
from flask_bootstrap import Bootstrap
from gui.forms import mainForm
from markupsafe import escape


app = Flask(__name__)
Bootstrap(app)
app.secret_key = "CHANGE IT, IF USING IT IN PRODUCTION"
app.config["WTF_CSRF_ENABLED"] = False # You do not really need security on localhost do you? ;)

@app.route('/', methods=('GET', 'POST'))
def index():
    form = mainForm.SimPermutForm()

    if form.validate_on_submit():
        #TODO: Better checking and stuff use validators!
        with open("input.txt","w") as f:
            f.write(form.simPermutText.data)
    return render_template('index.html',form=form)


@app.route("/js/<filename>")
def js(filename):
    with open("gui/templates/js/"+ filename +".js") as f:
        return f.read(), 200 , {'Content-Type': 'application/javascript; charset=utf-8'}