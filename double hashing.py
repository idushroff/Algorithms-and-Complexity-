

def double_hashing(keys, hashtable_size, double_hash_value):
    hashtable_list = [None] * hashtable_size
    for i in range(len(keys)):
        hashkey = keys[i] % hashtable_size
        if hashtable_list[hashkey] is None:
            hashtable_list[hashkey] = keys[i]
        else:
            new_hashkey = hashkey
            while hashtable_list[new_hashkey] is not None:
                steps = keys[i] % double_hash_value
                new_hashkey = (new_hashkey + steps) % hashtable_size
            hashtable_list[new_hashkey] = keys[i]
    return hashtable_list


values = [11, 20, 24, 7, 9, 21]
print(double_hashing(values, 13, 5))



# find the hash values for all values in the list
hash_vals = []
for val in values:
    hash_vals.append(val % 13)

# find the double hash for all values in list
double_hash_vals = []
for val in values:
    double_hash_vals.append(val % 5)

print(hash_vals)
print(double_hash_vals)