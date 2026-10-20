def run(url: str, engine: str):
    print(f"URL: {url}")
    print(f"ENGINE: {engine}")

    if "Playwright" in engine:
        print("Playwright")
    elif "BeautifulSoup" in engine:
        print("BeautifulSoup")