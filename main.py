from flask import Flask
from CaloriesFormPage import CaloriesFormPage

app = Flask(__name__)

app.add_url_rule('/', view_func=CaloriesFormPage.as_view('index.html'))

app.run()