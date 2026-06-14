d={'AAPL':180,'TSLA':250}
total=0
n=int(input('Total number of stock:'))
for i in range(n):
    name=input('\nEnter the stock name(in capital):')
    qty=int(input('Enter the quantity:'))
    name1=name.upper()
    if name in d:
        inv=d[name1]*qty
        total+=inv
        print('Value=',inv)
    else:
        print('Stock not found')
print('\nTotal investment=',total)
