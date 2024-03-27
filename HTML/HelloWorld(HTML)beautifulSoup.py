from bs4 import BeautifulSoup

# HTML kods
html_code = "<html><body><h1>Hello, World!<h1></body></html>"

# izveidojas BeautifulSoup objektu
soup = BeautifulSoup(html_code, 'html.parser')

# Iegūstam tekstu no h1 elementa
text = soup.h1.text

#ctrl + F to search for something in the code of a web page

# Izvadam rezultātu
print("Teksts", text)