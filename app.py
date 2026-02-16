from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    hb = float(request.form.get('hemoglobin'))

    if hb < 7:
        prediction = "Severe"
        advice = [
            "Eat iron-rich foods like ragi, spinach, drumstick leaves",
            "Include dates and jaggery daily",
            "Consume eggs or liver if non-vegetarian",
            "Take iron supplements only under medical guidance"
        ]

    elif 7 <= hb < 11:
        prediction = "Moderate"
        advice = [
            "Include green leafy vegetables daily",
            "Eat dal, pulses, and groundnuts",
            "Consume beetroot and pomegranate",
            "Add citrus fruits for better iron absorption"
        ]

    else:
        prediction = "Low"
        advice = [
            "Maintain a balanced diet",
            "Include seasonal fruits and vegetables",
            "Continue iron-rich foods",
            "Avoid tea/coffee immediately after meals"
        ]

    return render_template(
        'index.html',
        prediction=prediction,
        advice=advice
    )

if __name__ == "__main__":
    app.run()



