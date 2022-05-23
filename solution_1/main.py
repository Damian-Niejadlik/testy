def prepare_data(file: str):
    with open(f"zadanie_B\{file}", 'r') as f:
        data = f.readlines()
        schema = data[3].split()
        elephant_number = data[2].split()
        elephant_weight = data[1].split()
        elephant_dict = {elephant_number[index]: elephant_weight[index] for index in range(len(elephant_number))}
    return elephant_number, schema, elephant_dict


# print(prepare_data("slo1.in"))


def sort_by_schema(elephant_number, schema, elephant_dict):
    index = 0
    power = 0

    numbers_in_right_position = []

    for i in elephant_number:
        if elephant_number.index(i) == schema.index(i):
            numbers_in_right_position.append(i)

    while elephant_number != schema:
        if elephant_number[index] not in numbers_in_right_position:
            element = elephant_number[index]
            position_of_element = elephant_number.index(element)
            right_position_of_element = schema.index(element)
            if elephant_number[right_position_of_element] == schema[position_of_element]:
                elephant_number[right_position_of_element], elephant_number[position_of_element] = \
                    elephant_number[position_of_element], elephant_number[right_position_of_element]
                power += int(elephant_dict.get(elephant_number[right_position_of_element])) + \
                         int(elephant_dict.get(elephant_number[position_of_element]))
                numbers_in_right_position.extend([elephant_number[right_position_of_element],
                                                  elephant_number[position_of_element]])
            elif elephant_number[right_position_of_element] != schema[position_of_element]:
                elephant_number[right_position_of_element], elephant_number[position_of_element] =\
                    elephant_number[position_of_element], elephant_number[right_position_of_element]
                power += int(elephant_dict.get(elephant_number[right_position_of_element])) + \
                         int(elephant_dict.get(elephant_number[position_of_element]))
                numbers_in_right_position.append(elephant_number[right_position_of_element])
            else:
                index = 0
        else:
            index += 1
    return power


a, b, c = prepare_data("slo1.in")

print(sort_by_schema(a, b, c))
