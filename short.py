from pyshorteners import Shortener
import sys
import os
import keyboard

red="\033[31;1m"
green="\033[1;32m"
yellow="\033[1;33m"
blue="\033[1;34m"
purple="\033[1;35m"
cyan="\033[36;1m"
violate="\033[1;37m"
nc="\033[1;37m"

APInya=[f'1){yellow} TinyURL',f'{nc}2) {yellow}Chilp.it',f'{nc}3) {yellow}Da.gd',f'{nc}4) {yellow}Git.io(Only Github urls)',f'{nc}5) {yellow}Is.gd',f'{nc}6) {yellow}Osdb.link',f'{nc}7) {yellow}Qps.ru',f'{nc}8) {yellow}NullPointer',f'{nc}9) {yellow}Clck.ru']

s = Shortener()

def main():
	
	Link=input(f"{green}Input your link({red}dont porn link :v{green}) >{nc} ")

	print(f"{blue}Choose API you want to use:{nc} ")
	print('\n'.join(map(str, APInya)))

	API=input(f"{green}Input your choosen:{nc} ")

	if API=='1':
		Short_link=s.tinyurl.short(Link)
		print()
		print(f"{green}[SUCCES] {nc}- This your link >{cyan}",  Short_link)
		print()

	elif API=='2':
		Short_link=s.chilpit.short(Link)
		print()
		print(f"{green}[SUCCES] {nc}- This your link >{cyan}",  Short_link)
		print()

	elif API=='3':
		Short_link=s.dagd.short(Link)
		print()
		print(f"{green}[SUCCES] {nc}- This your link >{cyan}",  Short_link)
		print()

	elif API=='4':
		Short_link=s.gitio.short(Link)
		print()
		print(f"{green}[SUCCES] {nc}- This your link >{cyan}",  Short_link)
		print()

	elif API=='5':
		Short_link=s.isgd.short(Link)
		print()
		print(f"{green}[SUCCES] {nc}- This your link >{cyan}",  Short_link)
		print()

	elif API=='6':
		Short_link=s.osdb.short(Link)
		print()
		print(f"{green}[SUCCES] {nc}- This your link >{cyan}",  Short_link)
		print()

	elif API=='7':
		Short_link=s.qpsru.short(Link)
		print()
		print(f"{green}[SUCCES] {nc}- This your link >{cyan}",  Short_link)
		print()

	elif API=='8':
		Short_link=s.nullpointer.short(Link)
		print()
		print(f"{green}[SUCCES] {nc}- This your link >{cyan}",  Short_link)
		print()
	
	elif API=='8':
		Short_link=s.nullpointer.short(Link)
		print()
		print(f"{green}[SUCCES] {nc}- This your link >{cyan}",  Short_link)
		print()
	
	elif API=='9':
		Short_link=s.clckru.short(Link)
		print()
		print(f"{green}[SUCCES] {nc}- This your link >{cyan}",  Short_link)
		print()
	
	else:
		print()
		print(f"{red}[ERROR] {nc}- Please enter valid option")
		print()


def logo():

	os.system("clear")
	print(f'''
          {red}/                      ##
        #/                        ##
        ##                        ##
        ##                        ##
        ##                        ##
        ##  /##      /###     ### ##    /##       /###
        ## / ###    / ###  / ######### / ###     / #### /
        ##/   ###  /   ###/ ##   #### /   ###   ##  ###/
        ##     ## ##    ##  ##    ## ##    ### ###
        ##     ## ##    ##  ##    ## ########    ###
        {nc}##     ## ##    ##  ##    ## #######       ###
        ##     ## ##    ##  ##    ## ##              ###
        ##     ## ##    /#  ##    /# ####    /  /###  ##
        ##     ##  ####/ ##  ####/    ######/  / #### /
         ##    ##   ###   ##  ###      #####      ###/   {red}v.1
               /
              /
             /
            /

        {cyan}=================================================
''')
	inp = input("Press Enter to start: ")
	inp = True

	if inp == True:
		print()
		main()



logo()
