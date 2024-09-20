import pandas as pd
import list_helpers as lh
import dict_helpers as dh
import copy
import csv

def run_instant_runoff(results_path: str, 
                       print_turns: bool, 
                       print_audit: bool,
                       print_choice_stats: bool 
                    ):
    vote_dict = {}

    with open(results_path, newline='') as csvfile:
        votes = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in votes:
            if len(row) == 0:
                continue
            vote_dict[row[0]] = row[1:]

    turn_counter = 1

    all_rounds_audit = {}

    total_ballots = len(vote_dict)

    #calculate first position voting
    #eliminate last candidate
    #re-shuffle dicts, moving everyone 1 up

    if print_choice_stats:
        electoral_stats = pd.DataFrame.from_dict(vote_dict, orient='index')
        choice_counter = 1

        for column in electoral_stats:
            if choice_counter != 1:
                continue

            all_index = electoral_stats[column].value_counts().index.to_list()
            all_votes = electoral_stats[column].value_counts().to_list()
            
            all_votes_perc = list(map(lambda x: round(x / total_ballots * 100,2), all_votes))

            print(f"Choice #{choice_counter} perc:")

            for i in range(len(all_index)):
                
                print(f"{all_index[i]}: {all_votes_perc[i]}%")

            
            choice_counter += 1


    if print_turns:
        print(f"We have a total of {total_ballots} expressed ballots")

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
        for current_round in all_rounds_audit.items():
            print(current_round)

run_instant_runoff(results_path = r'./data/votes.csv',
                   print_turns = True, 
                   print_audit = False,
                   print_choice_stats = True
                )