import os

def clear_console():
    os.system('cls')

clear_console()

bids_list = {}
other_users = ""
value_paid = 0
winner_name = ""

while not (other_users == "no"):
    name = input('Enter your name:')
    bid = int(input('Bid Amount:'))
    bids_list[name] = bid
    other_users = input("Is there others users who want to bid ? type yes or no")
    clear_console()

if(other_users):
    for bidder in bids_list:
        if (bids_list[bidder] > value_paid):
            value_paid = bids_list[bidder]
            winner_name = bidder

print(f'The winner is {winner_name} with the bid of {value_paid}')


