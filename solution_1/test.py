from tqdm import tqdm
import time


def prepare_data(file: str):
    with open(f"zadanie_B\{file}", 'r') as f:
        data = f.readlines()
        schema = data[3].split()
        elephant_number = data[2].split()
        elephant_weight = data[1].split()
        elephant_dict = {elephant_number[index]: elephant_weight[index] for index in range(len(elephant_number))}
    return elephant_number, schema, elephant_dict


# print(prepare_data("slo1.in"))
time_start = time.time()


def sort_by_schema(elephant_number, schema, elephant_dict):
    power = 0
    numbers_in_wrong_position = []
    print("Your list with elephants is loading...")
    for i in tqdm(elephant_number):
        if elephant_number.index(i) != schema.index(i):
            numbers_in_wrong_position.append(i)
    print("\nPlease wait, your list is sorting now...\n")

    while elephant_number != schema:
        for element in numbers_in_wrong_position:
            position_of_element = elephant_number.index(element)
            right_position_of_element = schema.index(element)
            if elephant_number[right_position_of_element] == schema[position_of_element]:
                elephant_number[right_position_of_element], elephant_number[position_of_element] = \
                    elephant_number[position_of_element], elephant_number[right_position_of_element]
                power += int(elephant_dict.get(elephant_number[right_position_of_element])) + \
                         int(elephant_dict.get(elephant_number[position_of_element]))
                numbers_in_wrong_position.pop(
                    numbers_in_wrong_position.index(elephant_number[right_position_of_element])
                )
                numbers_in_wrong_position.pop(numbers_in_wrong_position.index(elephant_number[position_of_element]))
            elif elephant_number[right_position_of_element] != schema[position_of_element]:
                elephant_number[right_position_of_element], elephant_number[position_of_element] = \
                    elephant_number[position_of_element], elephant_number[right_position_of_element]
                power += int(elephant_dict.get(elephant_number[right_position_of_element])) + \
                         int(elephant_dict.get(elephant_number[position_of_element]))
                numbers_in_wrong_position.pop(
                    numbers_in_wrong_position.index(elephant_number[right_position_of_element])
                )
        # print(len(numbers_in_wrong_position))
    return power


a, b, c = prepare_data("slo8a.in")
print(f"Power needed to move elephant: {sort_by_schema(a, b, c)}\n")

time_end = time.time()

print(f"Operation took {time_end - time_start:.2f} seconds\n")
