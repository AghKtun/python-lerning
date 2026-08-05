# Sorting

n_1  = int(input())
n_2 = int(input())
n_3 = int(input())

diff_max = max(n_1, n_2, n_3)
diff_min = min(n_1, n_2, n_3)
diff_middle = (n_1 + n_2 + n_3) - diff_max - diff_min

print(diff_max, diff_middle, diff_min, sep='\n')
