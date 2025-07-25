input = ["a", "b", "c", "d"]


def split_into_chunks(input_list):
    return [input_list[i:i+3] for i in range(0, len(input_list), 3)]


print(split_into_chunks(input))
