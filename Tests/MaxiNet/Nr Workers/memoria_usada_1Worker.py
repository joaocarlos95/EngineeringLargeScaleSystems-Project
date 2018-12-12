#!/usr/bin/python2

#
# Minimal example showing how to use MaxiNet
#

import time

from MaxiNet.Frontend import maxinet
from MaxiNet.tools import FatTree
from mininet.node import OVSSwitch

topo = FatTree(30, 10, 0.1)
cluster = maxinet.Cluster(minWorkers=1, maxWorkers=1)

exp = maxinet.Experiment(cluster, topo, switch=OVSSwitch)
exp.setup()

print exp.get_node("h1").cmd("ifconfig")  # call mininet cmd function of h1
print exp.get_node("h30").cmd("ifconfig")

print "waiting 5 seconds for routing algorithms on the controller to converge"
time.sleep(5)

print exp.get_node("h30").cmd("ping -c 100 10.0.0.1")


exp.stop()
