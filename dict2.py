a = int(input("1-son:  "))
b = int(input("2-son:  "))
amal = input("Qanday amal bajarilishi kerak:")
kalkulator = {
    "qoshish":a+b,
    "ayirish":a-b,
    "ko'paytirish":a*b,
    "bo'lish":a/b
}
if amal == '+':
    print("Natija:  ",kalkulator["qoshish"])
elif amal == '-':
    print("Natija: ",kalkulator["ayirish"])
elif amal == '*':
    print("Naija:  ",kalkulator["ko'paytirish"])
elif amal == '/':
    print("Natija:  ",kalkulator["bo'lish"])
else:
    print("siz kiritgan amal mavjud emas.")