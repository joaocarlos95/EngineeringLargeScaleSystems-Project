# Engineering of Large Scale Systems Project (2018-2019)

### Contributors
- [@joaocarlos95](https://github.com/joaocarlos95) - João Carlos
- [@joaopbc](https://github.com/joaopbc) - João Correia
- [@RubenCondesso](https://github.com/RubenCondesso) - Rúben Condesso

### About
The main objective is to analyse and test a real distributed system with client-server architecture.

This project has 2 parts:
  1. The first part consists in analyse and testing the performance and scalability of the Mininet System
  2. The second part consists in analyse and testing the performance and scalability of the MaxiNet System

### Repository Content
```bash
.
├── clearAll.sh
├── InstallMaxiNet.sh
├── MakeInstall.sh
├── MaxiNet.cfg
├── README.md
├── Report - Part 1.pdf
├── Report - Part 2.pdf
├── StartUp.sh
└── Tests
    ├── MaxiNet
    │   ├── Complexity Latency
    │   │   ├── FatTree05.py
    │   │   ├── FatTree10.py
    │   │   ├── FatTree120.py
    │   │   ├── FatTree20.py
    │   │   ├── FatTree40.py
    │   │   ├── FatTree80.py
    │   │   └── Results
    │   │       ├── FatTree05.txt
    │   │       ├── FatTree10.txt
    │   │       ├── FatTree120.txt
    │   │       ├── FatTree20.txt
    │   │       ├── FatTree40.txt
    │   │       └── FatTree80.txt
    │   ├── Complexity Memory
    │   │   ├── FatTree05.py
    │   │   ├── FatTree10.py
    │   │   ├── FatTree120.py
    │   │   ├── FatTree20.py
    │   │   ├── FatTree40.py
    │   │   ├── FatTree80.py
    │   │   └── Results
    │   │       ├── FatTree05.txt
    │   │       ├── FatTree10.txt
    │   │       ├── FatTree120.txt
    │   │       ├── FatTree20.txt
    │   │       ├── FatTree40.txt
    │   │       └── FatTree80.txt
    │   ├── Complexity RTTController
    │   │   ├── FatTree05.py
    │   │   ├── FatTree10.py
    │   │   ├── FatTree120.py
    │   │   ├── FatTree20.py
    │   │   ├── FatTree40.py
    │   │   ├── FatTree80.py
    │   │   └── Results
    │   │       ├── FatTree05.txt
    │   │       ├── FatTree10.txt
    │   │       ├── FatTree120.txt
    │   │       ├── FatTree20.txt
    │   │       ├── FatTree40.txt
    │   │       └── FatTree80.txt
    │   ├── CPU Latency
    │   │   ├── Controller
    │   │   │   └── Results
    │   │   │       ├── 100%CPU.txt
    │   │   │       ├── 10%CPU.txt
    │   │   │       ├── 20%CPU.txt
    │   │   │       ├── 50%CPU.txt
    │   │   │       └── 5%CPU.txt
    │   │   ├── FatTree05_2Workers.py
    │   │   ├── FrontendServer
    │   │   │   └── Results
    │   │   │       ├── 100%CPU.txt
    │   │   │       ├── 10%CPU.txt
    │   │   │       ├── 20%CPU.txt
    │   │   │       ├── 50%CPU.txt
    │   │   │       └── 5%CPU.txt
    │   │   └── Workers
    │   │       └── Results
    │   │           ├── 100%CPU.txt
    │   │           ├── 10%CPU.txt
    │   │           ├── 20%CPU.txt
    │   │           ├── 50%CPU.txt
    │   │           └── 5%CPU.txt
    │   ├── MaxiNet vs Mininet
    │   │   ├── Tree23_MaxiNet.txt
    │   │   └── Tree23_Mininet.txt
    │   ├── NrWorkers Latency
    │   │   ├── 1Worker_1.py
    │   │   ├── 1Worker_2.py
    │   │   ├── 2Workers_1.py
    │   │   ├── 2Workers_2.py
    │   │   ├── 3Workers_1.py
    │   │   ├── 3Workers_2.py
    │   │   ├── 5Workers_1.py
    │   │   ├── 5Workers_2.py
    │   │   ├── 7Workers_1.py
    │   │   ├── 7Workers_2.py
    │   │   └── Results
    │   │       ├── 1Worker_1.txt
    │   │       ├── 1Worker_2.txt
    │   │       ├── 2Workers_1.txt
    │   │       ├── 2Workers_2.txt
    │   │       ├── 3Workers_1.txt
    │   │       ├── 3Workers_2.txt
    │   │       ├── 5Workers_1.txt
    │   │       ├── 5Workers_2.txt
    │   │       ├── 7Workers_1.txt
    │   │       └── 7Workers_2.txt
    │   ├── NrWorkers Memory
    │   │   ├── 1Worker.py
    │   │   ├── 2Workers.py
    │   │   ├── 3Workers.py
    │   │   ├── 5Workers.py
    │   │   ├── 7Workers.py
    │   │   └── Results
    │   │       ├── 1Worker.txt
    │   │       ├── 2Workers.txt
    │   │       ├── 3Workers.txt
    │   │       ├── 5Workers.txt
    │   │       └── 7Workers.txt
    │   └── NrWorkers RTTController
    │       ├── 1Worker.py
    │       ├── 2Workers.py
    │       ├── 3Workers.py
    │       ├── 5Workers.py
    │       ├── 7Workers.py
    │       └── Results
    │           ├── 1Worker.txt
    │           ├── 2Workers.txt
    │           ├── 3Workers.txt
    │           ├── 5Workers.txt
    │           └── 7Workers.txt
    └── Mininet
        ├── Bandwidth.txt
        ├── CPU.txt
        └── Pings.txt
```
  
### How to run:
#### Project Part 1
- Download the project to your computer
- Open a terminal and run the command **`chmod +x ./StartUp.sh && ./StartUp.sh`**
- Choose the number of workers
- After the installation, you'll have open 1 terminal for the Controller, 1 for the FrontendServer and N for the Workers
- Open a new one and get the ID of the Controller by enter the command **`docker ps`** and run the command **`docker exec -it <ID_Controller> bash`**
- You can perform some tests inside the folder /containernet/MaxiNet/MaxiNet/Frontend/examples/

#### Project Part 2
- 

##### P.S. You must have _docker_ installed on your computer as well _gnome-terminal_
