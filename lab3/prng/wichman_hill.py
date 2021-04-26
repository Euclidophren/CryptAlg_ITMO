def wichman_hill(seed_list, list_length):
    seed1 = seed_list[0]
    seed2 = seed_list[1]
    seed3 = seed_list[2]

    num_list = []
    for i in range(list_length):
        seed1 = 171 * seed1 % 30269
        seed2 = 172 * seed2 % 30307
        seed3 = 170 * seed3 % 30323

        num_list.append((float(seed1) / 30269.0 + float(seed2) / 30307.0 + float(seed3) / 30323.0) % 1.0)
    return num_list
