import requests

def get_generation_and_consumption(inverter_url, meter_url):
    try:
        inverter_data = requests.get(inverter_url).json()
        meter_data = requests.get(meter_url).json()
        generation = inverter_data.get("kWh", 0)
        consumption = meter_data.get("kWh", 0)
        return generation, consumption
    except Exception as e:
        print("Error calling MCP APIs:", e)
        return 0, 0

def send_curtailment_request(curtail_url, reason):
    print(f"🔌 Curtailment: Sending curtailment request to {curtail_url}")
    print(f"📝 Reason: {reason}")
    requests.post(curtail_url, json={"action": "shut_down", "reason": reason})

def send_battery_charge_request(battery_url, power, reason):
    print(f"🔋 Battery: Sending charge request to {battery_url}")
    print(f"💡 Power to absorb: {power} kWh")
    print(f"📝 Reason: {reason}")
    requests.post(battery_url, json={"action": "charge", "amount": power, "reason": reason})