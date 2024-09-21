import requests

def main():

    ur1 = 'https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=1'

    response = requests.get(ur1)
    response.raise_for_status()

    content = response.text

    length = len(content)
    print(f'Длина строки: {length}')

    words = content.split()
    word_count = len(words)
    print(f'Количество слов: {word_count}')

    modified_content = content.replace('.', '!')

    with open('referat2.txt', 'w', encoding='utf-8') as file:
        file.write(modified_content)

    print('Результат сохранен в файл referat2.txt')

if __name__ == '__main__':
    main()

