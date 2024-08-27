install:
	ansible-galaxy install -r requirements.yml --force

transmit-data: install
	ansible-playbook -i inventory/lab.yaml playbooks/transmit-data.yml