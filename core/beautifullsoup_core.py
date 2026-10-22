import requests
from bs4 import BeautifulSoup
from core.files_core import save_to_file  # Твой модуль сохранения


# Принимаем список селекторов, формат и имя файла из engine.py
def beautifull(url: str, selectors: list, file_format: str, file_name: str):
    print(f"[ДВИЖОК BS4] Начинаю работу...")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        final_data = []

        # Если передано 2 и более классов (например: имя и цена)
        if len(selectors) >= 2:
            class_1 = selectors[0]
            class_2 = selectors[1]

            list_1 = [el.get_text(strip=True) for el in soup.select(class_1)]
            list_2 = [el.get_text(strip=True) for el in soup.select(class_2)]

            # Формируем чистый список пар списков
            final_data = list(zip(list_1, list_2))

            print(f"[ДВИЖОК BS4] Сгруппировано пар для сохранения: {len(final_data)}")
            for index, (item_1, item_2) in enumerate(final_data[:5], start=1):
                print(f"  Превью [{index}]: {item_1} ===> {item_2}")

        # Если передан всего 1 класс
        elif len(selectors) == 1:
            found_elements = soup.select(selectors[0])
            # Сохраняем как пару: [Элемент, Пусто], чтобы DataFrame не ломался
            final_data = [[el.get_text(strip=True), ""] for el in found_elements]
            print(f"[ДВИЖОК BS4] Собрано одиночных элементов: {len(final_data)}")


        if final_data:
            save_to_file(data=final_data, format_type=file_format, file_name=file_name)
        else:
            print("[ДВИЖОК BS4] Нечего сохранять, списки пустые.")

    except Exception as e:
        print(f"[ДВИЖОК BS4] Ошибка парсинга или сохранения: {e}")
