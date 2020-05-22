import pandas as pd

nfl_player_stats = pd.read_csv('nfl_player_stats.csv')
nfl_player_stats = nfl_player_stats.loc[:, ~nfl_player_stats.columns.str.contains('^Unnamed')] #delete unnamed column
nfl_player_stats = nfl_player_stats.dropna(subset = ['Year']) # drop all row headers from collecting data

nfl_player_stats[['Player' , 'Extra Info']] = nfl_player_stats['Player'].str.split(' HOF' , expand=True)#remove HOF tag on player names
nfl_player_stats = nfl_player_stats.drop(columns=['Extra Info' , 'College Stats']) #drop columns

nfl_player_stats.to_csv(r'nfl_player_stats_clean.csv')