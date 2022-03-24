import requests

culori = ["alb_ffffff",
          "albastru_0000ff",
          "argintiu_c0c0c0",
          "auriu_ffd700",
          "bej_f5f5dc",
          "bronz_cd7f32",
          "galben_ffff00",
          "gri_808080",
          "maro_a52a2a",
          "mov_800080",
          "multicolor_000000",
          "negru_000000",
          "portocaliu_ffa500",
          "roz_ffc0cb",
          "roșu_ff0000",
          "transparent_ffffff",
          "turcoaz_40e0d0,",
          "verde_008000",
          ]


def getPage(url):
    print("-", end='')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    r = requests.get(url, allow_redirects=True, headers=headers)
    print(" -", end='')
    temp = bytes(r.content)
    print(" -", end='')
    temp = temp.decode("utf8")
    return temp


content = ""
for i in range(18):
    print("\n" + str(i+1) + "/18: ", end='')
    content = content + "\n" + getPage("https://www2.hm.com/ro_ro/femei/cumparaturi-sortate-dupa-produs/view-all.html?sort=newProduct&colorWithNames=%s&image-size=small&image=model&offset=0&page-size=1800" % (culori[i]))

f = open("h&mteste.html", "w")
f.write(content)
f.close()