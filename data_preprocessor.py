import pandas as pd
import numpy as np
from datetime import datetime

import os

directory = 'input_race_data/Bahrain'


def get_laptime_and_stint_length(track, driver):
    base_directory = 'input_race_data/'
    laptime_and_stint_length = {}
    avg_time_in_pits = {}

    for file in os.listdir(base_directory + track):
        filename = os.fsdecode(file)
        year = filename.split('-')[0]
        df = pd.read_csv(base_directory + track + '/' + filename)

        laptime_and_stint_length[year] = []
        for compound in ['HARD', 'MEDIUM', 'SOFT', 'INTERMEDIATE', 'WET']:
            compound_df = df[(df['Driver'] == driver) & (df['Compound'] == compound)]

            for stint, stint_df in compound_df.groupby(by='Stint'):
                if stint_df.shape[0] == 0:
                    continue
                else:
                    stint_length = stint_df.shape[0]
                    mean_laptime = stint_df['LapTime_in_seconds'].mean().round(3)
                    laptime_and_stint_length[year].append(
                        {compound: {'Stint' + str(stint): [stint_length, mean_laptime]}})

        avg_time_in_pits[year] = []
        df1 = df[(df['Driver'] == driver)]

        pit_in_df = df1.loc[df1['PitInTime'].notnull(), ['PitInTime']]
        pit_in_list = list(pit_in_df['PitInTime'])

        pit_out_df = df1.loc[df1['PitOutTime'].notnull(), ['PitOutTime']]
        pit_out_list = list(pit_out_df['PitOutTime'])

        time_in_pits = calc_avg_pit_stop_time(pit_in_list, pit_out_list)
        avg_time_in_pits[year].append(time_in_pits)

    return laptime_and_stint_length, avg_time_in_pits


def calc_avg_pit_stop_time(pit_in_list, pit_out_list):
    # e.g: pit_in_list = ['0 days 01:25:33.830000', '0 days 02:01:45.619000']
    # e.g: pit_out_list = ['0 days 01:25:58.127000', '0 days 02:02:10.556000']

    # strip the days prefix from the string to only keep HH:MM:SS.ssssss
    strip_days = lambda x: x[7:]
    pit_in_list = [strip_days(x) for x in pit_in_list]
    pit_out_list = [strip_days(x) for x in pit_out_list]

    # convert the string to a datetime object to subtract the two dates
    convert_to_datetime = lambda y: datetime.strptime(y, '%H:%M:%S.%f')
    pit_in_list = [convert_to_datetime(y) for y in pit_in_list]
    pit_out_list = [convert_to_datetime(y) for y in pit_out_list]

    elapsed_times = []
    for t1, t2 in zip(pit_out_list, pit_in_list):
        diff = t1 - t2
        elapsed_times.append(diff.total_seconds())

    avg_time_in_pits = sum(elapsed_times) / float(len(elapsed_times))

    return avg_time_in_pits
