from flask import Flask, render_template
from Data.meteo import meteo

app = Flask(__name__)


@app.route('/')
def index():
    forecasts = meteo['forecast']
    return render_template('weather.html', forecasts=forecasts)

@app.route('/api/meteo/<int:day>')
def meteo_par_jour(day):
    if 0 <= day < len(meteo['forecast']):
        return render_template('weather.html', forecast=meteo['forecast'][day])
    else:
        return "Jour invalide"
if __name__ == '__main__':
    app.run(debug=True)