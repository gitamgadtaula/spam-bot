import pyautogui
import time
from PyPDF2 import PdfReader
reader = PdfReader("script.pdf")
totalPages = reader.numPages


def startSpamming():
    for i in range(0, totalPages):
        page = reader.pages[i]
        print('place your cursor active to wherever you want to spam in 5 seconds')
        time.sleep(5)
        text = page.extract_text()
        for each_line in text:
            pyautogui.typewrite(each_line)
            pyautogui.press('enter')


startSpamming()
