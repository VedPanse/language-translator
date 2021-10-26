import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tkinter import *

# import time

query = ''
query2 = ''
text = ''


def translate():
    global query, query2, text

    query = primeE.get()
    query2 = secE.get()
    text = mainTextE.get("1.0", END)

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    # OR options.add_argument("--disable-gpu")

    chrome_driver_path = "/Users/vedpanse/Desktop/Develope/chromedriver"
    driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=options)

    URL = "https://google.com"
    driver.get(URL)

    select_input = driver.find_element(By.NAME, 'q')
    select_input.send_keys(f"Translate {query} to {query2}.")
    select_input.send_keys(Keys.ENTER)

    div_prime = driver.find_element(By.ID, "tw-source-text-ta")
    div_prime.send_keys(text)

    # speaker = driver.find_element(By.CLASS_NAME, "JKu1je")

    main_hub = driver.find_element(By.ID, "kAz1tf")
    speaker_button = main_hub.find_element(By.CLASS_NAME, "JKu1je")

    translated = Label(text=main_hub.text, font=("Arial", 16, "normal"))
    translated.grid(row=9, column=3)

    # speaker.click()
    # time.sleep(4)
    speaker_button.click()

    window.mainloop()


window = Tk()

window.title("Language translator")
window.minsize(2560, 1250)

white_space = Label(text="")
white_space.grid(row=1, column=1)

primeL = Label(text="Please enter your prime language.")
primeL.grid(row=2, column=2)

primeE = Entry()
primeE.grid(row=3, column=2)

secL = Label(text="Please enter your secondary language.")
secL.grid(row=5, column=2)

secE = Entry()
secE.grid(row=6, column=2)

mainTextL = Label(text="Enter the text that you want to translate.")
mainTextL.grid(row=8, column=2)

mainTextE = Text(bg="#f4f4f4", font=("Arial", 16, "normal"))
mainTextE.grid(row=9, column=2, padx=10,
               pady=10,
               ipady=30)

button = Button(text="Translate", command=translate)
button.grid(row=10, column=2)

window.mainloop()
