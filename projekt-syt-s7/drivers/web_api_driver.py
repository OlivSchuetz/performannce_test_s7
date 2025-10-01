# webapi_driver.py
import requests

PLC_IP = "192.168.0.1"   # <- IP eurer SPS
USERNAME = "admin"       # <- Zugangsdaten
PASSWORD = "admin"

def write_bool(var_name, value: bool):
    url = f"http://{PLC_IP}/api/values/{var_name}"
    payload = {"value": value}
    r = requests.put(url, auth=(USERNAME, PASSWORD), json=payload)
    return r.status_code, r.text

if __name__ == "__main__":
    status, resp = write_bool("DB1.DBX0.0", True)  # Beispiel-Adresse
    print("Status:", status, "Response:", resp)
