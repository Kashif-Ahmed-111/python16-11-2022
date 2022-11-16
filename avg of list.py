a = [1,2,3,6,9,2,5,3,98,68]
b=[212,56,36,96,25]
c=[555,2999,3666,2559,78]
def length_of_list(z):
    for i in z:
        length=len(z)
    return length
print(length_of_list(c))
def sum_of_element(y):
    sum1=0
    for i in y:
        sum1 = sum1+int(i)
    return sum1
print(sum_of_element(c))
def avg(x):
    for i in x:
        average=(sum_of_element(x)/length_of_list(x))
        return average
print(avg(c))
