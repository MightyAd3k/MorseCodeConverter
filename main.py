morse_code_dict = {
    'A': '*-', 'B': '-***', 'C': '-*-*', 'D': '-**', 'E': '*',
    'F': '**-*', 'G': '--*', 'H': '****', 'I': '**', 'J': '*---',
    'K': '-*-', 'L': '*-**', 'M': '--', 'N': '-*', 'O': '---',
    'P': '*--*', 'Q': '--*-', 'R': '*-*', 'S': '***', 'T': '-',
    'U': '**-', 'V': '***-', 'W': '*--', 'X': '-**-', 'Y': '-*--',
    'Z': '--**', '1': '*----', '2': '**---', '3': '***--', '4': '****-',
    '5': '*****', '6': '-****', '7': '--***', '8': '---**', '9': '----*', 
    '0': '-----', ' ': '/'
}

question = input('Do you want to code or encode the phrase?').lower()
input = input('Enter the phrase you wish to translate into Morse Code: \n').upper()

if question == 'code':

    lst = []
    for char in input:
        for key, value in morse_code_dict.items():
            if char == key:
                lst.append(value + '.')
    print(''.join(lst))

else:

    lst = []
    for char in input.split('.'):
        for key, value in morse_code_dict.items():
            if char == value:
                lst.append(key)
    print(''.join(lst).title())