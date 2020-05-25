import pandas as pd

df = pd.read_csv('csv/first_try.csv')
print(df)
df.drop(df.columns[0], axis=1,inplace=True)
print(df)

positions = ['OT','OG','OL','C','DE','DT','DL','EDGE','ILB','OLB','LB','SS','FS','S','CB','LS','K','P']
df = df[~df.Pos.isin(positions)]
print(df)

df =df[pd.notnull(df['College'])]
df =df[pd.notnull(df['Drafted (tm/rnd/yr)'])]

df[['Team','Round', 'Pick', 'Year']] = df['Drafted (tm/rnd/yr)'].str.split('/', expand = True, n=4)


df = df.reset_index(drop=True)

print(df)


df['Player'] = df['Player'].str.split('\\').str[0]

df.drop(df.columns[12], axis=1, inplace=True)
print(df)

players = ['Lamar Jackson', 'Brandon Jones', 'Daniel Thomas', 'Josh Allen', 'Nate Davis', 'Greg Little', 'Brian Allen', 'Minkah Fitzpatrick', 'Brian Allen', 'Quincy Wilson', 'Taiwan Jones',
           'Kevin White', 'Chris Davis', 'Charles Sims', 'Marcus Smith', 'Brennan Williams', 'Josh Johnson', 'Darius Slay', 'Jonathan Stewart', 'Josh Harris', 'Brandon Marshall', 'Josh Robinson',
           'Roy Helu', 'Greg Jones', 'Anthony Davis', 'Michael Bennett', 'Brandon Williams', 'Josh Johnson', 'Aundrae Allison', 'Levi Brown', 'Buster Davis', 'Buster Davis', 'Marcus Thomas',
           'Brian Calhoun', 'Joseph Addai', 'Bobby Carpenter', 'Courtney Anderson', 'Enoch Demar', 'Chris Brown', 'Jermaine Petty', 'Steve Smith', 'Mike Williams', 'Roy Williams', 'Brian Allen',
           'Doug Martin', 'Justin Forsett', 'Leonard Henry', 'Odell Beckham Jr.']
df = df[~df.Player.isin(players)]
print(df)

df.to_csv('combine_stats.csv')