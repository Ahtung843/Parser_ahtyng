from playwright.sync_api import sync_playwright


def playwrig(url: str):
    print(f"[ДВИЖОК PLAYWRIGHT] Начинаю работу с сайтом: {url}")

    with sync_playwright() as p:
        # headless=True означает, что браузер работает скрытно в фоне
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            # Переходим по переданному URL с таймаутом 30 секунд
            page.goto(url, timeout=30000)

            # Ждем, пока на странице затихнет сетевая активность (загрузится JS)
            page.wait_for_load_state("networkidle")

            print(f"[ДВИЖОК PLAYWRIGHT] Страница успешно загружена!")

            print(f"Заголовок страницы: {page.title()}")

            # Сюда мы чуть позже добавим сбор классов, которые введет пользователь

        except Exception as e:
            print(f"[ДВИЖОК PLAYWRIGHT] Ошибка при парсинге: {e}")

        finally:
            browser.close()
