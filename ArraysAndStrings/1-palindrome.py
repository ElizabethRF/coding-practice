"""
Escribe un programa que verifique que una frase es un palíndromo.
Un palíndromo es una frase que se lee igual de derecha a izquierda que de izquierda a derecha.

General questions:
- should i consider spaces? * no
- are there any special characters that i should transform or ignore? * consider only alphanumeric transform áéíóúüñÁÉÍÓÚÜ
- is it case sensitive? *no

Solution ideas: s
- stack
- two pointers

* assumed answers by me
"""

def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    # remove special chars
    a, b = 'áéíóúüñÁÉÍÓÚÜ', 'aeiouunAEIOUU'
    transition = str.maketrans(a, b)
    s = s.translate(transition)

    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[right].lower() != s[left].lower():
            return False
        else:
            left += 1
            right -= 1

    return True


if __name__ == "__main__":
    tests = [
        "0P",
        "La ruta nos aportó otro paso natural",
        "Claramente, esto no es un palíndromo"
    ]
    for x in tests:
        print(is_palindrome(x))