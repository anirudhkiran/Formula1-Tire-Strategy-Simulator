import itertools
from data_preprocessor import get_laptime_and_stint_length
from monte_carlo_sim import monte_carlo_simulation
from plotter import plot_strategies

track = 'Bahrain'
driver = 'HAM'
num_of_race_laps = 57

laptime_and_stint_length, time_in_pits_dict = get_laptime_and_stint_length(track, driver)

print(laptime_and_stint_length)
print(time_in_pits_dict)

'''
Creating a dictionary for each compound to store:
1. Maximum number of laps driven on this compound in the past
2. Minimum number of laps driven on this compound in the past
3. Average time per lap on a given compound. This is to take into account that the tire degrades over time - meaning
the lap time on the first few laps will be quicker than the last few laps. For the sake of the simulation, I have 
taken an average of all the lap times to closely represent tire degradation
'''
dict_keys = ['max_laps', 'min_laps', 'avg_lap_time']

hard_num_laps = []
hard_lap_times = []

medium_num_laps = []
medium_lap_times = []

soft_num_laps = []
soft_lap_times = []

inter_num_laps = []
inter_lap_times = []

wet_num_laps = []
wet_lap_times = []

medium_compound = dict.fromkeys(dict_keys, 0)
soft_compound = dict.fromkeys(dict_keys, 0)
inter_compound = dict.fromkeys(dict_keys, 0)
wet_compound = dict.fromkeys(dict_keys, 0)

compounds_used = []
for item in laptime_and_stint_length:
    for compound_dict in laptime_and_stint_length[item]:
        print(compound_dict)
        for compound in compound_dict:
            compounds_used.append(compound)
            for stint in compound_dict[compound]:
                if compound == 'HARD':
                    hard_num_laps.append(compound_dict[compound][stint][0])
                    hard_lap_times.append(compound_dict[compound][stint][1])
                if compound == 'MEDIUM':
                    medium_num_laps.append(compound_dict[compound][stint][0])
                    medium_lap_times.append(compound_dict[compound][stint][1])
                if compound == 'SOFT':
                    soft_num_laps.append(compound_dict[compound][stint][0])
                    soft_lap_times.append(compound_dict[compound][stint][1])
                if compound == 'INTERMEDIATE':
                    inter_num_laps.append(compound_dict[compound][stint][0])
                    inter_lap_times.append(compound_dict[compound][stint][1])
                if compound == 'WET':
                    wet_num_laps.append(compound_dict[compound][stint][0])
                    wet_lap_times.append(compound_dict[compound][stint][1])

print(hard_num_laps)
print(hard_lap_times)

print(medium_num_laps)
print(medium_lap_times)

print(soft_num_laps)
print(soft_lap_times)

print(inter_num_laps)
print(inter_lap_times)

print(wet_num_laps)
print(wet_lap_times)

compounds_list = list(set(compounds_used))
print('All compounds used in this race in the past: ', compounds_list)


# creating input data structure for the Monte-Carlo Simulations
monte_carlo_input = {}
for compound in compounds_list:
    if compound == 'HARD':
        monte_carlo_input[compound] = {'avg_lap_time': round(sum(hard_lap_times) / float(len(hard_lap_times)), 3),
                                       'stint_lenghts': [x for x in range(min(hard_num_laps), max(hard_num_laps)+1)]}

    if compound == 'MEDIUM':
        monte_carlo_input[compound] = {'avg_lap_time': round(sum(medium_lap_times) / float(len(medium_lap_times)), 3),
                                       'stint_lenghts': [x for x in range(min(medium_num_laps), max(medium_num_laps) + 1)]}

    if compound == 'SOFT':
        monte_carlo_input[compound] = {'avg_lap_time': round(sum(soft_lap_times) / float(len(soft_lap_times)), 3),
                                       'stint_lenghts': [x for x in range(min(soft_num_laps), max(soft_num_laps) + 1)]}

    if compound == 'INTERMEDIATE':
        monte_carlo_input[compound] = {'avg_lap_time': round(sum(inter_lap_times) / float(len(inter_lap_times)), 3),
                                       'stint_lenghts': [x for x in range(min(inter_num_laps), max(inter_num_laps) + 1)]}

    if compound == 'WET':
        monte_carlo_input[compound] = {'avg_lap_time': round(sum(wet_lap_times) / float(len(wet_lap_times)), 3),
                                       'stint_lenghts': [x for x in
                                                         range(min(wet_num_laps), max(wet_num_laps) + 1)]}

# calculating the average time spent in pits (this will be used while simulating a full-length race in the function below
total_pit_time = 0
for array in time_in_pits_dict.values():
    total_pit_time += array[0]
avg_pitstop_time = round(total_pit_time/float(len(time_in_pits_dict)), 3)

# number of monte-carlo simulations to be carried out
num_of_simulations = 10000

# storing results of the monte carlo simulation so that it can be visualized
race_time_on_strategy = monte_carlo_simulation(num_of_simulations, num_of_race_laps, compounds_list, monte_carlo_input, avg_pitstop_time, )

# sorting the top N quickest race times that were simulated
sorted_strategy_times = dict(sorted(race_time_on_strategy.items()))
top_N_strategies = dict(itertools.islice(sorted_strategy_times.items(), 10))

plot_strategies(track, driver, num_of_race_laps, top_N_strategies)





