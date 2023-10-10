lst=[2,3,4,5,6]
squares=[n**2 for n in lst]
print(squares)

cube=[n**3 for n in lst]
print(cube)

add_two=[n+2 for n in lst]
print(add_two)

#greater than five
gt_five=[n for n in lst if n>5]
print(gt_five)

even=[n for n in lst if n%2==0]
print(even)

odd=[n for n in lst if n%2!=0]
print(odd)

years=[y for y in range(1800,2026)]
print(years)

#find century years
years=[y for y in range(1800,2026)]
century_yr=[y for y in years if y%100==0]
print(century_yr)

non_centuryyr=[y for y in years if y%100!=0]
print(non_centuryyr)