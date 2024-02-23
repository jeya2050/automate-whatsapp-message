import pywhatkit
import pyautogui
import pandas as pd
df=pd.read_excel(r"Street Vendor Data11-Dec-2023.xlsx")

df=df[100::]#got first 100 df
# screenWidth, screenHeight = pyautogui.size()
# 2423,1293
print(df)

for i in df.iloc:
    name=(str(i["Name Of Street Vendor"])).upper()
    number=int(str(i["Mobile No"]).replace(" ",""))
    app_id=i["Application No"]
    print(name,number,app_id)

    message = f"""ஐயா/அம்மா {name}, 

        பிரதமரின் சாலையோர வியாபாரிகள் அரசு நலத்திட்டத்தின் கீழ் தாங்கள் வங்கி கடன் பெற்றுள்ளதை தொடர்ந்து தங்கள் குடும்பத்தின் விபரம் பதிவு செய்ய வேண்டி நகராட்சி அலுவலகத்திற்கு வரவும்.

        உங்கள் பதிவு என் : {app_id}
        மேலும் விவரங்களுக்கு : 7812844822

                        இப்படிக்கு - தேவகோட்டை நகராட்சி """
    try:
        result=pywhatkit.sendwhatmsg_instantly(str(f"+{number}"),message)
        pyautogui.moveTo(2423,1293)
        pyautogui.click()
    except Exception as a:
        print(a)
        print("message not send")
    finally:  
        pass       

print("work is completed")
