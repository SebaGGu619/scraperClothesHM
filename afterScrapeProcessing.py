import bs4

dbMtrx = [ [ 0 for i in range(2) ] for j in range(10000) ]

f = open("h&mteste.html", "r")
a = str(f.read())

soup = bs4.BeautifulSoup(a, features="html.parser")
arrayItems = soup.find_all("div", {"class": "item-details"})

for i in range(len(arrayItems)):
    dbMtrx[i][0] = arrayItems[i].a.contents[0]
    dbMtrx[i][1] = arrayItems[i].span.contents[0]

    print(arrayItems[i].a.contents[0])
    print(arrayItems[i].span.contents[0])
    print("\n")
