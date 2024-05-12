class Calorie:

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.temperature = temperature

    def calculate(self):
        cal = 10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10
        return cal
