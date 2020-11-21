#!/usr/bin/env python

import time
import sys
import requests
from bs4 import BeautifulSoup

URL = "https://www.fakeaddressgenerator.com/All_countries/address/country/Ireland"
i = 0
while i < 50:
  page = requests.get(URL, "lxml")
  time.sleep(2)
  soup = BeautifulSoup(page.content, "html.parser")
  a = []

  for article in soup.find_all("input", class_="no-style"):
    start = str(article).find("value")
    start = int(start) + 7
    end = (str(article)[start:]).replace('\xa0', ' ')
    t = 0
    while end[t] != '"':
      t = t + 1
    a.append(end[0:t])
  output = str((a[0],a[4],a[5],a[6],a[8]))

  with open("output.txt", "a+") as f:
    f.write(output + "\n")
  i = i + 1
