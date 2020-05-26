box = [int(x) for x in input().split()]
capacity = int(input())
sum = 0
counter_rack = 1
rack = []

while box:
    current_clothe = box.pop()

    if sum < capacity:
        sum += current_clothe
        rack.append(current_clothe)
    if sum == capacity:
        counter_rack +=1
        sum = 0
        rack.clear()
    if sum > capacity:
        counter_rack +=1
        sum = sum - capacity
        rack.clear()
        rack.append(sum)

if rack:
    counter_rack += 1

print(counter_rack)