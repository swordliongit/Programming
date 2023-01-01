key_list = ['key1', 'key3']

our_dict = {'key1': 1, 'key2': 2, 'key3': 3}


num_list = [1, 2, 3]

result = {item: our_dict[key]**2 for item, key in zip(num_list, our_dict)}


print(result)