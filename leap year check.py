def leap_year(year):
    if(year%400==0 or year%4==0):
        print("its a leap year")
        return
    else:
        print("not a leap yaear")
        return
year=int(input("enter year:-"))
leap_year