from flask import Flask, render_template, request, jsonify
from weather import generate_weather_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    if not city:
        return jsonify({'error': 'Please enter a city name'}), 400
    
    weather_data = generate_weather_data(city)
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True) 