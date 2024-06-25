
def reverse_only_letters(s):
  char_positions = []
  others = []
  final_str = []

  for index, val in enumerate(s):
    if val.isalpha():
      char_positions.append(index)
    else:
      others.append(index)

  flipped = char_positions[::-1]
  print(flipped)
  print(others)
  
 





s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)

    
