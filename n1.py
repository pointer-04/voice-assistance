import os

while True:
    print("--- Enter your choice below, enter z to exit")
    print("Enter your requirement : ",end=" ")
    text=input()
    text=text.lower()

    if 'z' in text:
        print("Program terminated")
        break

    if ('run' in text) or ('execute' in text) or ('launch' in text) or ('start' in text) or ('play' in text) or ('open' in text):
        if 'firefox' in text or 'google' in text:
            os.system("firefox www.google.com")
            print("Action completed successfuly")
            print("Do you wish to continue? [Y/N] : ",end=" ")
            ip=input()
            ip=ip.lower()
            if 'y' in ip:
                continue
            else:
                print("--- Thank you! ---")
                break
        elif 'chrome' in text or 'google' in text:
            os.system("chrome www.google.com")
            print("Action completed successfuly")
            print("Do you wish to continue? [Y/N] : ",end=" ")
            ip=input()
            ip=ip.lower()
            if 'y' in ip:
                continue
            else:
                print("--- Thank you! ---")
                break
        elif 'notepad' in text:
            os.system("notepad")
            print("Action completed successfuly")
            print("Do you wish to continue? [Y/N] : ",end=" ")
            ip=input()
            ip=ip.lower()
            if 'y' in ip:
                continue
            else:
                print("--- Thank you! ---")
                break
        elif 'sublime' in text or 'sublime text' in text:
            os.system("subl")
            print("Action completed successfuly")
            print("Do you wish to continue? [Y/N] : ",end=" ")
            ip=input()
            ip=ip.lower()
            if 'y' in ip:
                continue
            else:
                print("--- Thank you! ---")
                break
        elif 'wireshark' in text or 'wire shark' in text:
            os.system("wireshark")
            print("Action completed successfuly")
            print("Do you wish to continue? [Y/N] : ",end=" ")
            ip=input()
            ip=ip.lower()
            if 'y' in ip:
                continue
            else:
                print("--- Thank you! ---")
                break
        elif 'text editor' in text or 'text' in text:
            os.system("gedit")
            print("Action completed successfuly")
            print("Do you wish to continue? [Y/N] : ",end=" ")
            ip=input()
            ip=ip.lower()
            if 'y' in ip:
                continue
            else:
                print("--- Thank you! ---")
                break
        elif 'music box' in text or 'music' in text or 'rhythm box' in text:
            os.system("rhythmbox")
            print("Action completed successfuly")
            print("Do you wish to continue? [Y/N] : ",end=" ")
            ip=input()
            ip=ip.lower()
            if 'y' in ip:
                continue
            else:
                print("--- Thank you! ---")
                break
        elif 'cheese' in text or 'camera' in text or 'click' in text:
            os.system("cheese")
            print("Action completed successfuly")
            print("Do you wish to continue? [Y/N] : ",end=" ")
            ip=input()
            ip=ip.lower()
            if 'y' in ip:
                continue
            else:
                print("--- Thank you! ---")
                break
        elif 'document editor' in text or 'libre office' in text:
            os.system("libreoffice")
            print("Action completed successfuly")
            print("Do you wish to continue? [Y/N] : ",end=" ")
            ip=input()
            ip=ip.lower()
            if 'y' in ip:
                continue
            else:
                print("--- Thank you! ---")
                break
        elif 'anaconda' in text:
            os.system("anaconda-navigator")
            print("Action completed successfuly")
            print("Do you wish to continue? [Y/N] : ",end=" ")
            ip=input()
            ip=ip.lower()
            if 'y' in ip:
                continue
            else:
                print("--- Thank you! ---")
                break
        else:
            print("!!! required application is not in computer !!!")
            continue 
    else:
        print("!!! invalid requirement !!!")
        continue
