# Calorie Calculator Web App

Welcome to the Calorie Calculator Web App! This Flask application takes weight, height, age, city, and country as inputs and calculates the amount of calories you need to consume today depending upon the temperature of your city.

## Features

1. **Input Form:** Enter your weight, height, age, city, and country into the provided form.
2. **Weather Integration:** The application retrieves the current temperature of your city to adjust the recommended calorie intake accordingly.
3. **Response Page:** After submitting your information, you'll receive a response showing the calculated calorie intake for the day.

## Usage

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/kamalharsh14/Calorie-Calculator.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```bash
    python main.py
    ```

4. Open your web browser and navigate to `http://localhost:5000` to access the application.

5. Fill out the input form with your weight, height, age, city, and country.

6. Submit the form and view the response page to see your recommended calorie intake for the day.

## Dependencies

- Flask: A micro web framework for Python.
- Requests: HTTP library for making API requests.

## Directory Structure
- Calories App
- ├── templates/
- │ ├── index.html
- ├── Calorie.py
- ├── CaloriesForm.py
- ├── CaloriesFormPage.py
- ├── Temperature.py
- ├── temperature.yaml
- ├── main.py
- ├── README.md
- └── requirements.txt


## Author

- Harsh kamal Singh
- GitHub: [kamalharsh14](https://github.com/kamalharsh14)