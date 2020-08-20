num = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]

the_highest = 0
the_index = 0
the_higgest_sum_of_list_in_num = 0
for the_list in num:
    the_sum = sum(the_list)
    if the_highest <= the_sum:
        the_highest = the_sum
        the_higgest_sum_of_list_in_num = the_index
    the_index += 1

print(num[the_higgest_sum_of_list_in_num])