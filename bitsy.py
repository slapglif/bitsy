from flask import Flask, render_template, request, flash, redirect, url_for
from forms import ContactForm
from mandril import drill

app = Flask(__name__)

app.secret_key = 'super secret key'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('You must enter something into all of the fields')
            return render_template('index.html',form=form)
        else:
            sub = form.subject.data
            email = form.email.data
            message = form.message.data
            drill(sub,message,email)
            return render_template('index.html', success=True)
    elif request.method == 'GET':
        return render_template('index.html',form=form)


if __name__ == '__main__':
    app.run(debug=True,threaded=True)
