from colorama import Fore, Back, Style, init
import time
import random

init()



print(Fore.RED+"combien de token a gen ?:")
bite = int(input())

sexes=0

while sexes <= bite :
	def gen_token():
	    a = "AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn1234567890"
	    first = ''.join((random.choice(a)for i in range(20)))
	    second = ''.join((random.choice(a)for i in range(6)))
	    third = ''.join((random.choice(a)for i in range(27)))
	
	    result = "MTAxMDU3"+first + "." + second + "." + third

	    return result

	token = gen_token()
	print(token)
	sexes+=1







input()
