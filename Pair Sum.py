#Given an interger array, output all the unique pairs that sum up to a specific value k.

# pair_sum([1,3,2,2],4)
# would return pairs:

# (1,3)
# (2,2)

def pair_sum(array, k):
    if len(array) < 2:
        return print('Too small a pool')

    seen = set()
    output= set()

    for num in array:
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target ), max(num, target)))

    print('\n'.join(map(str, list(output))))

pair_sum([1,2,3,4,5,6,7,8,9],17)
