# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  # VM
  config.vm.box = "guillaumesadler/ubuntu-server-20.04"
  config.vm.box_version = "1"

  # Network
  config.vm.network "private_network", ip: "192.168.33.12"

  # Parameters
  config.vm.provider "virtualbox" do |v|
    v.memory = 8000
    v.cpus = 8
  end

  config.vm.provision :shell, path: "./provisioning/docker-compose.sh"

  # Provision
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provisioning/ansible/playbook.yml"
  end  

  #Sync Folders 
  config.vm.synced_folder '.', '/vagrant', disabled: true 
  config.vm.synced_folder './jenkins', '/workdir'

end