from pyshorteners import Shortener
import os

red = "\033[31;1m"
green = "\033[1;32m"
blue = "\033[1;34m"
cyan = "\033[36;1m"
nc = "\033[1;37m"

pilApi = [
    (f"{nc}Adf.ly", 'adfly'),
    (f"{nc}Bit.ly", 'bitly'),
    (f"{nc}Chilp.it", 'chilpit'),
    (f"{nc}Clck.ru", 'clckru'),
    (f"{nc}Cutt.ly", 'cuttly'),
    (f"{nc}Da.gd", 'dagd'),
    (f"{nc}Git.io", 'gitio'),
    (f"{nc}Is.gd", 'isgd'),
    (f"{nc}NullPointer", 'nullpointer'),
    (f"{nc}Os.db", 'osdb'),
    (f"{nc}Ow.ly", 'owly'),
    (f"{nc}Po.st", 'post'),
    (f"{nc}Qps.ru", 'qpsru'),
    (f"{nc}Short.cm", 'shortcm'),
    (f"{nc}Tiny.cc", 'tinycc'),
    (f"{nc}TinyURL.com", 'tinyurl')
]

shortener = Shortener()

def main():
    link = input(f"{green}Input your link({red}no porn links please :v{green}) >{nc} ")
    
    if not (link.startswith("http://") or link.startswith("https://")):
        link = "http://" + link

    print(f"{blue}Choose API you want to use:{nc} ")

    for i, (name, _) in enumerate(pilApi, start=1):
        print(f"{i}) {name}")

    pil = input(f"{green}Input your choice:{nc} ")

    if pil.isdigit() and 1 <= int(pil) <= len(pilApi):
        apiName = pilApi[int(pil) - 1][1]
        try:
            shortLink = getattr(shortener, apiName).short(link)
            print(f"\n{green}[SUCCESS] {nc}- Your shortened link: {cyan}{shortLink}{nc}\n")
        except Exception as e:
            print(f"\n{red}[ERROR] {nc}- Failed to shorten link: {str(e)}\n")
    else:
        print(f"\n{red}[ERROR] {nc}- Please enter a valid option\n")

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
    input("Press Enter to start: ")
    main()

if __name__ == "__main__":
    logo()
