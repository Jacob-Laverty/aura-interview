# Multicast receiver
# Guidance:  https://stackoverflow.com/a/1794373
import socket
import struct
import os
from datetime import datetime

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 8162
LOG_DIR = "/lab"

if not os.path.exists(LOG_DIR):
  raise Error('No log dir present, exiting')

LOG_FILE_PATH = os.path.join(LOG_DIR, datetime.now().strftime('%d_%m_%Y-received.log'))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((MCAST_GRP, MCAST_PORT))
mreq = struct.pack('4sl', socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

with open(LOG_FILE_PATH, 'w+') as log_file:
  while True:
    data, __addr = sock.recvfrom(1024)

    audit_log = f"{datetime.now().isoformat()} - Multicast received\n"
    data_log = f"{data.decode('utf-8')}\n"

    log_file.write(audit_log)
    log_file.write(data_log)
    
    log_file.flush()