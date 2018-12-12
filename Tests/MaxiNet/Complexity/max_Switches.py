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

cluster = maxinet.Cluster(minWorkers=2, maxWorkers=2)

topo = Topo()
topo.addHost("h1", ip=Tools.makeIP(1), mac=Tools.makeMAC(1))
topo.addHost("h2", ip=Tools.makeIP(2), mac=Tools.makeMAC(2))
topo.addHost("h3", ip=Tools.makeIP(3), mac=Tools.makeMAC(3))
topo.addHost("h4", ip=Tools.makeIP(4), mac=Tools.makeMAC(4))


topo.addSwitch("s1", dpid=Tools.makeDPID(1), wid=0)
topo.addSwitch("s2", dpid=Tools.makeDPID(2), wid=0)
topo.addSwitch("s3", dpid=Tools.makeDPID(3), wid=1)
topo.addSwitch("s4", dpid=Tools.makeDPID(4), wid=0)
topo.addSwitch("s5", dpid=Tools.makeDPID(5), wid=1)
topo.addSwitch("s6", dpid=Tools.makeDPID(6), wid=0)
topo.addSwitch("s7", dpid=Tools.makeDPID(7), wid=0)
topo.addSwitch("s8", dpid=Tools.makeDPID(8), wid=1)
topo.addSwitch("s9", dpid=Tools.makeDPID(9), wid=1)
topo.addSwitch("s10", dpid=Tools.makeDPID(10), wid=0)
topo.addSwitch("s11", dpid=Tools.makeDPID(11), wid=0)
topo.addSwitch("s12", dpid=Tools.makeDPID(12), wid=0)
topo.addSwitch("s13", dpid=Tools.makeDPID(13), wid=0)
topo.addSwitch("s14", dpid=Tools.makeDPID(14), wid=1)
topo.addSwitch("s15", dpid=Tools.makeDPID(15), wid=1)
topo.addSwitch("s16", dpid=Tools.makeDPID(16), wid=1)
topo.addSwitch("s17", dpid=Tools.makeDPID(17), wid=1)




topo.addLink("h1", "s10")
topo.addLink("h2", "s10")
topo.addLink("h3", "s17")
topo.addLink("h4", "s17")




topo.addLink("s1", "s2")
topo.addLink("s1", "s3")
topo.addLink("s3", "s5")
topo.addLink("s2", "s4")
topo.addLink("s4", "s6")
topo.addLink("s4", "s7")
topo.addLink("s5", "s8")
topo.addLink("s5", "s9")
topo.addLink("s6", "s10")
topo.addLink("s6", "s11")
topo.addLink("s7", "s12")
topo.addLink("s7", "s13")
topo.addLink("s8", "s14")
topo.addLink("s8", "s15")
topo.addLink("s9", "s16")
topo.addLink("s9", "s17")

# start experiment with OVSSwitch on cluster
exp = maxinet.Experiment(cluster, topo, switch=OVSSwitch)
exp.setup()

print "waiting 5 seconds for routing algorithms on the controller to converge"
time.sleep(5)

print "pinging h2 from h1 to check network connectivity..."
print exp.get_node("h1").cmd("ping -c 100 10.0.0.3")  # show network connectivity

print exp.get_node("h1").cmd("iperf -s -u &")
print exp.get_node("h4").cmd("iperf -c 10.0.0.1 -u")

exp.stop()