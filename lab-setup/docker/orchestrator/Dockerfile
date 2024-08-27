# Use an official Python runtime as a parent image
FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y \ 
    sshpass \
    openssh-client \
    telnet \
    iputils-ping \
    make

RUN pip install --no-cache-dir ansible

COPY ./lab-setup/ansible_id_rsa /home/root/.ssh/id_rsa
RUN chmod 600 /home/root/.ssh/id_rsa

RUN mkdir -p /ansible
RUN mkdir -p /ansible/aura

# Copy Ansible playbooks and inventory files into the container
COPY ./aura /ansible/aura
COPY ./lab-setup/scripts/orchestrator /ansible

ENV ANSIBLE_HOST_KEY_CHECKING=False

# Default command to run Ansible -- can be overridden when running the container
ENTRYPOINT ["tail", "-f", "/dev/null"]