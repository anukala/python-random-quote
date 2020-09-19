import random

def test():
  print("Keep it logically awesome.")

  with open("quotes.txt","a+") as f:
     f.write("Adding new quote")
     f.seek(0)
     quotes = [x.strip() for x in f.readlines()]
  
  last = len(quotes)-1
  rand = random.randint(0, last)
  rand1 = random.randint(0, last)
  rand2 = random.randint(0, last) 
  print(quotes[rand]+','+ quotes[rand1]+','+ quotes[rand2])

if __name__== "__main__":
  test()
