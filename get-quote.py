import random
def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt", "a")
  f.write("PIERWSZY DDD \n")
  f.write("DRUGI DDD \n")
  f.write("TRZECI DDD \n")
  f.close()
  
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()  

  last = len(quotes)-1
  rnd = random.randint(0,last)
  rnd2 = random.randint(0,last)
  print(quotes[rnd], quotes[rnd2])

if __name__== "__main__":
  primary()
