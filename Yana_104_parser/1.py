import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = 'https://cars.av.by/kia/niro'
r = requests.get(url)
soup = bs(r.text, "html.parser")
op = soup.find("div.card__comment", "div")
# soup = soupp(r.text, 'html')
# r.text
print(op)

# html= BS(url.content, 'html.parser')

# for el in html

# class="listing-item__message"><div>Состояние нового авто, без пробега по РБ. В родной краске, в ДТП не учавствовала.
# Полностью обслужена. 2-х зонный климат контроль, полный электропакет, мульти руль, адаптивный круиз контроль,
# LED оптика, камера заднего вида, блютуз громкая связь и многое другое. Дополнительный комплект зимней резины
# на  литых дисках.</div></div><div
