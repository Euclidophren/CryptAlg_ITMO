def middle_squares(seed, list_length):
    num_list = []
    for i in range(list_length):
        seed_length = len(str(seed))
        if seed_length % 2:
            seed_length += 1
            seed = str(int(seed)).zfill(seed_length)
        seed = str(int(seed) * int(seed)).zfill(2 * seed_length)
        half = int(seed_length / 2)
        seed = seed[half:(seed_length + half)]
        num_list.append(seed)
    return num_list
