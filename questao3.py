def roman_to_arabic(roman_numeral):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arabic_numeral = 0
    prev_value = 0
    
    for char in roman_numeral[::-1]:
        curr_value = roman_values[char]
        if curr_value < prev_value:
            arabic_numeral -= curr_value
        else:
            arabic_numeral += curr_value
        prev_value = curr_value
    
    return arabic_numeral

# Exemplo de uso
roman_numeral = "MMXXIII"
arabic_numeral = roman_to_arabic(roman_numeral)
print(f'O número romano {roman_numeral} é igual a {arabic_numeral} em indo arábicos')
