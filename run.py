from textfinder import mainpart
import time
import pyautogui as g
import os
time.sleep(2)
g.click(x=200, y=200)
mainpart()
f = open('recognized.txt','r')
text = f.read()
newlinerm = text.strip('\n')
scraped = newlinerm.split('SIGNUP LOGIN')
scraped2 = scraped[1].split('About')
almostfinal1 = scraped2[0].strip('\n')
almostfinal2 = almostfinal1.strip('  ')
almostfinal3 = almostfinal2.strip('\n')
final1 = almostfinal3.split('.\n')
final2 = final1[0].replace('\n',' ')
final3= final2.replace('|','I')
final = final3.replace('  ', ' ')
print(final)
f.close()
try:
    os.system('del wordss.png')
    os.system('del recognized.txt')
except:
    pass
g.click(x=500, y=500) # click text box
g.typewrite(final+'.')#,interval=.05)   #setup for intervals in seconds
