#!/bin/bash

sudo apt-get update
sudo apt-get -y install nano
sudo apt-get -y install cmake

echo "MaxiNet 1.2 installer"
echo ""
echo "This program installs MaxiNet 1.2 and all requirements to the home directory of your user"

if [ "$1" == "--help" ] || [ "$1" == "-h" ]
then
    echo ""
    echo "Invoke without any parameter to interactively install MaxiNet and its dependencies."
    echo "Use the -a parameter for complete and unguided installation."
    exit 0
fi


if [ "$1" == "-a" ]
then
    mininet="y"
    metis="y"
    pyro="y"
else
    containernet="y"
    if [ "$containernet" == "y" ] || [ "$containernet" == "Y" ]
    then
      containernet="y"
      echo ""
      echo "You choose to install container support. Warning: This will overwrite any existing Mininet installation."
    else
      containernet="n"
      echo ""

      mininet="y"

      if [ "$mininet" == "" ] || [ "$mininet" == "y" ] || [ "$mininet" == "Y" ]
      then
          mininet="y"
          echo ""
          echo "You choose to install Mininet. Warning: This will automatically remove existing directories ~/mininet, ~/loxigen, and ~/openflow"
      else
          mininet="n"
      fi
      echo ""
    fi

    metis="y"

    if [ "$metis" == "" ] || [ "$metis" == "y" ] || [ "$metis" == "Y" ]
    then
        metis="y"
    else
        metis="n"
    fi
    echo ""

    pyro="y"

    if [ "$pyro" == "" ] || [ "$pyro" == "y" ] || [ "$pyro" == "Y" ]
    then
        pyro="y"
    else
        pyro="n"
    fi
    echo ""


    echo "----------------"
    echo ""
    echo "MaxiNet installer will now install: "
    if [ "$mininet" == "y" ]; then echo " -Mininet 2.2.1rc1"; fi
    if [ "$containernet" == "y" ]; then echo " -Containernet 2.2.1"; fi
    if [ "$metis" == "y" ]; then echo " -Metis 5.1"; fi
    if [ "$pyro" == "y" ]; then echo " -Pyro 4"; fi
    echo " -MaxiNet 1.2"
    echo ""

fi

echo "installing required dependencies."

sudo apt-get -y install git autoconf screen cmake build-essential sysstat python-matplotlib uuid-runtime

if [ "$mininet" == "y" ]
then
  cd /containernet/
  sudo rm -rf openflow &> /dev/null
  sudo rm -rf loxigen &> /dev/null
  sudo rm -rf pox &> /dev/null
  sudo rm -rf oftest &> /dev/null
  sudo rm -rf oflops &> /dev/null
  sudo rm -rf ryu &> /dev/null
  sudo rm -rf mininet &> /dev/null

  git clone git://github.com/mininet/mininet
  cd mininet
  git checkout -b 2.2.1rc1 2.2.1rc1
  cd util/
  ./install.sh

  # the mininet installer sometimes crashes with a zipimport.ZipImportError.
  # In that case, we retry installation.
  if [ "$?" != "0" ]
  then
      ./install.sh
  fi
elif [ "$containernet" == "y" ]
then
  sudo apt-get -y install ansible aptitude
  # Patch config file if necessary
  grep "localhost ansible_connection=local" /etc/ansible/hosts >/dev/null
  if [ $? -ne 0 ]; then
    echo "localhost ansible_connection=local" | sudo tee -a /etc/ansible/hosts
  fi

  cd /containernet/
  sudo rm -rf containernet &> /dev/null
  sudo rm -rf oflops &> /dev/null
  sudo rm -rf oftest &> /dev/null
  sudo rm -rf openflow &> /dev/null
  sudo rm -rf pox &> /dev/null
  git clone https://github.com/containernet/containernet
  cd containernet/ansible
  sudo ansible-playbook install.yml
fi

if [ "$metis" == "y" ]
then
  cd /containernet/
  wget http://glaros.dtc.umn.edu/gkhome/fetch/sw/metis/metis-5.1.0.tar.gz
  tar -xzf metis-5.1.0.tar.gz
  rm metis-5.1.0.tar.gz
  cd metis-5.1.0
  make config
  make
  sudo make install
  cd /containernet/
  rm -rf metis-5.1.0
fi

if [ "$pyro" == "y" ]
then
  sudo apt-get -y install python-pip
  sudo pip install Pyro4
fi


cd /containernet/
sudo rm -rf MaxiNet &> /dev/null
git clone git://github.com/MaxiNet/MaxiNet.git
cd MaxiNet
git checkout v1.2
sudo make install
