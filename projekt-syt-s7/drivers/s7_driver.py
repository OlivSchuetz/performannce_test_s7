import snap7
from snap7.util import set_bool, get_bool

PLC_IP = "192.168.106.61"

def write_bool(db, byte_index, bit_index, value):
    client = snap7.client.Client()
    client.connect(PLC_IP, 0, 1)

    # Read the byte
    data = bytearray(client.db_read(db, byte_index, 1))
    
    # Modify the bit
    set_bool(data, 0, bit_index, value)
    
    # Write back
    client.db_write(db, byte_index, data)
    client.disconnect()

if __name__ == "__main__":
    write_bool(1, 0, 0, True)
    print("Done")


# S7 ENDPOINT URL OPC.tcp://192.168.10.62:4840
