# Formula1-Tire-Strategy-Simulator

Developed a software program that uses the Monte-Carlo simulation technique to predict the best possible tire strategies for a race. 

The data_preprocessor.py file extracts data such as compounds used in different stints, stint lengths and the time taken for each lap on a compound from past race data stored in the input_race_data folder. It also extracts average time spent in the pits for past races.

This data serves as an input to the monte_carlo_sim.py that performs hundreds of thousands of iterations.
Each iteration users tire and pit stop data to simulates a full length race. The elapsed race duration is recorded and the top strategies are visualized in a graph for easy analysis. 

The orchestrator for the entire program is the main.py file. Here you can set parameters such as the race location, the number of laps in the race and number of iterations of the Monte-Carlo simulation

The results of the simulations for the Bahrain Grand Prix and Lewis Hamilton as the driver are show here:

![image](https://github.com/user-attachments/assets/ee3e53cb-b098-419f-8e26-2f8bb6367438)

