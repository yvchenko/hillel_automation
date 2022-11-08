# Згенерувати, за допомогою list comprehension, послідовність
# цілих чисел 0..N де будуть відсутні кожний  K-ий елемент
#
# N, K запитати у користувача
# K повинно бути менша за N (строго), дозволити ввод К більшого
# за N але відмасштабувати його до розмірів менших за N (%)
# from 1 to N-1
# підказка:
#  %= N  # compound assignment

def minimize(n, k):
    k = abs(n - k)
    if k > n:
        k = minimize(n, k)

    return k

n = None
k = None

while not n or not k:
    try:
        if not n:
            n = abs(int(input("Please fill N from 1 to ... : ")))
        if not k:
            k = abs(int(input("\n Please fill K : ")))
    except ValueError:
        print("Please enter a number")


if n >= 2 and k >= n:
    print("Found to be fixed!")
    print(minimize(n, k))
