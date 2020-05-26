box = [int(clothes_box) for clothes_box in input().split(" ")]
rack_capacity = int(input())

counter_racks = 1
sum_of_clothes = 0
while box:
    sum_of_clothes += box[-1]
    if sum_of_clothes > rack_capacity:
        sum_of_clothes = 0
        counter_racks += 1
        continue

    box.pop()

print(counter_racks)