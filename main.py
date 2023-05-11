import string
import time
from collections import Counter


start = time.time()
letters = list(string.ascii_lowercase)
sum_count = 0
with open('text.txt', mode='r') as f:
    read_file = f.read().replace(' ', '')
    result = Counter(read_file)
    for count in letters:
        sum_count += result[count]
    for count_letter in letters:
        try:
            print(count_letter, '-', round(result[count_letter] * 100 / sum_count, 2), '%')
        except ZeroDivisionError:
            print(result[count_letter], '-', '0%')
stop = time.time()
print('Время работы программы:', round(stop - start, 3))
