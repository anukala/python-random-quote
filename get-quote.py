import random

def test():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  last = 13
  rand = random.randint(0, last)
  print(quotes[rand])

if __name__== "__main__":
  test()
