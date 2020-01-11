
x=([5,1,3],2)
def get_checkout_time(cust):
    checkout_time=0
    if cust[1]==1:
        checkout_time=sum(cust[0])
    elif cust[1]>1:
        counter=[i for i in range(cust[1])]
        print(counter)
        
    print("Checkout TIme:",checkout_time)
get_checkout_time(x)
'''
A=[i for i in range(20)]
print(A)
'''
