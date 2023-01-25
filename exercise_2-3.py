with open("data.txt", 'r') as f:
    data = f.readlines()

items_list = []

for line in data:
    stripped_line = line.strip().split(",")
    cost = float(stripped_line[1])
    name = stripped_line[0]
    item_tuple = (name, cost)
    items_list.append(item_tuple)

def cost_sort(item):
    return item[1]

items_list.sort(key=cost_sort, reverse=True)

print(f"'{items_list[0][0]}' costs the most amount of money.")

items_list.sort()
# Exercise 3
# I made this so much harder than it had to be, probably.
# Either way, my solution works but I hate how it looks.

amt_times_appeared = []
counter = 1
amt_times_appeared = [(i[0], counter) for i in items_list]

for item in amt_times_appeared:
    product = (item[0], item[1])
    counter = amt_times_appeared.count(product)
    for x in range(counter):
        amt_times_appeared.remove(product)
    product = (item[0], counter)
    amt_times_appeared.append(product)
                
amt_times_appeared.sort()

def length_sort(item):
    return len(item[0])

amt_times_appeared.sort(key=length_sort, reverse=True)

# Right justified with a width of at least 7: nice.
width = len(amt_times_appeared[0]) + 7

amt_times_appeared.sort()
for item in amt_times_appeared:
    print(f"{item[0]}".rjust(width) + f"{item[1]}".rjust(width))