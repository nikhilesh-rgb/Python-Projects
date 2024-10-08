logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = " "

    max(bidding_record)

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if int(bid_amount) > int(highest_bid):
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with bid of ₹{highest_bid}")


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name? ")
    price = input("What is your bid?: ₹")
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if should_continue == "no":
        continue_bidding = False
        highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)