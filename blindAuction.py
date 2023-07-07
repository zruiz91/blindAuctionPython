from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("Welcome to the secret auction program.")
bidders = []
name = input("What is your name? ")
bid = input("What is your bid? $")
highest_bid = 0
highest_bidder = ""
bidder = {
  "name": name,
  "bid": bid,
}
bidders.append(bidder)

more_bidders = input("Are there any more bidders? ").lower()

while more_bidders == "yes":
  clear()
  name = input("What is your name? ")
  bid = input("What is your bid? $")

  bidder = {
  "name": name,
  "bid": bid,
  }
  bidders.append(bidder)
  more_bidders = input("Are there any more bidders? ").lower()

for bidder in bidders:
  if int(bidder["bid"]) > int(highest_bid):
    highest_bid = bidder["bid"]
    highest_bidder = bidder["name"]



print(f"The winner was {highest_bidder} with a bid of ${highest_bid}")




