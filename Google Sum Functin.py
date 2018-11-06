def summ(arr, val):
  for i in range(0,len(arr)):
    for k in range(i+1, len(arr)):
      if (arr[i] + arr[k] == val):
        return(True)
  return(False)


def summ2(arr, val):
  for i in arr:
    if val-arr[i] in arr:
      return(True)
  return(False)




print(summ([1,2,3,4,5,6,7,8,9], 15))
print(summ2([1,2,3,4,5,6,7,8,9], 15))
