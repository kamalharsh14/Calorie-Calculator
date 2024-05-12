from wtforms import Form, StringField, SubmitField


class CaloriesForm(Form):
    weight = StringField("Weight: ")
    height = StringField("Height: ")
    age = StringField("Age: ")
    country = StringField("Country: ")
    city = StringField("City: ")
    button = SubmitField("Calculate")
