import os,sys,time,random
print("")
print("")
color = ["\033[1;31m","\033[1;32m"]
def menu(testeteste):
m = random.choice(color)+"Bem vindo THBD! \n Para mais informações, insira '1' \n\n"
for msg in m:
    sys.stdout.write(msg)
    sys.stdout.flush()
    time.sleep(0.06)
print("")
else:
break

loop = True

while loop:
    menu()
    what = input("#: ")
if what == "1":
        print("====================================")
        print("[+] Github: https://github.com/winndev")
        print("[+] Twitter: https://twitter.com/winnhacking")
        print("[+] Instagram: https://instagram.com/winntralha")
        print("[+] Discord: winndev#0606")
        print("[+] Site: https://shadowmans.tk")
        print("====================================")
        rmenu = input("[?] Voltar para o menu principal ? (s/n): ")
        if rmenu == "y":
            menu()
        else:
            break
