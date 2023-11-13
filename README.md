<h1 style="text-align: center;"><span style="color: #993300;">Auto Send Message telegram</span></h1>
With this collection you can be continuous and unlimited,
<ul>
 	<li><span style="color: #808080;">Send Message to your group you want.</span></li>

<h1 style="text-align: center;"><span style="color: #993300;">How To Run This Program?</h1>
	<li><span style="color: #808080;">First intall lastest python here https://www.python.org/</span></li>
 <li><span style="color: #808080;">Install telethon </span></li>
``` 
import pyautogui
import pandas
import time

excel_data = pandas.read_excel('Recipients data.xlsx', sheet_name='Recipients')

count = 0

time.sleep(3)

for column in excel_data['Username'].tolist():

      pyautogui.press('esc')
      pyautogui.hotkey('ctrl', 'f')
      time.sleep(1)
      pyautogui.write(str(excel_data['Username'][count]));
      pyautogui.press('enter')
      time.sleep(2)
      pyautogui.press('down')
      pyautogui.press('enter')
      pyautogui.write(str(excel_data['Message'][0]));
      pyautogui.press('enter')
      pyautogui.press('esc')
      count = count + 1

print('The script executed successfully.')
```
<li><span style="color: #808080;">Setup The  Code</span></li>
<li><span style="color: #808080;">Run in cmd vscode use this</span></li>
```python script.py```
<li><span style="color: #808080;">Recomended to use delay time more than 5 for not getting ban and detect spamming</span></li>
<h1 style="text-align: center;"><span style="color: #993300;">Dont forget to For this reppo and give me star</span></h1>
  
</ul>
