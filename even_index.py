#Print Characters Present at Even Index Numbers
def eve(str):
    for i in range(len(str)):
        if i%2==0:
            print(str[i],end='')
    
str='Malay'
eve(str)       