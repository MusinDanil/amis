"""
Create dataset from data in orders.csv


"""


def list_to_dataset(list):
    # takes list, returns dict with first elem of list as a key.
    result = {}
    for elem in list:
        if not elem[0] in result.keys():
            result[elem[0]] = []
        result[elem[0]].append(elem[1::])
    return result


temp_list = []
with open('orders.csv') as file:
    file.readline()
    for line in file:
        temp_list.append([word.strip() for word in line.split(',')])

temp_dict = list_to_dataset(temp_list)
for key in temp_dict.keys():
    temp_dict[key] = list_to_dataset(temp_dict[key])
    for ke in temp_dict[key].keys():
        temp_dict[key][ke] = list_to_dataset(temp_dict[key][ke])
print(temp_dict)
