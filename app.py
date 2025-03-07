from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(api_key, location):
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {"key": api_key, "q": location}
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch data, status code: {response.status_code}"}

@app.route("/", methods=["POST", "GET"])
def home():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city", "")
        API_KEY = "faa13149546b485297c50214250703"  
        weather_data = get_weather(API_KEY, city)
    
    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
