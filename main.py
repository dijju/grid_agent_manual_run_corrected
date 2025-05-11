from config import SOLAR_AGENTS, BATTERY_AGENT_URL, FGRID_THRESHOLD
from solinteg_api import get_grid_frequency
from mcp_client import get_generation_and_consumption, send_curtailment_request, send_battery_charge_request

def main():
    print("🔍 Starting Grid Agent Monitoring...")

    fgrid = get_grid_frequency()
    print(f"📡 Current Grid Frequency: {fgrid} Hz")

    total_excess = 0
    excess_map = {}

    for agent_id, urls in SOLAR_AGENTS.items():
        gen, cons = get_generation_and_consumption(urls["inverter_url"], urls["meter_url"])
        excess = gen - cons
        total_excess += excess
        excess_map[agent_id] = excess
        print(f"📊 {agent_id}: Generation={gen} kWh, Consumption={cons} kWh, Excess={excess} kWh")

    print(f"⚡ Total Excess Generation: {total_excess} kWh")

    if fgrid > FGRID_THRESHOLD:
        print("🚨 ALERT: Grid frequency exceeds safe threshold!")
        reason = f"Grid frequency high ({fgrid} Hz). Mitigating overgeneration."

        # Curtail highest excess solar agent
        sorted_agents = sorted(excess_map.items(), key=lambda x: -x[1])
        for agent_id, excess in sorted_agents:
            if excess > 0:
                send_curtailment_request(SOLAR_AGENTS[agent_id]["curtail_url"], reason)
                break

        # Ask battery to absorb remaining excess
        send_battery_charge_request(BATTERY_AGENT_URL, total_excess, reason)

    else:
        print("✅ Grid frequency is within safe limits. No action needed.")

if __name__ == "__main__":
    main()