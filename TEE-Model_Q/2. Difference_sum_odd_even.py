def check(ip_no):
    if (ip_no % 11 == 0):
        print("The difference between sum of odd digits and even digits is zero!")
    else:
        print("The difference between sum of odd digits and even digits is not zero!")


ip_no = int(input("Enter the number: "))
check(ip_no)
