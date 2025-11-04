
# 7**3 = 347 (** är upphöjt)

#modules:

# 5//7 (// kapar av alla decimal tal)

print("""
x + y = addition
x - y = substraktion
x * y = multiplikation
x / y = division
x ** y = exponent
x % y = restvärde
      """)

x = int(input("x: "))
y = int(input("y: "))

answer = x + y
print(answer)



name = input("Skriv ditt namn") #Standard input av "input" är string
age = input("Skriv din ålder") #Standard input av "input" är string
print("Välkommen", name)
print("Du är", age, "år gammal")

tal1 = int(input("Första talet"))
tal2 = int(input("Gånger detta tal"))
answer = tal1 * tal2

print(tal1, "*", tal2, "Är lika med", answer)

vikt = int(input("Hur mycket väger du i kg?"))
längd = int(input("Hur lång är du i cm?"))
längd2 = längd / 100
längd3 = längd2 ** 2
bmi = vikt//längd3
print("Din bmi är ", bmi)


age2 = input("hur gammal är du?")
antal_veckor = int(age2) * 52.25
print("Du är ", antal_veckor, "veckor gammal")

kg_lbs = int(input("Hur många kg till lbs?"))
lbs = kg_lbs * 2.20462262
print(kg_lbs, "kg är ", lbs, "lbs")