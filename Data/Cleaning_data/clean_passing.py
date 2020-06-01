import pandas as pd

passing_df = pd.read_csv('qb_college_passing.txt')

# groups each players different college years
counter = -1
for row in range(len(passing_df)):
    if (passing_df.iloc[[row] , 2].astype(str) == 'School').bool():
        counter = counter + 1   
    passing_df.iloc[[row], 0] = counter

passing_df = passing_df.groupby('Unnamed: 0').aggregate(lambda x: x.unique().tolist())

names = passing_df['Unnamed: 0.1'].apply(pd.Series).fillna(0)
names = names.loc[:, 0] # only keeps column with player names
clean_passing_stats = names.to_frame() # from series to df

games = passing_df['C G'].apply(pd.Series).fillna(0)
games = games.drop(0, axis=1) #drop column with titles
games = games.apply(pd.to_numeric) #makes int 64 type
games = games.sum(axis=1) # sums each row
clean_passing_stats = pd.concat([clean_passing_stats, games.to_frame()] , axis=1) #merge columns

completions = passing_df['C Cmp'].apply(pd.Series).fillna(0)
completions= completions.drop(0, axis=1) #drop column with titles
completions = completions.apply(pd.to_numeric) #makes int 64 type
completions = completions.sum(axis=1) # sums each row
clean_passing_stats = pd.concat([clean_passing_stats, completions.to_frame()] , axis=1) #merge columns

attempts = passing_df['C Att'].apply(pd.Series).fillna(0)
attempts = attempts.drop(0, axis=1) #drop column with titles
attempts = attempts.apply(pd.to_numeric) #makes int 64 type
attempts = attempts.sum(axis=1) # sums each row
clean_passing_stats = pd.concat([clean_passing_stats, attempts.to_frame()] , axis=1) #merge columns

percentage = passing_df['C Pct'].apply(pd.Series).fillna(0)
percentage = percentage.drop(0, axis=1) #drop column with titles
percentage = percentage.apply(pd.to_numeric) #makes int 64 type
percentage = percentage.sum(axis=1) # sums each row
clean_passing_stats = pd.concat([clean_passing_stats, percentage.to_frame()] , axis=1) #merge columns

yards = passing_df['C Yds'].apply(pd.Series).fillna(0)
yards = yards.drop(0, axis=1) #drop column with titles
yards = yards.apply(pd.to_numeric) #makes int 64 type
yards = yards.sum(axis=1) # sums each row
clean_passing_stats = pd.concat([clean_passing_stats, yards.to_frame()] , axis=1) #merge columns

ya = passing_df['C Y/A'].apply(pd.Series).fillna(0)
ya = ya.drop(0, axis=1) #drop column with titles
ya = ya.apply(pd.to_numeric) #makes int 64 type
ya = ya.sum(axis=1) # sums each row
clean_passing_stats = pd.concat([clean_passing_stats, ya.to_frame()] , axis=1) #merge columns

aya = passing_df['C AY/A'].apply(pd.Series).fillna(0)
aya = aya.drop(0, axis=1) #drop column with titles
aya = aya.apply(pd.to_numeric) #makes int 64 type
aya = aya.sum(axis=1) # sums each row
clean_passing_stats = pd.concat([clean_passing_stats, aya.to_frame()] , axis=1) #merge columns

touchdown = passing_df['C TD'].apply(pd.Series).fillna(0)
touchdown = touchdown.drop(0, axis=1) #drop column with titles
touchdown = touchdown.apply(pd.to_numeric) #makes int 64 type
touchdown = touchdown.sum(axis=1) # sums each row
clean_passing_stats = pd.concat([clean_passing_stats, touchdown.to_frame()] , axis=1) #merge columns

interception = passing_df['C Int'].apply(pd.Series).fillna(0)
interception = interception.drop(0, axis=1) #drop column with titles
interception = interception.apply(pd.to_numeric) #makes int 64 type
interception = interception.sum(axis=1) # sums each row
clean_passing_stats = pd.concat([clean_passing_stats, interception.to_frame()] , axis=1) #merge columns

rate = passing_df['C Rate'].apply(pd.Series).fillna(0)
rate = rate.drop(0, axis=1) #drop column with titles
rate = rate.apply(pd.to_numeric) #makes int 64 type
rate = rate.sum(axis=1) # sums each row
clean_passing_stats = pd.concat([clean_passing_stats, rate.to_frame()] , axis=1) #merge columns

clean_passing_stats.to_csv(r'cleaned_passing_stats.csv')

