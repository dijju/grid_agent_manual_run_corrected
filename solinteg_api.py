import requests
from config import SOLINTEG_API_URL

def get_grid_frequency():
    try:
        response = requests.get(SOLINTEG_API_URL)
        return float(response.json().get("fgrid", 0))
    except Exception as e:
        print("Error fetching fgrid:", e)
        return 0.0