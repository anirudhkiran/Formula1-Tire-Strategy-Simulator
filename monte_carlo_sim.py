import random

'''
This functions simulates a race 'num_iterations' times. The Monte-Carlo simulation is a stochastic process that takes in
random parameters for its simulations. The idea behind this technique is that even though the variables are taken at random,
if the simulations are carried out enough times, we will start to see some sort of repetitive pattern emerging.
'''


def monte_carlo_simulation(num_iterations, num_of_race_laps, compounds_list, monte_carlo_input, avg_pitstop_time):
    race_time_on_strategy = {}
    for i in range(num_iterations):

        print('Started Simulation ', i + 1)

        total_race_time = 0
        sim_laps = 0
        chequered_flag = False
        strategy_used = {}
        stint = 0

        while sim_laps < num_of_race_laps:
            stint += 1

            # choose a tire at random
            tire_index = random.randrange(len(compounds_list))
            tire = compounds_list[tire_index]

            # choose a stint length for the selected tire at random
            stint_length = random.choice(monte_carlo_input[tire]['stint_lenghts'])

            '''Calculate the total time on the selected tire. This can be done by multiplying the avg_lap_time for the 
            tire and the total number of laps driven on this tire'''

            total_time_on_tire = monte_carlo_input[tire]['avg_lap_time'] * stint_length

            # update the race time and laps for this iteration
            total_race_time += total_time_on_tire
            sim_laps += stint_length

            # log the tires used and the number of laps on the tire for this stint
            strategy_used[stint] = {'tire': tire, 'num_laps_on_tire': stint_length}

            if sim_laps == num_of_race_laps:
                print('Chequered Flag!')
                chequered_flag = True
                # if race has ended, simulation is complete. Exit
                break
            else:
                # once the tire life is complete, pit and change the tire
                total_race_time += avg_pitstop_time
                # print('Pitting to change tires')

        if chequered_flag:
            print('Race concluded.')
            print('Tire strategy used in the simulation:', strategy_used)
            race_time_on_strategy[round(total_race_time, 3)] = strategy_used
            print('race_time_on_strategy: ', race_time_on_strategy)

        # else:
        #     # print('Tire choice does not fit the number of race laps')
        #     # print('Tire strategy used in the simulation:', strategy_used)

        print('Ended Simulation ', i + 1)

    return race_time_on_strategy
