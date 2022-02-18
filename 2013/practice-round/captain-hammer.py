from decimal import Decimal
from math import asin, pi, pow

n_test_cases = int(input())
for n_test_case in range(1, n_test_cases + 1):
	v, d = map(Decimal, input().split(" "))
	theta = 90 * asin(Decimal(9.8) * d / Decimal(pow(v, 2))) / pi
	print(f"Case #{n_test_case}: {theta:7f}")
