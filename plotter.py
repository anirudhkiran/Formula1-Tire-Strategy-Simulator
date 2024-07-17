import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def generate_df_for_plot(strategies):
    df_array = []

    for time in strategies:
        entry = strategies[time]
        for stint in entry:
            # for each race time, create N arrays where N -> number of stints
            # each row_array is [time, stint number, compound used, stint length]
            row_array = [time, stint, entry[stint]['tire'], entry[stint]['num_laps_on_tire']]
            df_array.append(row_array)

    df = pd.DataFrame(df_array, columns=['Race Time', 'Stint Num', 'Compound', 'Stint Length'])

    return df

def plot_strategies(track, driver, num_of_race_laps, strategies):
    colors = {
        'HARD': 'lightgray',
        'MEDIUM': 'yellow',
        'SOFT': 'red',
        'INTERMEDIATE': 'green',
        'WET': 'blue'
    }

    time_array = list(strategies.keys())
    df_for_plot = generate_df_for_plot(strategies)

    fig, ax = plt.subplots(figsize=(5, 10))

    for time in time_array:
        time_entries = df_for_plot.loc[df_for_plot["Race Time"] == time]

        previous_stint_end = 0
        for idx, row in time_entries.iterrows():
            rects = plt.barh(
                y=time,
                width=row["Stint Length"],
                left=previous_stint_end,
                color=colors[row['Compound']],
                edgecolor="black",
                fill=True,
                height=8
            )

            ax.bar_label(rects, label_type='center', color='black')

            previous_stint_end += row["Stint Length"]

        # X co-ordinate to place the label in the plot. Y co-ordinate will be the race time
        x_coord = num_of_race_laps + 2
        plt.annotate(str(time), xy=(x_coord, time), ha='center', va='center')

    ax.invert_yaxis()

    plt.title("{} Grand Prix Strategies for {}".format(track, driver))
    plt.xlabel("Lap Number")
    plt.ylabel("Race Duration (in seconds)")
    plt.grid(False)

    ax.invert_yaxis()
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    plt.show()
