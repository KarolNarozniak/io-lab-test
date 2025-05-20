# Defininicja alfabet Base64 ale lepiej
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def extract_hidden_bits(encoded):
    """
    Wyciąga ukryte bity z zakodowanego Base64 napisu.
    Jeśli kończy się na "==", to mamy 1 bajt – bierzemy 4 dolne bity z drugiego znaku.
    Jeśli kończy się na "=" (ale nie "=="), to mamy 2 bajty – bierzemy 2 dolne bity z trzeciego znaku.
    """
    if encoded.endswith("=="):
        block = encoded[-4:]
        char_val = alphabet.index(block[1])
        hidden_bits = char_val & 0b1111  # wyciągamy 4 dolne bity
        return format(hidden_bits, "04b")
    elif encoded.endswith("="):
        block = encoded[-4:]
        char_val = alphabet.index(block[2])
        hidden_bits = char_val & 0b11  # wyciągamy 2 dolne bity
        return format(hidden_bits, "02b")
    else:
        # Brak paddingu = brak ukrytych bitów
        return ""


def bits_to_text(bit_string):
    """
    Konwertuje ciąg bitów na tekst, grupując po 8 bitów.
    Jeśli ostatnia grupa ma mniej niż 8 bitów, ją pomijamy.
    """
    chars = []
    for i in range(0, len(bit_string), 8):
        byte = bit_string[i : i + 8]
        if len(byte) < 8:
            break
        chars.append(chr(int(byte, 2)))
    return "".join(chars)


# Ścieżka do pliku (pamiętaj o odpowiednich backslashach lub surowym stringu)
file_path = r"D:\Files_from_browser\secret_flag\secret_flag\secret_flag.txt"

hidden_bits_total = ""

try:
    with open(file_path, "r") as file:
        # Czytamy plik linia po linii
        for line in file:
            encoded_line = line.strip()
            if encoded_line:
                hidden_bits = extract_hidden_bits(encoded_line)
                hidden_bits_total += hidden_bits
except FileNotFoundError:
    print("File not found:", file_path)
    exit(1)

print("Hidden bits:", hidden_bits_total)

# Konwertujemy zebrane bity na tekst
decoded_text = bits_to_text(hidden_bits_total)
print("Decoded text (flag):", decoded_text)
