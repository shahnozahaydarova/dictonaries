lugat = {
    "string":"shunchaki so'z",
    "Integer":123456,
    "Float":12.55,
    "Boolen":12==13,
    "List":[0,1,2,[0]],
    "Tuple":(0.1,(0,1,2)),
    "Dictionaries":{
        "lugat":"shunchaki lugat"
    },
}

a = input('''Sizga qaysi turdagi ma'lumot kerak:
            string
            integer
            float
            boolen
            list
            tuple
            dictionaries                    ''')
if a == 'string':
    print("Siz string ma'lumot turini tanladingiz: ",lugat["string"])
elif a == 'integer':
    print("Siz integer turini tanladingiz: ",lugat["Integer"])
elif a =='float':
    print("Siz float ma'lumot turini tanladingiz: ",lugat["Float"])
elif a == 'boolen':
    print("Siz boolen ma'lumot turini tanladingiz: ",lugat["Boolen"])
elif a == 'list':
    print("Siz list ma'lumot turini tanladingiz: ",lugat["List"])
elif a == 'tuple':
    print("Siz tuple ma'lumot turini tanladingiz: ",lugat["Tuple"])
elif a == 'dictionaries':
    print("Siz dictionaries ma'lumot turini tanladingiz: ",lugat["Dictionaries"])
else:
    print("Siz kiritgan ma'lumot turi mavjud emas.")