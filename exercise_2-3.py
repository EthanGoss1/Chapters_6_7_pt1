with open("file_with_lines.txt", 'r') as f:
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

# Exercise 3
# I made this so much harder than it had to be, probably.
# Either way, my solution works but I hate how it looks.
amt_times_appeared = []
burn_list = []
active = True
while active:
    index = 0
    for item in items_list:
        counter = 0
        if item[0] == items_list[:][index][0]:
            counter += 1
            index += 1
        else:
            index += 1
        if [item[0], counter] not in burn_list:
            burn_list.append([item[0], counter])
        else:
            burn_list.remove([item[0], counter])
            burn_list.append([item[0], counter+1])
    active = False

amt_times_appeared = [(i[0], i[1]) for i in burn_list]

print(amt_times_appeared)
