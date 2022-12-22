from datetime import datetime
phonenumber= int(input("enter the phone number:"))
lists='''
Rice   RS 20/kg
sugar  Rs 30/kg
sopa   Rs 20 
oil    Rs 100/kg
chips  RS 20
pen    Rs 15
salt   Rs 20/kg
'''
price=0
pricelist=[]
totalprice=0
ilist=[]
qlist=[]
plist=[]
# rates of items
items={'Rice':20,'sugar':30,'soap':20,'oil':100,'chips':20,'pen':15,'salt':20}

option=int(input("enter the number 1 to see items avilable: "))
if option==1:
    print(lists)
for i in range(len(items)):
    int1=int(input("press 1 to buy and 2 to exit: "))
    if int1==2:
        break
    if int1==1:
        item=input("enter the your item: ")
        quantity=int(input("enter the quantity: "))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice=totalprice+price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry item is out of stock:")
    else:
        print("you entered wrong: ")
    inp=input("can i bill your items yes or no")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*'=','python super market',25*'=')
            print(28*' ','hyderabad')
            print('phone number:',phonenumber,30*' ','Date:',datetime.now())
            print('sno',8*' ','items',8*' ','quantity',10*' ','price')
            for i in range(len(pricelist)):
                print(i,20*'',15*'',ilist[i],8*'',qlist[i],8*'',plist[i])
            print(75*"=")
            print(50*'','Totalamount:','Rs',totalprice)
            print('Gst',60*'','Rs',gst)
            print(75*'=')
            print(50*'','finalamount:','Rs',finalamount)
            print(75*'=')
            print(50*'','Thankyou visiting')
            

    
            



