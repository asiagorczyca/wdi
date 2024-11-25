import re
import os


# funkcja wyszukująca ile razy dany wzorzec pojawił się w tekście
def num_of_occurrences(pattern, text):
    return len(re.findall(pattern, text))


# funkcja do wybierania pliku txt z obecnego katalogu
def file_pick():
    # lista nazw wszystkich plików w katalogu
    textfiles = [file for file in os.listdir() if file.endswith(".txt")]

    print("Lista dostępnych plików tekstowych: ")
    for i in range(1, len(textfiles) + 1):
        print(f"{i}. {textfiles[i - 1]}")

    while True:
        try:
            filenum = int(input("Podaj numer pliku: ")) - 1
            if 0 <= filenum < len(textfiles):
                break
            else:
                print("Plik o podanym numerze nie istnieje")
        except ValueError:
            print("Podano nieprawidłowy numer pliku. Spróbuj ponownie")

    with open(f'{textfiles[filenum]}', 'r') as f:
        text = f.read()
    return text


text = file_pick()
count = num_of_occurrences(r"\b\w+", text)

print(f"Liczba słów: {count}")
