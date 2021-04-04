# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

def monday():
    print("MONDAY")

def tuesday():
    print("TUESDAY")

def wednesday():
    print("WEDNESDAY")

def thursday():
    print("THURSDAY")

def friday():
    print("FRIDAY")
    
def saturday():
    print("SATURDAY")
    
def sunday():
    print("SUNDAY")
    
options = {0 : monday,
        1 : tuesday,
        2 : wednesday,
        3 : thursday,
        4 : friday,
        5 : saturday,
        6 : sunday,
}

n = str(input()) #08 05 2015 will return WEDNESDAY
month, day, year = n.split(" ")
day_num = calendar.weekday(int(year), int(month), int(day))
options[day_num]()

