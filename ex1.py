
# q1
def is_leap_year(year):
    return (year%400 == 0) or (year%4 == 0 and year%100 != 0)


years = [800, 4, 100]

for year in years:
    if is_leap_year(year):
        print year, ' is leap year'

# q2 1)
print 145%23


# q2 2)
import math
print math.sin(0.5), ' and ', math.cos(0.5)

# q3
def is_prime(num):
    for i in range(2, num):
        if num%i == 0:
            return False
    else:
        return True


for num in range(1, 100):
    if is_prime(num):
        print num, ' is prime'


