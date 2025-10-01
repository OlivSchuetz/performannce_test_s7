import snap7
from snap7.util import set_bool

PLC_IP = "192.168.0.1"   

def write_bool(db_number, start_byte, bit_index, value: bool):
    client = snap7.client.Client()
    client.connect(PLC_IP, 0, 1)  
    
    data = client.db_read(db_number, start_byte, 1)
    set_bool(data, 0, bit_index, value)
    client.db_write(db_number, start_byte, data)
    client.disconnect()

if __name__ == "__main__":
    write_bool(1, 0, 0, True)  
    print("Done")
