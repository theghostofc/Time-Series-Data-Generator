import pandas as pd
import numpy as np

# User inputs
start_date = '2017-10-01'
total_days = 200

df = pd.DataFrame()

# Generate date range for the time-series as string
df['date'] = pd.date_range(start_date, periods = total_days).strftime('%Y-%m-%d')
# Generate frequency of the data
df['count'] = np.random.randint(5, 50, total_days)

df.head()

# Expand the frequencies, generate # of records - date x count
df = pd.concat([pd.DataFrame(data = [row], index = range(row['count'])) for _, row in df.iterrows()],
               ignore_index = True)

import random
def generate_timestamp(column):
    return '{0:s} {1:02d}:{2:02d}:{3:02d}'.format(column, random.randint(0, 23), # Hours
                                                  random.randint(0, 59), # Minutes
                                                  random.randint(0, 59)) # Seconds
# Convert date string to timestamp string
df['date'] = df['date'].apply(generate_timestamp)

# Looks good!
df.head()

# Set of moods to spread randomly. This can be repeated for more randomness.
mood = ['happy', 'neutral', 'sad']

# Randomly assign moods to each row
df['mood'] = np.random.choice(list(mood), len(df))
# Device Id stays same
df['device'] = '1'

# Clean up!
df.drop('count', axis = 1, inplace = True)

# Save as CSV
df.to_csv("smiley.csv")