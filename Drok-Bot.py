from googlesearch import *
from termcolor import *
head = colored (       '===== Welcome To Drok BOT =====' , 'yellow')
head2 = colored('       === By Vegan Hacker ===' , 'red')
print(' ')
print(' ')
print(head)
print(head2)
print(' ')
print(' ')
word = input(colored('  Enter Drok :' , 'green'))
#number = input(colored('  How many sites do you want :' , 'green'))
for url in search(word,stop = 300):
    print(url)