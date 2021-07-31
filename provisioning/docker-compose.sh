#!/usr/bin/env bash

sudo apt-get update

sudo apt-get install -y  apt-transport-https ca-certificates curl gnupg2 software-properties-common vim
		    	
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
				
sudo apt-key fingerprint 0EBFCD88

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
					    
sudo apt-get update

sudo apt-get install -y docker-ce docker-ce-cli containerd.io

sudo usermod --groups docker --append vagrant

sudo echo vm.max_map_count=262144 > /etc/sysctl.d/vm_max_map_count.conf

sudo sysctl --system

sudo grep -qF 'vagrant - nofile 65536' /etc/security/limits.conf || sudo echo 'vagrant - nofile 65536' >> /etc/security/limits.conf

sudo curl -L "https://github.com/docker/compose/releases/download/1.28.6/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

# JENKINS
# Java install
sudo apt -y update

sudo apt -y install openjdk-11-jdk

wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -

sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > \
    /etc/apt/sources.list.d/jenkins.list'

sudo apt-get -y update

sudo apt-get -y install jenkins

sudo systemctl daemon-reload

sudo systemctl start jenkins
