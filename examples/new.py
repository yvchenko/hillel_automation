import statistics
#
# data = [1, 2, 3, 4, 5, 6, 7]
# data_1 = [1, 12, 3, 22, 231, 43, 56]
#
# sum_data = sum(data) / len(data)
#
# print(sum_data)
#
# sum_data1 = statistics.mean(data)
#
# print(sum_data1)


def get_mean(data: list):
    print(sum(data)/len(data))
    print(statistics.mean(data))
    print(statistics.geometric_mean(data))


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [3, 6, 23, 11, 22, 61, 1083]
b = sorted(b)
print('=-=-', b)
c = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9]
# d = []

# get_mean(a)
# get_mean(b)
# get_mean(c)


def geom_mean(lst):
    sorted_list = sorted(lst)
    length = len(sorted_list)
    if length % 2 == 0:
        a1 = length/2
        a2 = a1 + 1
        return (sorted_list[int(a1)] + sorted_list[int(a2)])/2
    return sorted_list[round(length/2)]


print(geom_mean(b))