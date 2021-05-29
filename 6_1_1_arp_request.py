import os

from scapy.all import *

# 配置各种信息，以便调用
from scapy.layers.l2 import Ether, ARP

local_mac = 'C8:09:A8:89:53:CD'
local_ip = '192.168.5.107'
dest_ip = '192.168.5.113'
# if_name = 'eno33554944'

# 源MAC为本地MAC-----目的MAC为广播----操作码为1（请求）
result_raw = srp(
    Ether(src=local_mac, dst='FF:FF:FF:FF:FF:FF') / ARP(op=1, hwsrc=local_mac, hwdst='00:00:00:00:00:00', psrc=local_ip,
                                                        pdst=dest_ip), timeout=1, verbose=False)
result_list = result_raw[0].res  # res: the list of packets，产生由收发数据包所组成的清单（list）
# print(result_list[0][1].getlayer(ARP).fields['psrc'])
# print(result_list[0][1].getlayer(ARP).fields['hwsrc'])
print('IP地址: ' + result_list[0][1].getlayer(ARP).fields['psrc'] + ' MAC地址: ' + result_list[0][1].getlayer(ARP).fields[
    'hwsrc'])
