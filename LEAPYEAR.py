year= int(input("enter the year :"))
if year%4==0 and year%100==0 and year%400==0:
    print("its a leapyear")

else:
    print("its not a leap year")