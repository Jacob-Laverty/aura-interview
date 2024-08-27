# Guidance:  https://stackoverflow.com/a/1794373
import socket
import time
import random
import os

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 8162
MESSAGE = b'Hello, Multicast!'
START_TIME = time.time()
DURATION = 10
END_TIME = START_TIME + DURATION
LOG_DIR = '/lab'
LOCK_FILE_PATH = os.path.join(LOG_DIR, 'transmit.lock')

# regarding socket.IP_MULTICAST_TTL
# ---------------------------------
# for all packets sent, after two hops on the network the packet will not
# be re-sent/broadcast (see https://www.tldp.org/HOWTO/Multicast-HOWTO-6.html)
MULTICAST_TTL = 2


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, MULTICAST_TTL)

try:
  with open(LOCK_FILE_PATH, 'w') as lock_file:
    lock_file.write("Transmitting")
  while time.time() < END_TIME:
    # Get current timestamp of message
    message_timestamp_milli = int(time.time() * 1000)
    # Mock some data
    mock_bytes = random.randint(10,50)

    # Simulate network latency, sleep for number of milliseconds equal to the mock bytes
    # usually between 20-80ms
    time.sleep(mock_bytes / 1000)

    sock.sendto(MESSAGE, (MCAST_GRP, MCAST_PORT))
finally:
    if os.path.exists(LOCK_FILE_PATH):
      os.remove(LOCK_FILE_PATH)