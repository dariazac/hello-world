# Lists
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
for i in my_list:
    print i


def sqr(a_list):
    sq_list = [num * num for num in a_list]
    print sq_list


sqr(my_list)

# Tuples
my_tup = (1, 2, 3, 4, 5, 6, 7, 8)
# for i in my_tup:
#     print i

# Dict
my_dict = {'name': 'Bronx', 'age': '2', 'job': "Bill's Dog"}  # hash table
# for key, val in my_dict.iteritems():
#     print "My {} is {}".format(key, val)

# Set
my_set = {10, 20, 30, 40, 50, 30, 10, 20}
# for i in my_set:
#     print i
