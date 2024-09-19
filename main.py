import pandas as pd
import list_helper as lh

vote_dict = {
    "2222": ["A", "B", "C"],
    "3333": ["C", "A", "B"],
    "4444": ["A", "C", "B"],
    "5555": ["A", "B", "C"],
    "6666": ["B", "A", "C"],
    "7777": ["B", "A", "C"],
}

#calculate first position voting
#eliminate last candidate
#re-shuffle dicts, moving everyone 1 up

df_votes = pd.DataFrame.from_dict(vote_dict, orient='index')

all_counts = dict(df_votes[0].value_counts())

#print(df_votes)
#print(all_counts)
last_candidate = list(all_counts.keys())[-1]

print(f"The last candidate is {last_candidate}, removing them from the vote.")

for voter, ballot in vote_dict.items():
    vote_dict[voter] = lh.shift_all_items_once(ballot, last_candidate)

print("### Second Turn ###")
print(vote_dict)