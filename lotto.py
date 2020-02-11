import random

def get_lotto():
  lotto_range = range(1,47)
  lotto_nums = random.sample(lotto_range,6)
  return lotto_nums

print(get_lotto())