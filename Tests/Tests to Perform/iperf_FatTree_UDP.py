#!/usr/bin/python2

import time

from MaxiNet.Frontend import maxinet
from MaxiNet.tools import FatTree
from mininet.node import OVSSwitch

topo = FatTree(4, 10, 0.1)
cluster = maxinet.Cluster()

exp = maxinet.Experiment(cluster, topo, switch=OVSSwitch)
exp.setup()

print exp.get_node("h1").cmd("ifconfig")  # call mininet cmd function of h1
print exp.get_node("h4").cmd("ifconfig")

print "waiting 5 seconds for routing algorithms on the controller to converge"
time.sleep(5)

print exp.get_node("h4").cmd("iperf -s & -u")
print exp.get_node("h1").cmd("iperf -c 10.0.0.4 -u")

exp.stop()