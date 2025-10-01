# webapi_driver.py
import requests
import json
import urllib3

# Warnungen für selbstsignierte Zertifikate deaktivieren
urllib3.disable_warnings()

PLC_IP = "192.168.10.61"
USERNAME = "5AHIT"
PASSWORD = "5ahiT"
BASE_URL = f"https://{PLC_IP}/api/jsonrpc"

class WebApiDriver:
    def __init__(self):
        self.token = None
        self.login()

    def login(self):
        payload = [
            {
                "id": 0,
                "jsonrpc": "2.0",
                "method": "Api.Login",
                "params": {"user": USERNAME, "password": PASSWORD}
            }
        ]
        headers = {'Content-Type': 'application/json'}
        response = requests.post(BASE_URL, data=json.dumps(payload), headers=headers, verify=False)
        response.raise_for_status()
        self.token = response.json()[0]['result']['token']
        print("✅ Login erfolgreich, Token erhalten.")

    def _post(self, payload):
        if not self.token:
            raise Exception("Nicht eingeloggt. Token fehlt.")
        headers = {'X-Auth-Token': self.token, 'Content-Type': 'application/json'}
        response = requests.post(BASE_URL, data=json.dumps(payload), headers=headers, verify=False)
        response.raise_for_status()
        return response.json()

    def write_bool(self, var_name, value: bool):
        payload = [
            {
                "id": 1,
                "jsonrpc": "2.0",
                "method": "PlcProgram.Write",
                "params": {"var": var_name, "value": value}
            }
        ]
        return self._post(payload)

    def read(self, var_name):
        payload = [
            {
                "id": 2,
                "jsonrpc": "2.0",
                "method": "PlcProgram.Read",
                "params": {"var": var_name}
            }
        ]
        return self._post(payload)

    def logout(self):
        payload = [
            {
                "id": 0,
                "jsonrpc": "2.0",
                "method": "Api.Logout"
            }
        ]
        result = self._post(payload)
        self.token = None
        print("✅ Logout erfolgreich.")
        return result

# ===========================
# Beispiel für Nutzung
# ===========================
if __name__ == "__main__":
    driver = WebApiDriver()

    # Beispiel: Bit schreiben
    print(driver.write_bool('PerformanceData.ToServer', True))

    # Beispiel: Bit lesen
    print(driver.read('PerformanceData.FromServer'))

    # Logout
    driver.logout()
