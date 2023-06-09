from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import keyboard
from slowprint import slowprint 
import getpass
username = getpass.getuser()

# Set up Chrome driver options
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-data-dir=C:/Users/"+username+"/AppData/Local/Google/Chrome/User Data")  # Replace with the path to your user data directory

def greet():
    slowprint.slowprint(banner,0.25)
    x=input("Seçimizini belirtiniz: ")
    if(x=="1"):
        roamer()
    if(x=="2"):
        slowprint.slowprint('''
        Codarium Whatsapp Sohbet Botu
        Tarayıcıda açık olan sohbette (grup veya direkt mesaj farketmez) girilen söz 
        kalıbını aktif olarak 5sn aralıklarla arar. Eğer bulunursa daha önceden ayarlamış olduğunuz mesajı gönderir.


        1: Başlat
        Çıkmak için enter tuşuna basınız
        ''',0.25)
        choice=input('Seçiminizi belirtiniz: ')
        if(choice=="1"):
            roamer()
        else:
            exit()
    if(x=="3"):
        exit
def roamer():
    driver = webdriver.Chrome(options=options)

# Navigate to web.whatsapp.com
    driver.get("https://web.whatsapp.com")
    input('Whatsapp Webe giriş yapınız eğer yaptıysanız ve hedef sohbete girdiyseniz entera basınız')
    query = input("Aranacak kelimeyi giriniz: ").lower()
    query=query.lower()
    detectText = input("Hedef kelime bulunduktan sonra gönderilecek mesajı giriniz: ")
    print('Bot aktifleştirildi. Sohbet botunu durdurmak için ESC tuşuna basılı tutunuz')
    while True:
        if(keyboard.is_pressed('esc')):
            print("Bot durduruldu")
            time.sleep(2)
            driver.quit()
            time.sleep(2)
            break
            

        time.sleep(5) 
        text=[]
        parent_spans =driver.find_elements(By.CSS_SELECTOR, "span._11JPr.selectable-text.copyable-text:not([class*='le5p0ye3'])")
        parent_spans_timestamps = driver.find_elements(By.CSS_SELECTOR, 'span.fewfhwl7')
        for x in range(len(parent_spans)):
            # Find the child span element within the parent span

            if(parent_spans[x].text.lower().find(query)!=-1 and  not(any(item in (parent_spans[x].text.lower()+" "+ parent_spans_timestamps[x].text) for item in  [line.rstrip() for line in open('saved.txt')]))):
                
                text.append(parent_spans[x].text)
                text.append(parent_spans_timestamps[x].text)

            # Print the text
        if(text.__len__()!=0):
            print("TESPİT EDİLDİ:",text[0])
            element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p")
            element.send_keys(detectText)
            element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button")
            element.click()
            time.sleep(0.5)
            f = open("saved.txt", "a")
            f.write(str(text[0])+" "+str(text[1]) +"\n")
            f.close()
            y = input('Aramaya devam etmek istiyor musunuz (e,h): ')
            if(y=="e"or y=="E"):
                continue
            if(y=="h"or y=="H"):
                driver.quit()
                time.sleep(2)
                break
# Wait for the user to scan the QR code and manually log in to WhatsApp
banner='''
       /\              
      /##\ 
     /####\ 
    /######\ 
   /########\ 
  /##########\  
 /############\     
/##############\    1: Başlat
\##############/    2: Hakkında
 \############/     3: Çıkış
  \##########/
   \########/
    \######/
     \####/
      \##/
       \/
'''
# Find all parent span elements with class name _11JPr
savedItems=[]

greet()

    # Close the browser

print()
