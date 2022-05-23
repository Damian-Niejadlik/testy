# some_list = [2, 4, 1, 6, 3, 5, ]
# schema = [4, 3, 6, 1, 2, 5, ]

a = [3015, 4728, 4802, 4361, 135, 4444, 4313, 1413, 4581, 546]
b = [4444, 135, 546, 3015, 4802, 4581, 4728, 1413, 4361, 4313]


def sort_by_schema(some_list, schema):
    index = 0
    power = 0

    numbers_in_right_position = []

    for i in some_list:
        if some_list.index(i) == schema.index(i):
            numbers_in_right_position.append(i)

    while some_list != schema:
        if some_list[index] not in numbers_in_right_position:
            element = some_list[index]
            position_of_element = some_list.index(element)
            right_position_of_element = schema.index(element)
            if some_list[right_position_of_element] == schema[position_of_element]:
                some_list[right_position_of_element], some_list[position_of_element] = some_list[position_of_element],\
                                                                                       some_list[right_position_of_element]
                power += some_list[right_position_of_element] + some_list[position_of_element]
                numbers_in_right_position.extend([some_list[right_position_of_element], some_list[position_of_element]])
            elif some_list[right_position_of_element] != schema[position_of_element]:
                some_list[right_position_of_element], some_list[position_of_element] = some_list[position_of_element], \
                                                                                       some_list[right_position_of_element]
                power += some_list[right_position_of_element] + some_list[position_of_element]
                numbers_in_right_position.append(some_list[right_position_of_element])
            else:
                index = 0
        else:
            index += 1
    return some_list, power


print(sort_by_schema(a, b))
