def is_leap(yr):
    if ((yr%4==0 and yr%100!=0) or (yr%400==0)):
        return True
    else:
        return False
year=int(input("Enter a year"))
print(is_leap(year))