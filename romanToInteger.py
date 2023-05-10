class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        value = 0
        letter_bef = ''
        for letter in reversed(s):
            if (letter_bef == 'V' or letter_bef == 'X') and letter == 'I':
                value -= (1 + symbols[letter])
            elif (letter_bef == 'L' or letter_bef == 'C') and letter == 'X':
                value -= (10 + symbols[letter])
            elif (letter_bef == 'D' or letter_bef == 'M') and letter == 'C':
                value -= (100 + symbols[letter])

            value += symbols[letter]
            letter_bef = letter

        return value
