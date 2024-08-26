# Use an official Python runtime as a parent image
FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y \ 
    sshpass \
    openssh-client \
    telnet \
    iputils-ping

RUN pip install --no-cache-dir ansible

COPY ./ansible_id_rsa /home/root/.ssh/id_rsa
RUN chmod 600 /home/root/.ssh/id_rsa

RUN mkdir -p /ansible

# Copy Ansible playbooks and inventory files into the container
COPY ./scripts/orchestrator /ansible

ENV ANSIBLE_HOST_KEY_CHECKING=False

# Default command to run Ansible -- can be overridden when running the container
ENTRYPOINT ["tail", "-f", "/dev/null"]