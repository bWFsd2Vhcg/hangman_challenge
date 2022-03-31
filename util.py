def get_letter(prompt: str) -> str:
    """Gets Single Letter Input From User, Always Returns Capitalized"""
    letter = ' '
    while len(letter) != 1 or not letter.isalpha():
        letter = input(f'{prompt}: ').strip().upper()
    return letter
