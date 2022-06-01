def is_it_good(foods: list):
  if foods:
    for food in foods:
      print("this is good "+ food)
  else:
    print("wdym")
  
if __name__ == "__main__":
  foods = ['pizza','pasta','fish']
  is_it_good(food)
