install:
	ansible-galaxy install -r requirements.yml --force

sample: install
	ansible-playbook playbooks/sample-test-case.yml

test-case-1: install
	ansible-playbook playbooks/test-case-1.yml

.PHONY: gen-aura-lab-keys build-lab-network build-lab start-lab stop-lab

gen-aura-lab-keys:
ifeq (,$(wildcard ./lab-setup/ansible_id_rsa))
	ssh-keygen -b 2048 -t rsa -C "ansible@email.com" -f "./lab-setup/ansible_id_rsa" -N ""
	chmod 600 "./lab-setup/ansible_id_rsa"
	chmod 644 "./lab-setup/ansible_id_rsa.pub"
endif

build-lab: gen-aura-lab-keys
	docker-compose -f docker-compose.yml build

start-lab: build-lab
	docker-compose -f docker-compose.yml up -d

stop-lab:
	@docker ps -q --filter "name=aura-lab" | xargs -r docker kill
	@docker ps -a -q --filter "name=aura-lab" | xargs -r docker rm
	@docker network rm aura-lab_aura_comms