
default_money = 0
start_money = 0
profit_rate = 0
num_of_month = 0

while(1):
    default_money = float(input("default money : ")) 
    if(default_money<=0):
        print("error : default_money <= 0")
        continue
    else:
        start_money=default_money
        break

while(1):
    profit_rate = float(input("profit rate [0.1-1] : "))
    if(profit_rate>1 or profit_rate <= 0):
        print("error : profit rate")
        continue
    else:
        break

while(1):
    num_of_month = int(input("number of month [1-12] : "))
    if(num_of_month<1 or num_of_month > 12):
        print("error : number of month")
        continue
    else:
        break

for i in range(num_of_month):
    profit=default_money*profit_rate
    default_money+=profit
    print('%.3f' % default_money)

print("total profit in",num_of_month,"months:",'%.3f' %(default_money-start_money))