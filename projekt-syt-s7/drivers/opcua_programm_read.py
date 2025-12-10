from opcua import Client
import time
 
client = Client("opc.tcp://192.168.106.62:4840")
client.connect()
 
start = time.time()
 
buffer = []
for i in range(0, 133):  # gültiger Bereich
    node = client.get_node(f'ns=3;s="PerformaceDataS7"."BulkData"[{i}]')
    buffer.append(node.get_value())
 
end = time.time()
 
print("Read completed in", end - start, "seconds")
 
client.disconnect()