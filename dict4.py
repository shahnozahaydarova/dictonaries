hayvon = {
    "uy hayvonlari":{
        "ot":["jigarrang","o't"],
        "it":("oq-qora","go'sht")
    },
    "yovvoyi hayvonlar":{
        "ayiq":["oq","asal"],
        "tulki":("sariq","hayvon")
    }
}


a = input('''Sizga qaysi turdagi hayvon haqida ma\'lumot kerak:
            1 == uy hayvonlari
            2 == yovvoyi hayvonlar        ''')
if a=='1':
    b = input('''Siz uy hayvonlari bo'limini tanladingiz.Sizga qaysi uy hayvoni haqida ma'lumot kerak:
            1 == ot
            2 ==it                  ''')
    if b == '1':
        print("Siz tanlagan hayvon ot.Otning rangi: ",hayvon["uy hayvonlari"]["ot"][0],"Ozuqasi: ",hayvon["uy hayvonlari"]["ot"][1])
    elif b == '2':
        print("Siz tanlagan hayvon it.Itning rangi: ",hayvon["uy hayvonlari"]["it"][0],"Ozuqasi",hayvon["uy hayvonlari"]["it"][1])
elif a == '2':
    c = input('''Siz yovvoyi hayvonlar bo'limini tanladingiz.Sizga qaysi yovvoyi hayvon haqida ma'lumot kerak: 
            1 == ayiq
            2 == tulki              ''')
    if c == '1':
        print("Siz tanlagan hayvon ayiq.Ayiqning rangi: ",hayvon["yovvoyi hayvonlar"]['ayiq'][0],"Ozuqasi: ",hayvon["yovvoyi hayvonlar"]['ayiq'][1])
    elif c == '2':
        print("Siz tanlagan hayvon tulki.Tulkinng rangi: ",hayvon["yovvoyi hayvonlar"]['tulki'][0],"Ozuqasi: ",hayvon["yovvoyi hayvonlar"]['tulki'][1])
else:
    print("Bizda mavjud bo'lmagan ma'lumot turini kiritdingiz.")        