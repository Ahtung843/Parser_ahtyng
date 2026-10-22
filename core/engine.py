# Принимаем новые параметры file_format и file_name
def run(url: str, engine: str, selectors: list, file_format: str, file_name: str):
    print(f"URL: {url} | ENGINE: {engine}")
    print(f"ФОРМАТ: {file_format} | ИМЯ ФАЙЛА: {file_name}")

    if "Playwright" in engine:
        from core.playwrigt_core import playwrig
        final_selector = ", ".join(selectors)
        # Сюда тоже можно будет докинуть, когда обновим playwrig
        playwrig(url, final_selector)

    elif "BeautifulSoup" in engine:
        from core.beautifullsoup_core import beautifull
        # Передаем всё в ядро BeautifulSoup!
        beautifull(url, selectors, file_format, file_name)
