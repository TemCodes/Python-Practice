def solution(stores, houses):
    distance = []
    for i in range(0,len(houses)):
        closest = abs(houses[i] - stores[0])
        val = stores[0]
        for j in range(0,len(stores)):
            diff = abs(houses[i] - stores[j])
            if (diff < closest):
                val = stores[j]
                closest = diff
        distance.append(val)
    return(distance)


print(solution([1,3,7,11,20,30,50], [1,2,3,5,8,9,0,15,16,25,40]))
