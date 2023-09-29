from flask import Flask, render_template

app = Flask(__name__)

meteo = {
     "city": {
        "insee": "35238",
        "cp": 35000,
        "name": "Rennes",
        "latitude": 48.112,
        "longitude": -1.6819,
        "altitude": 38
    },
    "update": "2020-10-29T12:40:08+0100",
    "forecast": [
        {
            "insee": "35238",
            "cp": 35000,
            "latitude": 48.112,
            "longitude": -1.6819,
            "day": 0,
            "datetime": "2020-10-29T01:00:00+0100",
            "wind10m": 15,
            "gust10m": 49,
            "dirwind10m": 230,
            "rr10": 0.2,
            "rr1": 0.3,
            "probarain": 40,
            "weather": 4,
            "tmin": 11,
            "tmax": 17,
            "sun_hours": 1,
            "etp": 1,
            "probafrost": 0,
            "probafog": 0,
            "probawind70": 0,
            "probawind100": 0,
            "gustx": 49
        },
        {
            "insee": "35238",
            "cp": 35000,
            "latitude": 48.112,
            "longitude": -1.6819,
            "day": 1,
            "datetime": "2020-10-30T01:00:00+0100",
            "wind10m": 15,
            "gust10m": 43,
            "dirwind10m": 215,
            "rr10": 0,
            "rr1": 0,
            "probarain": 20,
            "weather": 3,
            "tmin": 11,
            "tmax": 17,
            "sun_hours": 3,
            "etp": 1,
            "probafrost": 0,
            "probafog": 0,
            "probawind70": 0,
            "probawind100": 0,
            "gustx": 43
        },
        {
            "insee": "35238",
            "cp": 35000,
            "latitude": 48.112,
            "longitude": -1.6819,
            "day": 2,
            "datetime": "2020-10-31T01:00:00+0100",
            "wind10m": 20,
            "gust10m": 35,
            "dirwind10m": 203,
            "rr10": 1.9,
            "rr1": 2.5,
            "probarain": 70,
            "weather": 40,
            "tmin": 10,
            "tmax": 17,
            "sun_hours": 2,
            "etp": 0,
            "probafrost": 0,
            "probafog": 0,
            "probawind70": 10,
            "probawind100": 0,
            "gustx": 43
        },
        {
            "insee": "35238",
            "cp": 35000,
            "latitude": 48.112,
            "longitude": -1.6819,
            "day": 3,
            "datetime": "2020-11-01T01:00:00+0100",
            "wind10m": 30,
            "gust10m": 41,
            "dirwind10m": 210,
            "rr10": 15.5,
            "rr1": 21,
            "probarain": 90,
            "weather": 11,
            "tmin": 15,
            "tmax": 18,
            "sun_hours": 0,
            "etp": 1,
            "probafrost": 0,
            "probafog": 0,
            "probawind70": 20,
            "probawind100": 0,
            "gustx": 61
        },
        {
            "insee": "35238",
            "cp": 35000,
            "latitude": 48.112,
            "longitude": -1.6819,
            "day": 4,
            "datetime": "2020-11-02T01:00:00+0100",
            "wind10m": 30,
            "gust10m": 56,
            "dirwind10m": 207,
            "rr10": 10.2,
            "rr1": 27,
            "probarain": 80,
            "weather": 211,
            "tmin": 9,
            "tmax": 18,
            "sun_hours": 0,
            "etp": 1,
            "probafrost": 0,
            "probafog": 0,
            "probawind70": 30,
            "probawind100": 0,
            "gustx": 86
        },
        {
            "insee": "35238",
            "cp": 35000,
            "latitude": 48.112,
            "longitude": -1.6819,
            "day": 5,
            "datetime": "2020-11-03T01:00:00+0100",
            "wind10m": 15,
            "gust10m": 30,
            "dirwind10m": 216,
            "rr10": 2.8,
            "rr1": 12.2,
            "probarain": 60,
            "weather": 41,
            "tmin": 6,
            "tmax": 14,
            "sun_hours": 6,
            "etp": 1,
            "probafrost": 10,
            "probafog": 0,
            "probawind70": 0,
            "probawind100": 0,
            "gustx": 45
        },
        {
            "insee": "35238",
            "cp": 35000,
            "latitude": 48.112,
            "longitude": -1.6819,
            "day": 6,
            "datetime": "2020-11-04T01:00:00+0100",
            "wind10m": 15,
            "gust10m": 26,
            "dirwind10m": 49,
            "rr10": 0.4,
            "rr1": 2.2,
            "probarain": 60,
            "weather": 40,
            "tmin": 5,
            "tmax": 13,
            "sun_hours": 6,
            "etp": 1,
            "probafrost": 10,
            "probafog": 10,
            "probawind70": 0,
            "probawind100": 0,
            "gustx": 36
        },
        {
            "insee": "35238",
            "cp": 35000,
            "latitude": 48.112,
            "longitude": -1.6819,
            "day": 7,
            "datetime": "2020-11-05T01:00:00+0100",
            "wind10m": 20,
            "gust10m": 32,
            "dirwind10m": 71,
            "rr10": 0,
            "rr1": 0,
            "probarain": 20,
            "weather": 3,
            "tmin": 5,
            "tmax": 14,
            "sun_hours": 5,
            "etp": 1,
            "probafrost": 10,
            "probafog": 0,
            "probawind70": 10,
            "probawind100": 0,
            "gustx": 32
        },
        {
            "insee": "35238",
            "cp": 35000,
            "latitude": 48.112,
            "longitude": -1.6819,
            "day": 8,
            "datetime": "2020-11-06T01:00:00+0100",
            "wind10m": 15,
            "gust10m": 30,
            "dirwind10m": 88,
            "rr10": 0,
            "rr1": 0,
            "probarain": 40,
            "weather": 3,
            "tmin": 7,
            "tmax": 17,
            "sun_hours": 5,
            "etp": 1,
            "probafrost": 10,
            "probafog": 0,
            "probawind70": 0,
            "probawind100": 0,
            "gustx": 30
        },
        {
            "insee": "35238",
            "cp": 35000,
            "latitude": 48.112,
            "longitude": -1.6819,
            "day": 9,
            "datetime": "2020-11-07T01:00:00+0100",
            "wind10m": 15,
            "gust10m": 27,
            "dirwind10m": 92,
            "rr10": 2.4,
            "rr1": 5.2,
            "probarain": 60,
            "weather": 41,
            "tmin": 8,
            "tmax": 17,
            "sun_hours": 4,
            "etp": 1,
            "probafrost": 0,
            "probafog": 0,
            "probawind70": 0,
            "probawind100": 0,
            "gustx": 38
        },
        {
            "insee": "35238",
            "cp": 35000,
            "latitude": 48.112,
            "longitude": -1.6819,
            "day": 10,
            "datetime": "2020-11-08T01:00:00+0100",
            "wind10m": 15,
            "gust10m": 24,
            "dirwind10m": 110,
            "rr10": 6.4,
            "rr1": 8.4,
            "probarain": 60,
            "weather": 40,
            "tmin": 8,
            "tmax": 16,
            "sun_hours": 3,
            "etp": 1,
            "probafrost": 0,
            "probafog": 0,
            "probawind70": 0,
            "probawind100": 0,
            "gustx": 35
        },
        {
            "insee": "35238",
            "cp": 35000,
            "latitude": 48.112,
            "longitude": -1.6819,
            "day": 11,
            "datetime": "2020-11-09T01:00:00+0100",
            "wind10m": 15,
            "gust10m": 22,
            "dirwind10m": 140,
            "rr10": 1.6,
            "rr1": 7,
            "probarain": 60,
            "weather": 41,
            "tmin": 7,
            "tmax": 15,
            "sun_hours": 3,
            "etp": 1,
            "probafrost": 0,
            "probafog": 0,
            "probawind70": 0,
            "probawind100": 0,
            "gustx": 37
        },
        {
            "insee": "35238",
            "cp": 35000,
            "latitude": 48.112,
            "longitude": -1.6819,
            "day": 12,
            "datetime": "2020-11-10T01:00:00+0100",
            "wind10m": 10,
            "gust10m": 21,
            "dirwind10m": 153,
            "rr10": 2.2,
            "rr1": 6.5,
            "probarain": 60,
            "weather": 41,
            "tmin": 6,
            "tmax": 15,
            "sun_hours": 4,
            "etp": 1,
            "probafrost": 10,
            "probafog": 30,
            "probawind70": 0,
            "probawind100": 0,
            "gustx": 31
        },
        {
            "insee": "35238",
            "cp": 35000,
            "latitude": 48.112,
            "longitude": -1.6819,
            "day": 13,
            "datetime": "2020-11-11T01:00:00+0100",
            "wind10m": 15,
            "gust10m": 21,
            "dirwind10m": 201,
            "rr10": 3.5,
            "rr1": 10,
            "probarain": 60,
            "weather": 41,
            "tmin": 6,
            "tmax": 15,
            "sun_hours": 4,
            "etp": 1,
            "probafrost": 10,
            "probafog": 0,
            "probawind70": 10,
            "probawind100": 0,
            "gustx": 31
        }
    ]
}
@app.route('/')
def index():
    forecasts = meteo['forecast']
    return render_template('weather.html', forecasts=forecasts)

@app.route('/day/<int:day>')
def weather_by_day(day):
    if 0 <= day < len(meteo['forecast']):
        return render_template('weather.html', forecast=meteo['forecast'][day])
    else:
        return "Jour invalide"
if __name__ == '__main__':
    app.run(debug=True)