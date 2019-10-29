import random
import time
ism_file = open("isms.txt", "r")
for line in  ism_file:
  ism_array = ism_file.read().split()  
ism_file.close()


tweet_array = []
for ism in ism_array:
  ing = ism[:-3] + "ing"
  str = f"{ism} becomes {ing}"
  tweet_array.append(str)

def grab_random():
  index = random.randint(0, len(tweet_array) - 1)
  send = tweet_array.pop(index)
  # print(len(tweet_array))
  # print(send)
  return send

# for i in range(0, len(tweet_array) - 1):
#   grab_random() 
  
def printer(): 
    print("TIME\n") 
  
while True:
  time.sleep(86400)



