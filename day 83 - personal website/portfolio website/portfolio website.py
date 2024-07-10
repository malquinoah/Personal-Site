from flask import Flask, render_template, redirect, url_for,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Email, DataRequired
from flask_ckeditor import CKEditor, CKEditorField
from flask_bootstrap import Bootstrap5
import os
import smtplib

app = Flask(__name__)
ckeditor = CKEditor(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
bootstrap = Bootstrap5(app)


class Contact(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[Email(message='That\'s not a valid email address.'), DataRequired(message='Input is required')])
    body = CKEditorField('Body', validators=[DataRequired(message='Input is required')])
    submit = SubmitField('Submit')


@app.route("/", methods=['POST', 'GET'])
def home():
    form = Contact()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        body = form.body.data
        with smtplib.SMTP('smtp.gmail.com', port=587) as server:
            server.starttls()  # Secure the connection
            server.login(user='pythontestcode3@gmail.com', password='vkmktavxlzhsrotj')
            server.sendmail(from_addr='pythontestcode3@gmail.com',
                            to_addrs='malquinoah@icloud.com', msg=f'Subject: Portfolio Contact\n\nfrom:{name}\n{email}\nmessage:{body}')
            flash('Email sent!')

    return render_template('index.html', form=form)


@app.route('/linkedin')
def linkedin():
    return redirect("http://www.linkedin.com/in/noah-malqui-b87b082a8")














if __name__ == '__main__':
    app.run(debug=True, port=5001)

