import snap7

client = snap7.client.Client()
client.connect("192.168.10.61", 0, 1)

try:
    data = client.db_read(7, 0, 1)
    print("Read successful:", data)
except Exception as e:
    print("Error:", e)

client.disconnect()
