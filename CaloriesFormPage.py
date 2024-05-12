from flask.views import MethodView
from flask import render_template, request

from Calorie import Calorie
from CaloriesForm import CaloriesForm
from Temperature import Temperature


class CaloriesFormPage(MethodView):

    def get(self):
        calories_form = CaloriesForm()
        return render_template('index.html', caloriesForm=calories_form, showResult=False)

    def post(self):
        calories_form = CaloriesForm(request.form)
        height = float(calories_form.height.data)
        weight = float(calories_form.weight.data)
        age = float(calories_form.age.data)
        city = str(calories_form.city.data)
        country = str(calories_form.country.data)

        temperature = Temperature(country=country, city=city)
        calories = Calorie(height=height, weight=weight, age=age, temperature=temperature.get())

        return render_template('index.html', caloriesForm=calories_form,
                               calories=calories.calculate(), temperature=temperature.get(), showResult=True)


