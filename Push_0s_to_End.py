def reshape_array(array):
  n = len(array)
  count = 0

  for i in range(n):
    if array[i] != 0:
      array[count] = array[i]
      count+=1

  while count < n:
    array[count] = 0
    count +=1
  return array



print(reshape_array([2,1,0,1,0,0,2]))

print(reshape_array([2,1,0,1,0,0,2]) == [2,1,1,2,0,0,0])
