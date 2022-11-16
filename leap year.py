def is_leap(year):
    if year%100!=0:
        if year%4==0:
            ans = True
        else:
            ans = False
    else:
        if year%4==0:
            if year%100==0:
                if year%400==0:
                    ans = True
                else:
                    ans = False
    return ans
    # Write your logic here

year = int(input())
print(is_leap(year))