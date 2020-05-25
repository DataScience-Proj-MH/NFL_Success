import pandas as pd

college_stats = pd.read_csv('college_and_combine_stats.csv')
nfl_stats = pd.read_csv('nfl_player_stats_clean.csv')

college_stats[['Round' , 'del']] = college_stats['Round'].str.split('th' , expand=True)
college_stats[['Round' , 'del']] = college_stats['Round'].str.split('st' , expand=True)
college_stats[['Round' , 'del']] = college_stats['Round'].str.split('nd' , expand=True)
college_stats[['Round' , 'del']] = college_stats['Round'].str.split('rd' , expand=True)

college_stats['Round'] = pd.to_numeric(college_stats['Round']).astype(int)
college_stats['Rnd'] = college_stats['Round']

college_stats[['Pick' , 'del2']] = college_stats['Pick'].str.split('th' , expand=True)
college_stats[['Pick' , 'del2']] = college_stats['Pick'].str.split('st' , expand=True)
college_stats[['Pick' , 'del2']] = college_stats['Pick'].str.split('nd' , expand=True)
college_stats[['Pick' , 'del2']] = college_stats['Pick'].str.split('rd' , expand=True)

college_stats['Pick'] = pd.to_numeric(college_stats['Pick']).astype(int)

complete_player_stats = pd.merge(college_stats, nfl_stats , on=['Rnd' , 'Pick' , 'Year'] , how='inner')

complete_player_stats[['Ht Ft' , 'Ht In']] = complete_player_stats['Ht'].str.split('-' , expand=True)
complete_player_stats['Ht Ft'] = complete_player_stats['Ht Ft'].apply(pd.to_numeric)
complete_player_stats['Ht In'] = complete_player_stats['Ht In'].apply(pd.to_numeric)

complete_player_stats = complete_player_stats.drop(columns=['Unnamed: 0_x' , 'Unnamed: 0.1' , 'College_x' , 'F' , 'del' , 'del2',
                                                            'Unnamed: 0_y' , 'Player_y' , 'Pos_y' , 'Tm' , 'QBrec' , 'College_y' , 'Ht'])

complete_player_stats.to_csv(r'final_df.csv')