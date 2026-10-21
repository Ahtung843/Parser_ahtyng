import requests
from bs4 import BeautifulSoup


# Теперь мы принимаем именно список selectors (массив классов из интерфейса)
def beautifull(url: str, selectors: list):
    print(f"[ДВИЖОК BS4] Отправляю быстрый запрос к сайту: {url}")
    print(f"[ДВИЖОК BS4] Список классов для поиска: {selectors}")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        print(f"[ДВИЖОК BS4] Ответ получен (Код: {response.status_code})")

        # Если пользователь ввел несколько классов (например, поле 1 — имя, поле 2 — цена)
        if len(selectors) >= 2:
            class_1 = selectors[0]  # Первый класс (например, .tab_item_name)
            class_2 = selectors[1]  # Второй класс (например, .discount_final_price)

            # Собираем два раздельных чистых списка
            list_1 = [el.get_text(strip=True) for el in soup.select(class_1)]
            list_2 = [el.get_text(strip=True) for el in soup.select(class_2)]

            print(f"\n[РЕЗУЛЬТАТ СТРУКТУРИРОВАННОГО ПАРСИНГА]")
            print("-" * 50)

            # Функция zip объединяет их строго попарно: первое имя к первой цене
            # Избегаем ошибок, если списки получились разной длины
            for index, (item_1, item_2) in enumerate(zip(list_1, list_2), start=1):
                print(f"[{index}] {item_1} ===> {item_2}")

            print("-" * 50)

        # Если введен всего один класс, парсим стандартно построчно
        elif len(selectors) == 1:
            found_elements = soup.select(selectors[0])
            print(f"[ДВИЖОК BS4] Найдено элементов: {len(found_elements)}")
            print("-" * 50)
            for index, element in enumerate(found_elements, start=1):
                clean_text = element.get_text(strip=True)
                if clean_text:
                    print(f"[{index}] {clean_text}")
            print("-" * 50)

    except Exception as e:
        print(f"[ДВИЖОК BS4] Ошибка при парсинге: {e}")
