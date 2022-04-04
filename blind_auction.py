from art import logo
print(logo)
dic = {}
bidding = False
def highest(bidders):
  highbid = 0
  for bidder in dic:
    new = dic[bidder]
    if new > highbid:
      highbid = new
      winner = bidder
  print(f"The new winner is {winner}")
       
while not bidding:
  name = input("what is your name?\n")
  bid = int(input("How much do you want to bid?\n$"))
  dic[name] = bid
  user = input("Is there anyother user who wants to play? 'Yes' or 'No'").lower()
  
  if user == "no":
    bidding = True
    highest(bidders =dic)
  
  
  
  
   
    
    
  
