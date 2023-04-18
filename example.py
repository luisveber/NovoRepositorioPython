from email import message
import fins.udp
import time

fins_instance = fins.udp.UDPFinsConnection()
fins_instance.connect('192.168.0.50')
fins_instance.dest_node_add=1
fins_instance.srce_node_add=25

#for i in range(1):

#fins_instance.memory_area_write(fins.FinsPLCMemoryAreas().WORK_BIT,b'\x00\x50\x00',b'\x01',1)
#mem_area = fins_instance.memory_area_read(fins.FinsPLCMemoryAreas().WORK_BIT,b'\x00\x50\x00')
fins_instance.memory_area_write(fins.FinsPLCMemoryAreas().WORK_BIT,b'\x00\x17\x00',b'\x01',1)
mem_area = fins_instance.memory_area_read(fins.FinsPLCMemoryAreas().WORK_BIT,b'\x00\x17\x00')
print(mem_area)
    
