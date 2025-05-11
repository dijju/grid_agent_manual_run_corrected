SOLINTEG_API_URL = "http://localhost:7000/fgrid"
SOLAR_AGENTS = {
    "SA1": {
        "inverter_url": "http://localhost:5001/inverter",
        "meter_url": "http://localhost:5001/meter",
        "curtail_url": "http://localhost:5001/curtail"
    },
    "SA2": {
        "inverter_url": "http://localhost:5002/inverter",
        "meter_url": "http://localhost:5002/meter",
        "curtail_url": "http://localhost:5002/curtail"
    }
}
BATTERY_AGENT_URL = "http://localhost:6001/charge"
FGRID_THRESHOLD = 50.0