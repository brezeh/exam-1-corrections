#exam 1 corrections breze howard

#prints results 
for num in range(1,51):
    prints = ""
    
    if num % 5 == 0:
        prints += 'HiFive'
    elif num % 2 == 0: 
        prints += "HiTwo"
    elif num % 3 == 0 or num % 7 == 0:
        prints += "HiThreeOrSeven"
    print(prints)