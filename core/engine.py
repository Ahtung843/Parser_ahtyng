def run(url: str, engine: str, selectors: list):
    print(f"URL: {url}")
    print(f"ENGINE: {engine}")
    print(f"СПИСОК КЛАССОВ В ЯДРО: {selectors}")

    if "Playwright" in engine:
        from core.playwrigt_core import playwrig
        # Для плейрайта пока можно оставить строку, если не переписал его внутренности
        final_selector = ", ".join(selectors)
        playwrig(url, final_selector)

    elif "BeautifulSoup" in engine:
        from core.beautifullsoup_core import beautifull
        # Передаем ЧИСТЫЙ СПИСОК (массив) прямо в ядро супа!
        beautifull(url, selectors)

