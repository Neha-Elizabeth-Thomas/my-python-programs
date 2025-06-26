import pandas as pd

# Create the DataFrame
data = {
    'Player': ['Hardik Pandya', 'KL Rahul', 'Andre Russel', 'Jasprit Bumrah', 'Virat Kohli', 'Rohit Sharma'],
    'Team': ['Mumbai Indians', 'Kings Eleven', 'Kolkata Knight riders', 'Mumbai Indians', 'RCB', 'Mumbai Indians'],
    'Category': ['Batsman', 'Batsman', 'Batsman', 'Bowler', 'Batsman', 'Batsman'],
    'BidPrice': [13, 12, 7, 10, 17, 15],
    'Runs': [1000, 2400, 900, 200, 3600, 3700]
}

df = pd.DataFrame(data)

# i) Print total players per team
print("Total players per team:")
print(df['Team'].value_counts())

# ii) Find player who had highest BidPrice from each team
print("\nPlayer with highest BidPrice from each team:")
print(df.loc[df.groupby('Team')['BidPrice'].idxmax(),['Team', 'Player', 'BidPrice']])

# iii) Find average runs of each team
print("\nAverage runs of each team:")
print(df.groupby('Team')['Runs'].mean())

# iv) Sort all players according to BidPrice
print("\nPlayers sorted by BidPrice:")
print(df.sort_values('BidPrice', ascending=False)[['Player', 'BidPrice']])