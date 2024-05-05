import timeit

numbers = [170, 151, 100, 16, 193, 9, 37, 102, 50, 181,
           154, 2, 129, 125, 57, 14, 62, 91, 71, 148,
           29, 145, 36, 199, 88, 140, 115, 168, 172, 59,
           78, 15, 135, 134, 70, 93, 189, 3, 106, 124,
           184, 4, 82, 69, 26, 6, 168, 114, 16, 117,
           88, 193, 72, 167, 99, 8, 195, 183, 17, 172,
           99, 180, 104, 177, 70, 156, 22, 86, 36, 7,
           155, 50, 14, 192, 158, 191, 97, 44, 16, 148,
           186, 184, 97, 133, 52, 168, 10, 72, 97, 54,
           35, 92, 144, 170, 146, 11, 5, 87, 40, 114,
           135, 153, 112, 111, 129, 8, 73, 56, 177, 18,
           169, 109, 70, 62, 194, 70, 138, 191, 125, 69,
           6, 146, 191, 135, 158, 120, 14, 48, 133, 71,
           153, 97, 31, 106, 14, 105, 78, 97, 116, 32,
           28, 119, 31, 1, 54, 197, 91, 53, 33, 90,
           160, 3, 110, 123, 160, 50, 27, 150, 49, 76,
           157, 43, 173, 118, 71, 167, 103, 186, 132, 5,
           55, 99, 104, 24, 63, 90, 115, 158, 52, 91,
           164, 189, 100, 176, 49, 52, 69, 2, 104, 82,
           120, 25, 107, 25, 121, 63, 194, 20, 29, 39,
           172, 28, 53, 116, 68, 31, 96, 18, 18, 103,
           11, 97, 20, 22, 12, 42, 34, 26, 21, 139,
           38, 72, 101, 129, 13, 5, 185, 186, 155, 38,
           70, 5, 65, 191, 86, 129, 39, 38, 19, 84,
           80, 50, 176, 68, 98, 13, 157, 42, 47, 105,
           104, 19, 66, 183, 19, 122, 164, 19, 43, 36,
           26, 176, 79, 70, 48, 41, 5, 86, 148, 10]

words = ["banana", "apple", "orange", "grape", "pear", "pineapple", "watermelon", "kiwi", "strawberry", "blueberry",
         "peach", "mango", "lemon", "lime", "cherry", "avocado", "coconut", "pomegranate", "plum", "raspberry",
         "apricot", "blackberry", "fig", "cranberry", "nectarine", "melon", "tangerine", "guava", "grapefruit",
         "passionfruit", "dragonfruit", "papaya", "lychee", "date", "kumquat", "persimmon", "boysenberry",
         "cantaloupe", "honeydew", "starfruit", "kiwifruit", "mulberry", "rhubarb", "elderberry", "plantain",
         "quince", "gooseberry", "soursop", "tamarillo", "tamarind", "durian", "ackee", "breadfruit", "cherimoya",
         "feijoa", "longan", "rambutan", "ugli fruit", "jambul", "sapote", "calamondin", "carambola", "salak",
         "surinam cherry", "maracuja", "langsat", "cupuaçu", "santol", "pawpaw", "guanabana", "mangosteen",
         "jabuticaba", "mamey sapote", "cocoa bean", "bilimbi", "ackee", "tamarillo", "kumquat", "kumara", "manzano",
         "pitahaya", "pomelo", "satsuma", "ugli fruit", "yuzu", "clementine", "bergamot", "blood orange", "tangelo",
         "citron", "finger lime", "limequat", "mandarin", "tangor", "tardivo", "uvaia", "physalis", "sugar apple",
         "caimito", "custard apple", "granadilla", "jaboticaba", "soursop", "tamarillo"]

unsorted_tuples = [
    (3, 7),
    (1, 9),
    (5, 2),
    (8, 4),
    (6, 3),
    (2, 8),
    (4, 6),
    (9, 1),
    (7, 5),
    (10, 0),
    (13, 17),
    (11, 19),
    (15, 12),
    (18, 14),
    (16, 13),
    (12, 18),
    (14, 16),
    (19, 11),
    (17, 15),
    (20, 10)
]

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

execution_time = timeit.timeit(lambda: insertion_sort(numbers), number=1000)
print("Execution time for insertion sort (numbers):", execution_time)
execution_time = timeit.timeit(lambda: merge_sort(numbers), number=1000)
print("Execution time for merge sort (numbers):", execution_time)
execution_time = timeit.timeit(lambda: numbers.sort(), number=1000)
print("Execution time for Timsort (numbers):", execution_time)

execution_time = timeit.timeit(lambda: insertion_sort(words), number=1000)
print("Execution time for insertion sort (words):", execution_time)
execution_time = timeit.timeit(lambda: merge_sort(words), number=1000)
print("Execution time for merge sort (words):", execution_time)
execution_time = timeit.timeit(lambda: words.sort(), number=1000)
print("Execution time for Timsort sort (words):", execution_time)

execution_time = timeit.timeit(lambda: insertion_sort(unsorted_tuples), number=1000)
print("Execution time for insertion sort (unsorted tuples):", execution_time)
execution_time = timeit.timeit(lambda: merge_sort(unsorted_tuples), number=1000)
print("Execution time for merge sort (unsorted tuples):", execution_time)
execution_time = timeit.timeit(lambda: unsorted_tuples.sort(), number=1000)
print("Execution time for Timsort sort (unsorted_tuples):", execution_time)
