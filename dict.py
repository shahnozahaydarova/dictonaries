a = input('''Sizga qaysi  texnika kerak.
            1 == konditsioner.
            2 == Muzlatgich.
            3 == Televizor. 
                                            ''')
tehnika = {
    "Konditsoner" :{
        "k1":["Samsung","oq","kulrang"],
        "k2":["Good well","oq","kulrang"],
        "k3":("Shivaki","oq","kulrang"),
    },
    "Muzlatgich":{
        "m1":["Samsung","oq","kulrang","qora"],
        "m2":["Good well","oq","kulrang","qora"],
        "m3":("Shivaki","oq","kulrang","qora"),
    },
    "Televizor":{
        "t1":["Samsung","qora"],
        "t2":["Good well","qora"],
        "t3":("Shivaki","qora"),
    },
}
if a == '1':
    print("Siz Konditsioner bo'limini tanladingiz.")
    print(tehnika["Konditsoner"]["k1"][0],tehnika["Konditsoner"]["k2"][0],tehnika["Konditsoner"]["k3"][0])
    b = input("Sizga qaysi turdagi konditsioner kerak:     ")
    if b.lower() == 'samsung':
        print(tehnika["Konditsoner"]['k1'][1],tehnika["Konditsoner"]["k1"][2])
        c = input("Sizga Samsung brendining konditsionerlaridan qaysi rangdagi mahsuloti kerak:     ")
        if c.lower() == 'oq':
            print("Siz samsung brendining oq rangli konditsionerini tanladingiz va mahsulotimizni 500000 so'mga xarid qilishingiz mumkin.")
        elif c.lower() == 'kulrang':
            print("Siz samsung brendining kulrang rangli konditsionerini tanladingiz va mahsulotimizni 450000 so'mga xarid qilishingiz mumkin.")
    if b.lower() == 'good well':
        print(tehnika["Konditsoner"]['k2'][1],tehnika["Konditsoner"]["k2"][2])
        c = input("Sizga Good well brendining konditsionerlaridan qaysi rangdagisi kerak:     ")
        if c.lower() == 'oq':
            print("Siz Good well brendining oq rangli konditsionerini tanladingiz va mahsulotimizni 500000 so'mga xarid qilishingiz mumkin.")
        elif c.lower() == 'kulrang':
            print("Siz Good well brendining kulrang rangli konditsionerini tanladingiz va mahsulotimizni 450000 so'mga xarid qilishingiz mumkin.")
    if b.lower() == 'shivaki':
        print(tehnika["Konditsoner"]['k3'][1],tehnika["Konditsoner"]["k3"][2])
        c = input("Sizga Shivaki brendining konditsionerlaridan qaysi rangdagi mahsuloti kerak:     ")
        if c.lower() == 'oq':
            print("Siz Shivaki brendining oq rangli konditsionerini tanladingiz va mahsulotimizni 500000 so'mga xarid qilishingiz mumkin.")
        elif c.lower() == 'kulrang':
            print("Siz Shivakii brendining kulrang rangli konditsionerini tanladingiz va mahsulotimizni 450000 so'mga xarid qilishingiz mumkin.")
if a == '2':
    print("Siz Muzlatgich bo'limini tanladingiz.")
    print(tehnika["Muzlatgich"]["m1"][0],tehnika["Muzlatgich"]["m2"][0],tehnika["Muzlatgich"]["m3"][0])
    b = input("Sizga qaysi turdagi muzlagich kerak:     ")
    if b.lower() == 'samsung':
        c = input("Sizga Samsung brendining konditsionerlaridan qaysi rangdagi mahsuloti kerak:     ")
        if c.lower() == 'oq':
            print(tehnika["Muzlatgich"]['m1'][1],tehnika["Muzlatgich"]["m1"][2],tehnika["Muzlatgich"]["m1"][3])
            print("Siz samsung brendining oq rangli muzlatgichini tanladingiz va mahsulotimizni 500000 so'mga xarid qilishingiz mumkin.")
        elif c.lower() == 'kulrang':
            print("Siz samsung brendining qora rangli muzlatgichini tanladingiz va mahsulotimizni 450000 so'mga xarid qilishingiz mumkin.")
        elif c.lower() == 'qora':
            print("Siz samsung brendining kulrang rangli muzlatgichini tanladingiz va mahsulotimizni 60000 so'mga xarid qilishingiz mumkin.")   
    if b.lower() == 'good well':
        print(tehnika["Muzlatgich"]['m2'][1],tehnika["Muzlatgich"]["m2"][2],tehnika["Muzlatgich"]['m3'][3])
        c = input("Sizga Good well brendining Muzlatgichlaridan qaysi rangdagisi kerak:     ")
        if c.lower() == 'oq':
            print("Siz Good well brendining oq rangli Muzlatgichini tanladingiz va mahsulotimizni 500000 so'mga xarid qilishingiz mumkin.")
        elif c.lower() == 'kulrang':
            print("Siz Good well brendining kulrang rangli Muzlatgichini tanladingiz va mahsulotimizni 450000 so'mga xarid qilishingiz mumkin.")
        elif c.lower() == 'qora':
            print("Siz Good well brendining qora rangli muzlatgichini tanladingiz va mahsulotimizni 60000 so'mga xarid qilishingiz mumkin.")
    if b.lower() == 'shivaki':
        print(tehnika["Muzlatgich"]['m3'][1],tehnika["Muzlatgich"]["m3"][2],tehnika["Muzlatgich"]["m3"][3])
        c = input("Sizga Shivaki brendining muzlatgichlaridan qaysi rangdagi mahsuloti kerak:     ")
        if c.lower() == 'oq':
            print("Siz Shivaki brendining oq rangli muzlatgichlarini tanladingiz va mahsulotimizni 500000 so'mga xarid qilishingiz mumkin.")
        elif c.lower() == 'kulrang':
            print("Siz Shivaki brendining kulrang rangli muzlatgichlarini tanladingiz va mahsulotimizni 450000 so'mga xarid qilishingiz mumkin.")
        elif c.lower() == 'qora':
            print("Siz Shivaki brendining qora rangli muzlatgichlarini tanladingiz va mahsulotimizni 450000 so'mga xarid qilishingiz mumkin.")
if a == '3':
    print("Siz Televizor bo'limini tanladingiz.")
    print(tehnika["Televizor"]["m1"][0],tehnika["Televizor"]["m2"][0],tehnika["Televizor"]["m3"][0])
    b = input("Sizga qaysi turdagi Televizor kerak:     ")
    if b.lower() == 'samsung':
        print("Siz samsung brendini tanladingiz va mahsulotimizni 60000 so'mga xarid qilishingiz mumkin.")   
    if b.lower() == 'good well':
        print("Siz Good well brendini tanladingiz va mahsulotimizni 60000 so'mga xarid qilishingiz mumkin.")
    if b.lower() == 'shivaki':
        print("Siz Shivaki brendini tanladingiz va mahsulotimizni 450000 so'mga xarid qilishingiz mumkin.")