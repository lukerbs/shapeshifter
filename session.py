from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
#from pyperclip import paste
from os.path import exists
from tqdm import tqdm
import pandas as pd 
import numpy as np 
import requests
# import vpnutil
import string
import random
#import names
import math
import time
import csv
import os

input("ALERT: Did you make sure to rotate the VPN?")

user_agents = [
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
	"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 12.0; rv:95.0) Gecko/20100101 Firefox/95.0",
	"Mozilla/5.0 (X11; Linux i686; rv:95.0) Gecko/20100101 Firefox/95.0",
	"Mozilla/5.0 (Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0",
	"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:95.0) Gecko/20100101 Firefox/95.0",
	"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.43",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.43Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.43"
]

screen_resolutions = [
	[1920,1080],
	[1366,787],
	[1440,900],
	[1536,864],
	[2560,1440],
	[1680,1050],
	[1280,720],
	[1280,800],
	[1792,1120],
	[1600,900]
]

# set driver and chrome options
PATH = "./chromedriver"
chrome_options = Options()  
#chrome_options.add_argument("--headless") 
# random user agent 
user_agent = random.choice(user_agents)
chrome_options.add_argument(f'user-agent={user_agent}')
# random screen resolution
resolution = random.choice(screen_resolutions)
chrome_options.add_argument(f'--window-size={resolution[0]},{resolution[1]}')

# instantiate selenium webdriver object
driver = webdriver.Chrome(executable_path=PATH, options=chrome_options)

print('Creating New Browsing Session ...')
try:
	link = 'https://www.google.com'
	print(f'Opening: {link}\n')
	driver.get(link)
	time.sleep(1.5)
	agent = driver.execute_script("return navigator.userAgent")
	print(f'USER AGENT: {agent}')
	print(f'SCREEN RESOLUTION: {driver.get_window_size()}')


	input('Go?')
	driver.quit()
	print("DONE: Closing browsing session.")

except Exception as e:
	print({f'ERROR: {e}'})
	print('Closing browsing session.')

	driver.quit()

print('')