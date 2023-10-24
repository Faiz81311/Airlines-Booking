import csv

f=open("Airline.csv","w")


print("Would You like To Take A One Way Ticket Or A Round Way Ticket ")

print("Press [1] For A One Way Ticket")
print(" Press [2] For A Round Way Ticket")
n=input("Enter Choice : ")

if n == '1':
    fields=["Departure","Date Of Departure","Destination","Class","Concessionary Passenger"]
    l=[]

    dep = input("Where Would You Like To Depart From : ")
    dep_date = input("When Would Like To Depart (Day-Date-Year) : ")
    des = input("Where Is Your Destination : ")
    cl = input("Whcih Class Would You Like (Economy Class,Bussiness Class or First Class) : ")
    conpas = input("Are You A Concessionary Passenger (Yes/No) : ")

    l.append(dep)
    l.append(dep_date)
    l.append(des)
    l.append(cl)
    l.append(conpas)

    x = csv.writer(f)
    x.writerow(fields)
    x.writerow(l)
    

elif n == '2':
    fields=["Departure","Date Of Departure","Destination","Date Of Return","Class","Concessionary Passenger"]
    l=[]

    dep = input("Where Would You Like To Depart From : ")
    dep_date = input("When Would Like To Depart (Day-Date-Year) : ")
    des = input("Where Is Your Destination : ")
    ret = input("When Would You Like To Return (Day-Date-Year) : ")
    cl = input("Whcih Class Would You Like (Economy Class,Bussiness Class or First Class) : ")
    conpas = input("Are You A Concessionary Passenger (Yes/No) : ")

    l.append(dep)
    l.append(dep_date)
    l.append(des)
    l.append(ret)
    l.append(cl)
    l.append(conpas)

    x = csv.writer(f)
    x.writerow(fields)
    x.writerow(l)
    
else:
    print("Enter Valid Choice")











