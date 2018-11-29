def compare_strings(string_1, string_2):
  string1= string_1.lower()
  string2= string_2.lower()
  length = min(len(string1), len(string2))

  for i in range(length):
    if string1[i] < string2[i]:
      return string1
    elif string1[i] > string2[i]:
        return string2
    i+=1
  if(len(string1)) == length:
    return string1
  else:
    return string2



print(compare_strings('award', 'away') == 'award')
print(compare_strings('FARTS', 'fart') == 'fart')
print(compare_strings('monster', 'anagram') == 'anagram')
