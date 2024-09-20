import pandas as pd
import list_helpers as lh
import dict_helpers as dh
import copy
import csv

def run_instant_runoff(print_turns: bool, print_audit: bool):
    vote_dict = {}

    with open(r'./data/votes.csv', newline='') as csvfile:
        votes = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in votes:
            if len(row) == 0:
                continue
            vote_dict[row[0]] = row[1:]

    turn_counter = 1

    all_rounds_audit = {}

    #calculate first position voting
    #eliminate last candidate
    #re-shuffle dicts, moving everyone 1 up

    while dh.find_max_length_sublist(vote_dict) > 1:

        all_rounds_audit[turn_counter] = copy.deepcopy(vote_dict)

        if print_turns:
            print(f"### Starting turn: {turn_counter} ###")

        df_votes = pd.DataFrame.from_dict(vote_dict, orient='index')

        all_counts = dict(df_votes[0].value_counts())

        if print_turns:
            print("All counts for current round")
            print(all_counts)
        
        last_candidate = list(all_counts.keys())[-1]

        if print_turns:
            print(f"The last candidate is {last_candidate}, removing them from the vote.")

        for voter, ballot in vote_dict.items():
            vote_dict[voter] = lh.shift_all_items_once(ballot, last_candidate)

        turn_counter += 1

    winning_candidate = list(all_counts.keys())[0]

    if print_turns:
        print(f"### The winning candidate is {winning_candidate}, congrats! ###")

    if print_audit:
        print("### This is the audit for every round ###")
        print(all_rounds_audit)

run_instant_runoff(print_turns = True, print_audit = False)