from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)
OPENSKY_URL = "https://opensky-network.org/api/states/all"

@app.route("/flights")
def flights():
    resp = requests.get(OPENSKY_URL, timeout=5)
    data = resp.json()
    flights = []
    for s in data.get("states", []):
        lon, lat = s[5], s[6]
        if lon is None or lat is None:
            continue
        flights.append({
            "icao24":   s[0],
            "callsign": s[1].strip() if s[1] else "",
            "lat":      lat,
            "lon":      lon,
            "alt":      s[7],
            "vel":      s[9],
            "hdg":      s[10]
        })
    return jsonify(time=data["time"], flights=flights)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # debug=True for auto‑reload; host=0.0.0.0 so other devices on your LAN can view it
    app.run(debug=True, host="0.0.0.0", port=5000)
