install:
	ansible-galaxy install -r requirements.yml --force

sample: install
	ansible-playbook playbooks/sample-test-case.yml

test-case-1: install
	ansible-playbook playbooks/test-case-1.yml

.PHONY: build-lab-network build-lab start-lab stop-lab

build-lab-network:
	docker network create --subnet 10.250.0.0/20 aura_comms 

build-lab:
	docker-compose -f docker-compose.yml build

start-lab: build-lab
	docker-compose -f docker-compose.yml up -d

stop-lab:
	@docker ps -q --filter "name=aura-lab" | xargs -r docker kill
	@docker ps -a -q --filter "name=aura-lab" | xargs -r docker rm