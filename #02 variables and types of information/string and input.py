
#Saydullayev Fayzullo
#02/16/2022
#string

sity = "Toshkent"
district = 'Chilonzor'

print(sity + ' ' + district)

name = "Fayzullo"

print("My name " + name)

surname = "Saydullayev"

full_name = f"{surname} {name}"  #f-string ko'p matinlarni birlashtirish uchun foydalanadi

print(full_name)

print(f"Hi my name {name}. {full_name}!")

#special characters
print("Hello World!")
print("Hello \tWorld!")  #\t katta bo'sh joy tashlash uchun
print("Hello \nWorld!")  #\n keyingi qatorga o'tish uchun

#string methods
print(name)
print(name.upper()) #upper() matndagi barcha harflarni katta harfga aylantiradi
print(name.lower()) #lower() matndagi barcha harflarni kichik harfga aylantiradi

full_name = full_name.lower()
print('\n' + full_name)

#Saydullayev Fayzullo
#02/16/2022
#string and input
#Home Work

kocha = "Bog'bon"
mahalla = "Sag'bon"
tuman = "Olmazor"
viloyat = "Toshkent"

print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + tuman + " tumani, " + viloyat + " shahri")
####################################################################

kocha = input("ko'changiz - ")
mahalla = input("mahallangiz - ")
tuman = input("tumaningiz - ")
viloyat = input("viloyatingiz - ")

print("\n" + kocha.title() + " ko'chasi,\n" + mahalla.title() + " mahallasi,\n" + tuman.title() + " tumani,\n" + viloyat.title() + " shahri.\n")

yangi_manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati."

print(yangi_manzil.upper())
print(yangi_manzil.lower())
print(yangi_manzil.title())
print(yangi_manzil.capitalize())

print(full_name.title()) #title() matndagi har bir so'zning birinchi harfini katta harfga aylantiradi
print(full_name.capitalize()) #capitalize() matndagi birinchi so'zning birinchi harfini katta harfga aylantiradi

text = "\n     Hello    "
print(text)

print(text + "World!")

print(text.lstrip()) #lstrip() matnning chap tomonidagi bo'shliqni olib tashlaydi
print(text.rstrip() + " World!") #rstrip() matnning o'ng tomonidagi bo'shliqni olib tashlaydi
print(text.strip() + " World!\n")

#input
ism = input("Ismingiz nima ")
print("salom " + ism)
