from opcua import Client, ua
import time

client = Client("opc.tcp://192.168.106.62:4840")
client.connect()

node = client.get_node('ns=3;s="PerformaceDataS7"."ToServer"."bool00"')

start = time.time()

for i in range(1000):
    val = (i % 2 == 0)
    node.set_value(ua.DataValue(ua.Variant(val, ua.VariantType.Boolean)))

end = time.time()
print("Bool write 1000x:", end - start, "seconds")

client.disconnect()

