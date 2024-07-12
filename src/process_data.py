import numpy as np
import os
from os.path import dirname, abspath
import pandas as pd

root_dir = dirname(dirname(abspath(__file__)))
data_filename = os.path.join(root_dir, 'data/raw_data/boost_df.csv')

df = pd.read_csv(data_filename)

# Time features
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['trip_start_date'] = pd.to_datetime(df['trip_start_date'])
df['offer_hour'] = df['timestamp'].dt.hour

df['offer_start_time'] = df.groupby('trip_id')['timestamp'].transform('min')
df['time_elapsed'] = (df['timestamp'] - df['offer_start_time']).dt.total_seconds() / 60

# Boost features
df['total_boost'] = df['total_price'] - df['base_price']
df['avg_boost'] = df.groupby(['metro_area', 'base_price', 'boost_number']).total_boost.transform('mean')
df['total_boost_pct_change_from_avg'] = (df['total_boost'] - df['avg_boost']) / df['avg_boost'] * 100
df['total_boost_pct_change_from_avg'] = df['total_boost_pct_change_from_avg'].fillna(0)

# Driver features
df['avg_driver_supply'] = df.groupby(['metro_area', 'offer_hour']).total_driver_supply.transform('mean')
df['driver_supply_difference'] = (df['total_driver_supply'] - df['avg_driver_supply']) / df['avg_driver_supply']

# Remove unnecessary features
df = df[['claimed', 'time_elapsed', 'total_boost', 'total_boost_pct_change_from_avg', 'driver_supply_difference']]

# Export data
data_dir = os.path.join(root_dir, 'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

model_data_dir = os.path.join(data_dir, 'model_data')
if not os.path.exists(model_data_dir):
    os.makedirs(os.path.join(model_data_dir))

target_filepath = os.path.join(model_data_dir, 'model_data.csv')
df.to_csv(target_filepath, index=False)