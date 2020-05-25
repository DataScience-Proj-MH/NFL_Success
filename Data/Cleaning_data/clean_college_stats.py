import pandas as pd

college_stats = pd.read_csv('college_stats.txt') # load in both df
combine_stats = pd.read_csv('combine_stats.txt')


counter = -1; #used for creating custom index
# groups each players different college years
for row in range(len(college_stats)):
    if (college_stats.iloc[[row] , 3].astype(str) == 'School').bool():
        counter = counter + 1   
    college_stats.iloc[[row], 0] = counter
    
college_stats = college_stats[college_stats.Scool != 'School'] #removes unnecessary info
college_stats = college_stats[college_stats.Yer != 'Career']

# groups players college stats reducing rows
college_stats = college_stats.groupby('F').aggregate(lambda x: x.unique().tolist())

# cleaning individual Series
games = college_stats.G.apply(pd.Series).fillna(0)
games = games.apply(pd.to_numeric) #makes int 64 type
games = games.sum(axis=1) # sums each row
clean_college_stats = games.to_frame() # from series to df

rec = college_stats.Rec.apply(pd.Series).fillna(0)
rec = rec.apply(pd.to_numeric)
rec = rec.sum(axis=1)
clean_college_stats = pd.concat([clean_college_stats, rec.to_frame()] , axis=1)

recYds = college_stats.RecYds.apply(pd.Series).fillna(0)
recYds = recYds.apply(pd.to_numeric)
recYds = recYds.sum(axis=1)
clean_college_stats = pd.concat([clean_college_stats, recYds.to_frame()] , axis=1)

recAvg = college_stats.RecAvg.apply(pd.Series).fillna(0)
recAvg = recAvg.apply(pd.to_numeric)
recAvg = recAvg.sum(axis=1)
clean_college_stats = pd.concat([clean_college_stats, recAvg.to_frame()] , axis=1)

recTD = college_stats.RecTD.apply(pd.Series).fillna(0)
recTD = recTD.apply(pd.to_numeric)
recTD = recTD.sum(axis=1)
clean_college_stats = pd.concat([clean_college_stats, recTD.to_frame()] , axis=1)

rushAtt = college_stats.RushAtt.apply(pd.Series).fillna(0)
rushAtt = rushAtt.apply(pd.to_numeric)
rushAtt = rushAtt.sum(axis=1)
clean_college_stats = pd.concat([clean_college_stats, rushAtt.to_frame()] , axis=1)

rushYds = college_stats.RushYds.apply(pd.Series).fillna(0)
rushYds = rushYds.apply(pd.to_numeric)
rushYds = rushYds.sum(axis=1)
clean_college_stats = pd.concat([clean_college_stats, rushYds.to_frame()] , axis=1)

rushAvg = college_stats.RushAvg.apply(pd.Series).fillna(0)
rushAvg = rushAvg.apply(pd.to_numeric)
rushAvg = rushAvg.sum(axis=1)
clean_college_stats = pd.concat([clean_college_stats, rushAvg.to_frame()] , axis=1)

rushTD = college_stats.RushTD.apply(pd.Series).fillna(0)
rushTD = rushTD.apply(pd.to_numeric)
rushTD = rushTD.sum(axis=1)
clean_college_stats = pd.concat([clean_college_stats, rushTD.to_frame()] , axis=1)

scrimPlays = college_stats.ScrimPlays.apply(pd.Series).fillna(0)
scrimPlays = scrimPlays.apply(pd.to_numeric)
scrimPlays = scrimPlays.sum(axis=1)
clean_college_stats = pd.concat([clean_college_stats, scrimPlays.to_frame()] , axis=1)

scrimYds = college_stats.ScrimYds.apply(pd.Series).fillna(0)
scrimYds = scrimYds.apply(pd.to_numeric)
scrimYds = scrimYds.sum(axis=1)
clean_college_stats = pd.concat([clean_college_stats, scrimYds.to_frame()] , axis=1)

scrimAvg = college_stats.ScrimAvg.apply(pd.Series).fillna(0)
scrimAvg = scrimAvg.apply(pd.to_numeric)
scrimAvg = scrimAvg.sum(axis=1)
clean_college_stats = pd.concat([clean_college_stats, scrimAvg.to_frame()] , axis=1)

scrimTD = college_stats.ScrimTD.apply(pd.Series).fillna(0)
scrimTD = scrimTD.apply(pd.to_numeric)
scrimTD = scrimTD.sum(axis=1)    
clean_college_stats = pd.concat([clean_college_stats, scrimTD.to_frame()] , axis=1)

# remove columns
clean_college_stats.columns = ['C Games', 'C Rec', 'C RecYds', 'C  RecAvg', 'C RecTD', 'C RushAtt',
                               'C Rush Yds', 'C RushAvg', 'C RushTD', 'C ScrimPLays', 'C ScrimYds',
                               'C ScrimAvg', 'C ScrimTD']

#drop incompatible row
clean_college_stats = clean_college_stats.drop(clean_college_stats.index[426])
clean_college_stats = clean_college_stats.reset_index()

#combine combine_stats and clean_college_stats and export
combine_college = combine_stats.join(clean_college_stats)
combine_college.to_csv(r'college_and_combine_stats.csv')