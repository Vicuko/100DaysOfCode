from replit import clear
# HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
new_bidder = True
bids = dict()
highest_bid = {"name": None, "bid": 0}
while new_bidder:
    bidder_name = input("Please introduce the bidder's name: ")
    bid = int(input("Please introduce the bid: $"))
    bids[bidder_name] = bid
    if bid > highest_bid["bid"]:
        highest_bid["name"] = bidder_name
        highest_bid["bid"] = bid

    more_bidders = input("Are there any more bids? [yes/no] ").lower()
    if more_bidders == "no":
        new_bidder = False
    clear()

print(f"The highest bid is: {highest_bid['bid']} by {highest_bid['name']}")
print(bids)
