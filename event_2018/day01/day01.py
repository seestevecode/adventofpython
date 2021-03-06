import os
input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(input_path) as input_list:
    formatted_list = [int(line) for line in input_list]

# Part 1
print("Part 1:", sum(formatted_list))


# Part 2
def process_file(counter, counters):
    for line in formatted_list:
        counter += line
        if counter in counters:
            print("Part 2:", counter)
            exit()
        else:
            counters.append(counter)
    else:
        process_file(counter, counters)


process_file(0, [0])
