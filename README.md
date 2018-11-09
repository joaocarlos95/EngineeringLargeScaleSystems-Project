# Engineering of Large Scale Systems Project (2018-2019)

### Contributors
- [@joaocarlos95](https://github.com/joaocarlos95) - João Carlos
- [@joaopbc](https://github.com/joaopbc) - João Correia
- [@RubenCondesso](https://github.com/RubenCondesso) - Rúben Condesso

### About
The main objective is to analyse and test a real distributed system with client-server architecture.

This project has 2 parts:
  1. The first part consists in analyse and testing the performance and scalability of the MaxiNet System
  2. 
  
### How to run:
#### Project Part 1
- Open a terminal and run the command ./StartUp.sh
- Choose the number of workers
- After all installation, you'll have open 1 terminal for the Controller, 1 for the FrontendServer and N for the Workers
- Open a new one and get the ID of the FrontendServer by enter the command "docker ps"
- After that enter inside the container by executing the command "docker exec -it <ID_FrontendServer> bash"
- You can perform some tests inside the folder /containernet/MaxiNet/MaxiNet/Frontend/examples/

#### Project Part 2
- 
