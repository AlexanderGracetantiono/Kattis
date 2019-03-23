def jan(d):
    d=d%7
    if d==0:
        return "Wednesday"
    elif d==1:
        return "Thursday"
    elif d==2:
        return "Friday"
    elif d==3:
        return "Saturday"
    elif d==4:
        return "Sunday"
    elif d==5:
        return "Monday"
    elif d==6:
        return "Tuesday"

def feb(d):
    d=d%7
    if d==4:
        return "Wednesday"
    elif d==5:
        return "Thursday"
    elif d==6:
        return "Friday"
    elif d==0:
        return "Saturday"
    elif d==1:
        return "Sunday"
    elif d==2:
        return "Monday"
    elif d==3:
        return "Tuesday"
 
def mar(d):
    d=d%7
    if d==4:
        return "Wednesday"
    elif d==5:
        return "Thursday"
    elif d==6:
        return "Friday"
    elif d==0:
        return "Saturday"
    elif d==1:
        return "Sunday"
    elif d==2:
        return "Monday"
    elif d==3:
        return "Tuesday"

def apr(d):
    d=d%7
    if d==1:
        return "Wednesday"
    elif d==2:
        return "Thursday"
    elif d==3:
        return "Friday"
    elif d==4:
        return "Saturday"
    elif d==5:
        return "Sunday"
    elif d==6:
        return "Monday"
    elif d==0:
        return "Tuesday"

def jul(d):
    d=d%7
    if d==1:
        return "Wednesday"
    elif d==2:
        return "Thursday"
    elif d==3:
        return "Friday"
    elif d==4:
        return "Saturday"
    elif d==5:
        return "Sunday"
    elif d==6:
        return "Monday"
    elif d==0:
        return "Tuesday"

def may(d):
    d=d%7
    if d==6:
        return "Wednesday"
    elif d==0:
        return "Thursday"
    elif d==1:
        return "Friday"
    elif d==2:
        return "Saturday"
    elif d==3:
        return "Sunday"
    elif d==4:
        return "Monday"
    elif d==5:
        return "Tuesday"

def june(d):
    d=d%7
    if d==3:
        return "Wednesday"
    elif d==4:
        return "Thursday"
    elif d==5:
        return "Friday"
    elif d==6:
        return "Saturday"
    elif d==0:
        return "Sunday"
    elif d==1:
        return "Monday"
    elif d==2:
        return "Tuesday"

def aug(d):
    d=d%7
    if d==5:
        return "Wednesday"
    elif d==6:
        return "Thursday"
    elif d==0:
        return "Friday"
    elif d==1:
        return "Saturday"
    elif d==2:
        return "Sunday"
    elif d==3:
        return "Monday"
    elif d==4:
        return "Tuesday"

def sep(d):
    d=d%7
    if d==2:
        return "Wednesday"
    elif d==3:
        return "Thursday"
    elif d==4:
        return "Friday"
    elif d==5:
        return "Saturday"
    elif d==6:
        return "Sunday"
    elif d==0:
        return "Monday"
    elif d==1:
        return "Tuesday"

def oct(d):
    d=d%7
    if d==0:
        return "Wednesday"
    elif d==1:
        return "Thursday"
    elif d==2:
        return "Friday"
    elif d==3:
        return "Saturday"
    elif d==4:
        return "Sunday"
    elif d==5:
        return "Monday"
    elif d==6:
        return "Tuesday"

def nov(d):
    d=d%7
    if d==4:
        return "Wednesday"
    elif d==5:
        return "Thursday"
    elif d==6:
        return "Friday"
    elif d==0:
        return "Saturday"
    elif d==1:
        return "Sunday"
    elif d==2:
        return "Monday"
    elif d==3:
        return "Tuesday"

def dec(d):
    d=d%7
    if d==2:
        return "Wednesday"
    elif d==3:
        return "Thursday"
    elif d==4:
        return "Friday"
    elif d==5:
        return "Saturday"
    elif d==6:
        return "Sunday"
    elif d==0:
        return "Monday"
    elif d==1:
        return "Tuesday"

# “Monday”, “Tuesday”, “Wednesday”, “Thursday”, “Friday”, “Saturday” or “Sunday”.
x=str(input()).split()
date=int(x[0])
month=int(x[1])
if month==1:
    print(jan(date))
elif month==2:
    print(feb(date))
elif month==3:
    print(mar(date))
elif month==4:
    print(apr(date))
elif month==5:
    print(may(date))
elif month==6:
    print(june(date))
elif month==7:
    print(jul(date))
elif month==8:
    print(aug(date))
elif month==9:
    print(sep(date))
elif month==10:
    print(oct(date))
elif month==11:
    print(nov(date))
elif month==12:
    print(dec(date))