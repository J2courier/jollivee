#initializing
des = ["","Hamburger", "French Fries", "Coke", "Exit"]
prc = [0, 25, 30, 15]
stock_Beg = [0, 100, 100, 100]
stock_End = [0, 100, 100, 100 ]
prev_qty = [0, ]
pres_qty = [0, 0, 0, 0]
grandtotal = []
sold = []
sales = []
stl = 0
item = 1
chng = 0
ttl = 0
order = 1
qty = 0
q = [0, ]
sentinelData = ""

#display option
def display():
    print(f"Order No: {order}")
    print(f"[1] {des[1]} | ₱  {prc[1]} | {stock_End[1]}")
    print(f"[2] {des[2]} | ₱  {prc[2]} | {stock_End[2]}")
    print(f"[3] {des[3]} | ₱  {prc[3]} | {stock_End[3]}")
    print(f"[4] {des[4]}")
#to create out loop for entering a choice
while True:
    display()#call out the function display
    ch = int(input("please enter choice: "))
    if ch < 0 or ch > 4:
        print("invalid input")
    if ch == 4:
        if stl != 0:
            break
        if stl == 0:
            print("you've exited.")
            ans = str(input("Another customer?: "))
            if ans == 'Y' or ans == 'y':
                print("please wait")
    if ch > 0 and ch <4:
        pres_qty[ch] = int(input("please enter quantity: "))
        print("---------------------------------------------------------------")
        if ch <= stock_Beg[ch]: 
            stl = pres_qty[ch] * prc[ch]
            stock_End[ch] = stock_Beg[ch] - pres_qty[ch]
            prev_qty = pres_qty
            print(f"{item} Description: {des[ch]} | Price: ₱ {prc[ch]} | stocks: {stock_End[ch]} | qty: {pres_qty[ch]} | subtotal: {stl}")
            item += 1          
            ttl = stl + ttl 
            print("---------------------------------------------------------------")
             
while True:
    print("---------------------------------------------------------------")
    print(f"Total is: {ttl}")
    print("---------------------------------------------------------------")
    pyt = int(input("Please enter your payment: "))
    print("---------------------------------------------------------------")
    if pyt < ttl:#if the payment is less than the total prize, either cancel order or make some changes in order and payment     
        print("insufficient amount")
        ans = str(input("Cancel order? Y or N?: "))
        if ans == 'Y' or ans == 'y': 
            #qty = qty + pres_qty[ch]
            #q[ch] = qty
            #stock_End[ch] = stock_End[ch] + prev_qty
            print("order cancelled!!")
            print("Im trying to reset the stocks")
            #print(f"[1] {des[1]} | ₱  {prc[1]} | {stock_End[1]}")
            #print(f"[2] {des[2]} | ₱  {prc[2]} | {stock_End[2]}")
            #print(f"[3] {des[3]} | ₱  {prc[3]} | {stock_End[3]}")
            #print(f"[4] {des[4]}")
        if ans == 'N' or ans == 'n':
            ttl = 0
            while True:
                ch = int(input("please enter choice: "))
                if ch == 4:
                    if stock_End != stock_Beg:
                        break
                    if stock_End == stock_Beg: 
                        print("you've exited.")
                        exit
                    if ch > 0 and ch <4:
                        qty = int(input("please enter quantity: "))
                        print("wala ko pa na reset ang stocks....")
                        if ch <= stock_Beg[ch]: 
                            stl = qty * prc[ch]
                            stock_End[ch] = stock_End[ch] - qty
                            print(f"{item} Description: {des[ch]} | Price: ₱ {prc[ch]} | stocks: {stock_End[ch]} qty: {qty} subtotal: {stl}")
                            item += 1          
                            ttl = stl + ttl                       
    if pyt > ttl:#if payment is greater than the total price
        chng = pyt - ttl
        print("---------------------------------------------------------------")
        print(f"Payment is: {pyt}")
        print(f"Change: {chng}")
        print("---------------------------------------------------------------")
        print("order success!!")
        ans = str(input("another customer?: "))
        if ans == 'Y' or ans == 'y':
            order += 1
            display()
            ch = int(input("please enter choice: "))
            if ch == 4:
                if stl != 0:
                    break
                if stl == 0:
                    print("you've exited.")
                    ans = str(input("Another customer?: "))
                    if ans == 'Y' or ans == 'y':
                        print("please wait")
            if ch > 0 and ch <4:
                pres_qty[ch] = int(input("please enter quantity: "))
                print("---------------------------------------------------------------")
                if ch <= stock_Beg[ch]: 
                    stl = pres_qty[ch] * prc[ch]
                    stock_End[ch] = stock_Beg[ch] - pres_qty[ch]
                    print(f"{item} Description: {des[ch]} | Price: ₱ {prc[ch]} | stocks: {stock_End[ch]} | qty: {pres_qty[ch]} | subtotal: {stl}")
                    item += 1          
                    ttl = stl + ttl 
                    print("---------------------------------------------------------------")
                    break
        if ans == 'N' or ans == 'n':
            print("wait...")
            break
    if pyt == ttl:#if payment is equal to the total price
        print(f"Payment is: {pyt}")
        print(f"Change: {chng}")
        print(f"Order Success!!")
            #sd = prev_qty + sold
        #sold.append(sd)
        #sl = stl + sales
        #sales.append(sl)
        #gtl = ttl[order] + ttl[order + 1]
        #grandtotal.appened(gtl)
        ans = str(input("another customer?: "))
        if ans == 'Y' or ans == 'y':
            order += 1
            print("wait hold on...")
            break
        if ans == 'N' or ans == 'n':
            print("OKAY NA CODE KO PA, supposed to be ma display na di ang inventory!")
            break
                    #print("---------SB-------SE-------SOLD-------SALES")
                    #print(f"{des[1]} {stock_Beg[1]} {stock_End[1]} {sd[1]} {sl[1]}")
                    #print(f"{des[2]} {stock_Beg[2]} {stock_End[2]} {sd[2]} {sl[2]}")
                    #print(f"{des[3]} {stock_Beg[3]} {stock_End[3]} {sd[3]} {sl[3]}")
                
                
                
        
                
                
            

        
        
            
            
                

                     
                    

                
                
                
                
                
                
                
