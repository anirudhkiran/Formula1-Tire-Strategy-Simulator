# Formula1-Tire-Strategy-Simulator

Developed a software program that uses the Monte-Carlo simulation technique to predict the best possible tire strategies for a race. 

data_preprocessor.py - extracts data such as compounds used in different stints, stint lengths and the time taken for each lap on a compound from past race data stored in the input_race_data folder. It also extracts average time spent in the pits for past races.

monte_carlo_sim.py - data from previous file serves as an input to the monte_carlo_sim.py that performs hundreds of thousands of iterations. Each iteration users tire and pit stop data to simulate a full length race. The elapsed race duration for each iteration is recorded  

main.py - this is the orchestrator for the entire program. Here you can set parameters such as the race location, the number of laps in the race and number of iterations of the Monte-Carlo simulation

plotter.py - the top strategies are visualized in a graph for easy analysis

The results of the simulations for the Bahrain Grand Prix and Lewis Hamilton as the driver are show here:

![image](https://github.com/user-attachments/assets/ee3e53cb-b098-419f-8e26-2f8bb6367438)

