import os
import requests
from bs4 import BeautifulSoup


def create_jokes_folder():
    folder_name = "jokes"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name


def parse_jokes(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        jokes = []

        joke_blocks = soup.find_all('div', class_='text')

        for block in joke_blocks:
            joke_text = block.get_text(strip=True)
            if joke_text:  # Пропускаем пустые блоки
                jokes.append(joke_text)

        return jokes

    except Exception as e:
        print(f"Ошибка при парсинге: {e}")
        return []


def save_jokes_to_file(jokes, folder_name):
    file_path = os.path.join(folder_name, "jokes.txt")
    with open(file_path, 'w', encoding='utf-8') as file:
        for i, joke in enumerate(jokes, 1):
            file.write(f"{i}. {joke}\n\n")
    print(f"Сохранено {len(jokes)} шуток в файл: {file_path}")



url = 'https://www.anekdot.ru/'
jokes_folder = create_jokes_folder()
jokes_list = parse_jokes(url)

if jokes_list:
    save_jokes_to_file(jokes_list, jokes_folder)
else:
    print("Не удалось получить шутки. Проверьте подключение к интернету или структуру сайта.")