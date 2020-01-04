# O(1), Arithmetic Progression
maxnum = 999
total = (1/2)*(int(maxnum/3))*(2*3+((int(maxnum/3))-1)*3) + \
    (1/2)*(int(maxnum/5))*(2*5+((int(maxnum/5))-1)*5) - \
    (1/2)*(int(maxnum/15))*(2*15+((int(maxnum/15))-1)*15)

print(total)
