FROM satmandu/raspios:latest as base

COPY ./scripts/receive.py /usr/local/bin

RUN useradd -m ansible
RUN echo ansible:badusrpass | chpasswd

RUN echo "ansible ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers

USER ansible
RUN mkdir ~/.ssh
RUN chmod -R 700 ~/.ssh
COPY --chown=ansible:sudo ./ansible_id_rsa.pub /home/ansible/.ssh/id_rsa.pub
RUN cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
RUN chmod 644 ~/.ssh/id_rsa.pub
RUN chmod 644 ~/.ssh/authorized_keys
USER root

# Ensure the script is executable
RUN chmod +x /usr/local/bin/receive.py

# Create the init script for the service
RUN echo "#!/bin/sh\n\
### BEGIN INIT INFO\n\
# Provides:          aura_comms_receive\n\
# Required-Start:    \$remote_fs \$syslog\n\
# Required-Stop:     \$remote_fs \$syslog\n\
# Default-Start:     2 3 4 5\n\
# Default-Stop:      0 1 6\n\
# Short-Description: Start aura_comms_receive at boot time\n\
# Description:       Enable aura_comms_receive provided by daemon.\n\
### END INIT INFO\n\
\n\
case \"\$1\" in\n\
  start)\n\
    echo \"Starting aura_comms_receive\"\n\
    /usr/bin/python3 -u /usr/local/bin/receive.py &\n\
    ;;\n\
  stop)\n\
    echo \"Stopping aura_comms_receive\"\n\
    pkill -f /usr/local/bin/receive.py\n\
    ;;\n\
  restart)\n\
    echo \"Restarting aura_comms_receive\"\n\
    \$0 stop\n\
    \$0 start\n\
    ;;\n\
  *)\n\
    echo \"Usage: /etc/init.d/aura_comms_receive {start|stop|restart}\"\n\
    exit 1\n\
    ;;\n\
esac\n\
\n\
exit 0\n" > /etc/init.d/aura_comms_receive

# Make the init script executable
RUN chmod +x /etc/init.d/aura_comms_receive

EXPOSE 22

RUN cd /etc/ssh && ssh-keygen -A

CMD service ssh start && tail -f /dev/null

# Start the service when the container starts
# CMD service aura_comms_receive start && tail -f /dev/null