some_list = ['asad', 'bunny', 'gaurav', 'sachin', 'asad', 'vinay', 'sachin']

duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))

print(duplicates)