#  Konwersje liczb i działania na systemach

##  Konwersja z systemu dziesiętnego na inny

### Ogólna metoda:
1. Dziel liczbę dziesiętną przez podstawę nowego systemu.
2. Zapisz resztę.
3. Powtarzaj dzielenie ilorazu aż do 0.
4. Odczytaj zapisane reszty od końca – to wynik.

### Przykłady:

####  Dziesiętny na Binarny
```
13 ÷ 2 = 6 reszta 1  
6 ÷ 2 = 3 reszta 0  
3 ÷ 2 = 1 reszta 1  
1 ÷ 2 = 0 reszta 1  
Wynik: 1101₂
```

####  Dziesiętny na Trójkowy
```
20 ÷ 3 = 6 reszta 2  
6 ÷ 3 = 2 reszta 0  
2 ÷ 3 = 0 reszta 2  
Wynik: 202₃
```

####  Dziesiętny na Ósemkowy
```
83 ÷ 8 = 10 reszta 3  
10 ÷ 8 = 1 reszta 2  
1 ÷ 8 = 0 reszta 1  
Wynik: 123₈
```

---

##  Konwersja z systemu dziesiętnego na dowolny (2–16)

```python
def decimal_to_base(n: int, base: int) -> str:
    if base < 2 or base > 16:
        return "Podstawa musi być w zakresie od 2 do 16"

    if n == 0:
        return "0"

    digits = "0123456789ABCDEF"
    result = ""

    while n > 0:
        result = digits[n % base] + result
        n //= base

    return result

dec = int(input("Podaj liczbę dziesiętną: "))
base = int(input("Na jaką podstawę chcesz przekonwertować (2–16): "))
converted = decimal_to_base(dec, base)
print(f"{dec}₁₀ = {converted}_{base}")
```
##  Dodawanie liczb binarnych „pod kreską”

```python
def dodawanie_binarne(a: str, b: str):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    result = ""
    carry_line = ""
    carry = 0

    for i in range(max_len - 1, -1, -1):
        bit_a = int(a[i])
        bit_b = int(b[i])
        total = bit_a + bit_b + carry
        result_bit = total % 2
        carry = total // 2
        result = str(result_bit) + result
        carry_line = ("↑" if carry else " ") + carry_line

    if carry:
        result = "1" + result
        carry_line = " " + carry_line

    print("  " + a)
    print("+ " + b)
    print("-" * (len(result) + 1))
    print(" " + result)
    print(" " + carry_line + "  (przeniesienia)")


dodawanie_binarne("1101", "1011")
```

#### Przykład:
```
Podaj liczbę dziesiętną: 255
Na jaką podstawę chcesz przekonwertować: 16
Wynik: 255₁₀ = FF₁₆
```

---

## Działania na systemach (2-16)

```python

def add_base_numbers_simple(num1, num2, base):
    if base < 2 or base > 16:
        raise ValueError("Podstawa musi być od 2 do 16.")

    digits = "0123456789ABCDEF"

    char_to_val = {}
    val_to_char = {}
    i = 0
    while i < base:
        char_to_val[digits[i]] = i
        val_to_char[i] = digits[i]
        i += 1

    len1 = len(num1)
    len2 = len(num2)
    max_len = len1 if len1 > len2 else len2

    while len(num1) < max_len:
        num1 = "0" + num1
    while len(num2) < max_len:
        num2 = "0" + num2

    num1 = num1.upper()
    num2 = num2.upper()

    carry = 0
    result = ""

    index = max_len - 1
    while index >= 0:
        d1 = char_to_val[num1[index]]
        d2 = char_to_val[num2[index]]

        total = d1 + d2 + carry
        carry = 0
        if total >= base:
            carry = 1
            total = total - base

        result = val_to_char[total] + result

        index -= 1

    if carry == 1:
        result = "1" + result

    return result


print(add_base_numbers_simple("A", "5", 16))   
print(add_base_numbers_simple("F", "1", 16))    
print(add_base_numbers_simple("1A3", "2F", 16))
print(add_base_numbers_simple("1111", "1", 2))  
```


