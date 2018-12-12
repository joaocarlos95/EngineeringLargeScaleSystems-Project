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
topo.addHost("h5", ip=Tools.makeIP(5), mac=Tools.makeMAC(5))
topo.addHost("h6", ip=Tools.makeIP(6), mac=Tools.makeMAC(6))
topo.addHost("h7", ip=Tools.makeIP(7), mac=Tools.makeMAC(7))
topo.addHost("h8", ip=Tools.makeIP(8), mac=Tools.makeMAC(8))
topo.addHost("h9", ip=Tools.makeIP(9), mac=Tools.makeMAC(9))
topo.addHost("h10", ip=Tools.makeIP(10), mac=Tools.makeMAC(10))
topo.addHost("h11", ip=Tools.makeIP(11), mac=Tools.makeMAC(11))
topo.addHost("h12", ip=Tools.makeIP(12), mac=Tools.makeMAC(12))
topo.addHost("h13", ip=Tools.makeIP(13), mac=Tools.makeMAC(13))
topo.addHost("h14", ip=Tools.makeIP(14), mac=Tools.makeMAC(14))
topo.addHost("h15", ip=Tools.makeIP(15), mac=Tools.makeMAC(15))
topo.addHost("h16", ip=Tools.makeIP(16), mac=Tools.makeMAC(16))
topo.addHost("h17", ip=Tools.makeIP(17), mac=Tools.makeMAC(17))
topo.addHost("h18", ip=Tools.makeIP(18), mac=Tools.makeMAC(18))
topo.addHost("h19", ip=Tools.makeIP(19), mac=Tools.makeMAC(19))
topo.addHost("h20", ip=Tools.makeIP(20), mac=Tools.makeMAC(20))
topo.addHost("h21", ip=Tools.makeIP(21), mac=Tools.makeMAC(21))
topo.addHost("h22", ip=Tools.makeIP(22), mac=Tools.makeMAC(22))
topo.addHost("h23", ip=Tools.makeIP(23), mac=Tools.makeMAC(23))
topo.addHost("h24", ip=Tools.makeIP(24), mac=Tools.makeMAC(24))
topo.addHost("h25", ip=Tools.makeIP(25), mac=Tools.makeMAC(25))
topo.addHost("h26", ip=Tools.makeIP(26), mac=Tools.makeMAC(26))
topo.addHost("h27", ip=Tools.makeIP(27), mac=Tools.makeMAC(27))
topo.addHost("h28", ip=Tools.makeIP(28), mac=Tools.makeMAC(28))


topo.addSwitch("s1", dpid=Tools.makeDPID(1), wid=0)
topo.addSwitch("s2", dpid=Tools.makeDPID(2), wid=1)
topo.addSwitch("s3", dpid=Tools.makeDPID(3), wid=1)
topo.addSwitch("s4", dpid=Tools.makeDPID(4), wid=1)
topo.addSwitch("s5", dpid=Tools.makeDPID(5), wid=0)
topo.addSwitch("s6", dpid=Tools.makeDPID(6), wid=0)
topo.addSwitch("s7", dpid=Tools.makeDPID(7), wid=1)
topo.addSwitch("s8", dpid=Tools.makeDPID(8), wid=1)
topo.addSwitch("s9", dpid=Tools.makeDPID(9), wid=1)
topo.addSwitch("s10", dpid=Tools.makeDPID(10), wid=1)
topo.addSwitch("s11", dpid=Tools.makeDPID(11), wid=1)
topo.addSwitch("s12", dpid=Tools.makeDPID(12), wid=0)
topo.addSwitch("s13", dpid=Tools.makeDPID(13), wid=0)
topo.addSwitch("s14", dpid=Tools.makeDPID(14), wid=0)
topo.addSwitch("s15", dpid=Tools.makeDPID(15), wid=0)
topo.addSwitch("s16", dpid=Tools.makeDPID(16), wid=0)

topo.addLink("h1", "s5")
topo.addLink("h2", "s5")
topo.addLink("h3", "s6")
topo.addLink("h4", "s6")
topo.addLink("h5", "s3")
topo.addLink("h6", "s3")
topo.addLink("h7", "s4")
topo.addLink("h8", "s4")
topo.addLink("h9", "s7")
topo.addLink("h10", "s7")
topo.addLink("h11", "s8")
topo.addLink("h12", "s8")
topo.addLink("h13", "s9")
topo.addLink("h14", "s9")
topo.addLink("h15", "s10")
topo.addLink("h16", "s10")
topo.addLink("h17", "s11")
topo.addLink("h18", "s11")
topo.addLink("h19", "s12")
topo.addLink("h20", "s12")
topo.addLink("h21", "s13")
topo.addLink("h22", "s13")
topo.addLink("h23", "s14")
topo.addLink("h24", "s14")
topo.addLink("h25", "s15")
topo.addLink("h26", "s15")
topo.addLink("h27", "s16")
topo.addLink("h28", "s16")




topo.addLink("s1", "s2")
topo.addLink("s1", "s5")
topo.addLink("s1", "s6")
topo.addLink("s1", "s12")
topo.addLink("s1", "s13")
topo.addLink("s1", "s14")
topo.addLink("s1", "s15")
topo.addLink("s1", "s16")


topo.addLink("s2", "s3")
topo.addLink("s2", "s4")
topo.addLink("s2", "s5")
topo.addLink("s2", "s6")
topo.addLink("s2", "s7")
topo.addLink("s2", "s8")
topo.addLink("s2", "s9")
topo.addLink("s2", "s10")
topo.addLink("s2", "s11")




# start experiment with OVSSwitch on cluster
exp = maxinet.Experiment(cluster, topo, switch=OVSSwitch)
exp.setup()

print "waiting 5 seconds for routing algorithms on the controller to converge"
time.sleep(5)

print "pinging h2 from h1 to check network connectivity..."
print exp.get_node("h1").cmd("ping -c 100 10.0.0.8")  # show network connectivity

exp.stop()
