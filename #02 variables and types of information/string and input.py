
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
