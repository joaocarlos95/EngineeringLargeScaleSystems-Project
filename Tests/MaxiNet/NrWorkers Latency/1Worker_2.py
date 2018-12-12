#!/usr/bin/python2

#
# This example shows how to dynamically add hosts and switches to a
# running emulation.
# Due to technical limitations it is NOT possible to create a link
# between a switch and a host if these are emulated at DIFFERENT workers
# This limitation does (of course) NOT hold for links between switches.
#
# Dynamic adding and removing of nodes also does not work when using the
# UserSwitch.


import time

from mininet.topo import Topo
from mininet.node import OVSSwitch

from MaxiNet.Frontend import maxinet
from MaxiNet.tools import Tools


# create topology

cluster = maxinet.Cluster(minWorkers=1, maxWorkers=1)

topo = Topo()
topo.addHost("h1", ip=Tools.makeIP(1), mac=Tools.makeMAC(1))
topo.addHost("h2", ip=Tools.makeIP(2), mac=Tools.makeMAC(2))
topo.addHost("h3", ip=Tools.makeIP(3), mac=Tools.makeMAC(3))
topo.addHost("h4", ip=Tools.makeIP(4), mac=Tools.makeMAC(4))
topo.addHost("h5", ip=Tools.makeIP(5), mac=Tools.makeMAC(5))
topo.addHost("h6", ip=Tools.makeIP(6), mac=Tools.makeMAC(6))
topo.addHost("h7", ip=Tools.makeIP(7), mac=Tools.makeMAC(7))
topo.addHost("h8", ip=Tools.makeIP(8), mac=Tools.makeMAC(8))

topo.addSwitch("s1", dpid=Tools.makeDPID(1))
topo.addSwitch("s2", dpid=Tools.makeDPID(2))
topo.addSwitch("s3", dpid=Tools.makeDPID(3))
topo.addSwitch("s4", dpid=Tools.makeDPID(4))
topo.addSwitch("s5", dpid=Tools.makeDPID(5))
topo.addSwitch("s6", dpid=Tools.makeDPID(6))
topo.addSwitch("s7", dpid=Tools.makeDPID(7))

topo.addLink("h1", "s4")
topo.addLink("h2", "s4")
topo.addLink("h3", "s5")
topo.addLink("h4", "s5")
topo.addLink("h5", "s6")
topo.addLink("h6", "s6")
topo.addLink("h7", "s7")
topo.addLink("h8", "s7")

topo.addLink("s1", "s2")
topo.addLink("s1", "s3")
topo.addLink("s2", "s4")
topo.addLink("s2", "s5")
topo.addLink("s3", "s6")
topo.addLink("s3", "s7")

# start experiment with OVSSwitch on cluster
exp = maxinet.Experiment(cluster, topo, switch=OVSSwitch)
exp.setup()

print "waiting 5 seconds for routing algorithms on the controller to converge"
time.sleep(5)

print "pinging h2 from h1 to check network connectivity..."
print exp.get_node("h1").cmd("ping -c 100 10.0.0.8")  # show network connectivity

exp.stop()
