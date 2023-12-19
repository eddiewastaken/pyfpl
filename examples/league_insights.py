from ..pyfpl import PyFPL
import pandas as pd

pd.set_option('display.max_columns', None)

## Fetching to Dataframe
league_overview = PyFPL.League.get_overview("$YOUR_LEAGUE_ID_HERE")
results_data = []
for manager in league_overview["standings"]["results"]:
    results_data.append([manager['player_name'],
                         manager['entry_name'],
                         manager['event_total'],
                         manager['total'],
                         manager['last_rank'],
                         manager['rank']])

results_df = pd.DataFrame(results_data, columns=['Manager', 'Team', 'GW Pts', 'Total Pts', 'Prev Pos', 'Pos'])


## Data Processing
# Top GW scorers
top_ten_gw_scorers = results_df.sort_values(['GW Pts'], ascending=False)[:10][['Manager', 'Team', 'GW Pts']]

# Current standings
results_df['Pos Diff'] = results_df['Prev Pos'] - results_df['Pos']
results_df['Pos Movement'] = results_df.apply(lambda row: '↑' if row['Prev Pos'] - row['Pos'] > 0 else ('-' if row['Prev Pos'] - row['Pos'] == 0 else '↓'), axis=1)
results_df['Pos Diff'] = abs(results_df['Prev Pos'] - results_df['Pos']).astype(str)
results_df['Pos Diff'] = results_df['Pos Movement'] + " " + results_df['Pos Diff']
top_ten_overall = results_df.sort_values(['Pos'])[:10][['Manager', 'Team', 'Pos', 'Pos Diff', 'Total Pts']]

# Output
print(top_ten_gw_scorers.to_markdown(numalign="center", stralign="center"), end='\n\n')
print(top_ten_overall.to_markdown(numalign="center", stralign="center"))
