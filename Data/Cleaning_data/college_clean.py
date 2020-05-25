import pandas as pd

df = pd.read_csv('csv/college2.csv')


cols = ['Index2', 'Year', 'School', 'Conf', 'Class', 'Pos',	'G', 'Rec', 'RecYds', 'RecAvg', 'RecTD', 'RushAtt',
        'RushYds', 'RushAvg', 'RushTD', 'ScrimPlays', 'ScrimYds', 'ScrimAvg', 'ScrimTD']
df.columns = cols


df = df[~df['Year'].isnull()]

df.to_csv('college_stats.csv')
