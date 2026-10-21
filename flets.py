import flet as ft
from core.engine import run


def main(page: ft.Page):
    page.title = "Parser IMB - Cyber Engine"
    page.window.width = 800
    page.window.height = 700  # Чуть увеличили высоту для новых полей
    page.window.resizable = False
    page.bgcolor = "#12072B"
    page.theme_mode = ft.ThemeMode.DARK

    # Заголовок
    title = ft.Text(
        value="PARSER IMB",
        size=40,
        weight=ft.FontWeight.BOLD,
        style=ft.TextStyle(
            shadow=ft.BoxShadow(spread_radius=5, blur_radius=15, color="#FF007F")
        ),
        spans=[ft.TextSpan(text=" ARCHITECTURE", style=ft.TextStyle(color="#00FFFF"))]
    )

    # Поле URL
    url_input = ft.CupertinoTextField(
        placeholder_text="https://example.com",
        border_color="#FF007F",
        cursor_color="#FF007F",
        placeholder_style=ft.TextStyle(color="#63458A"),
        text_style=ft.TextStyle(color="#FFFFFF"),
        padding=12
    )

    # Выбор движка
    engine_dropdown = ft.Dropdown(
        label="Engine",
        border_color="#FF007F",
        focused_border_color="#00FFFF",
        label_style=ft.TextStyle(color="#FF007F"),
        color="#FFFFFF",
        options=[
            ft.dropdown.Option("Playwright (Dynamic JS)"),
            ft.dropdown.Option("BeautifulSoup (Fast Static)"),
        ],
        value="BeautifulSoup (Fast Static)"
    )

    # --- ДИНАМИЧЕСКИЕ ПОЛЯ КЛАССОВ (СТРОГО ПО ДОКУМЕНТАЦИИ FLET 1.0+) ---

    # Функция, генерирующая само текстовое поле
    def create_selector_field(number):
        return ft.CupertinoTextField(
            placeholder_text=f"Class/Selector #{number} (example: .title)",
            border_color="#9D00FF",
            cursor_color="#00FFFF",
            placeholder_style=ft.TextStyle(color="#63458A"),
            text_style=ft.TextStyle(color="#FFFFFF"),
            padding=12
        )

    # 1. Инициализируем ListView с ОДНИМ первым полем внутри
    selectors_view = ft.ListView(
        controls=[create_selector_field(1)],  # Первое поле создается сразу здесь
        spacing=10,
        height=150,  # Фиксированная высота для скролла, чтобы элементы не сжимались
        expand=True
    )

    # Функция-обработчик клика по плюсу
    def add_field_click(e):
        # Считаем количество уже созданных полей прямо из ListView
        next_number = len(selectors_view.controls) + 1

        # Создаем новое поле
        new_field = create_selector_field(next_number)

        # Напрямую пушим новое поле в список контролов ListView
        selectors_view.controls.append(new_field)

        # Обновляем всю страницу — теперь Flet гарантированно перерисует добавленный элемент
        page.update()

    # Твой бирюзовый плюс из доки (работает идеально)
    add_button = ft.IconButton(
        icon=ft.Icons.ADD,
        icon_color="#00FFFF",
        icon_size=30,
        tooltip="Добавить еще один класс",
        on_click=add_field_click
    )

    def on_button_click(e):
        target_url = url_input.value
        engine = engine_dropdown.value

        # Собираем данные напрямую из ListView.controls
        active_selectors = [field.value for field in selectors_view.controls if field.value]

        print(f"[UI] Финальный список классов: {active_selectors}")

        # Отправляем массив в твой engine.py
        run(url=target_url, engine=engine, selectors=active_selectors)

    # Кнопка Старт
    start_button = ft.FilledButton(
        content=ft.Text("LAUNCH PARSER", color="#FFFFFF", weight=ft.FontWeight.BOLD),
        bgcolor="#9D00FF",
        on_click=on_button_click,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            shadow_color="#FF007F",
            elevation=10,
        ),
        width=200,
        height=50,
    )

    # Главная панель управления
    control_panel = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Target URL", color="#FF007F", weight=ft.FontWeight.BOLD),
                url_input,
                engine_dropdown,
                ft.Row(
                    controls=[
                        ft.Text("CSS Selectors / Classes", color="#FF007F", weight=ft.FontWeight.BOLD),
                        add_button
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),

                selectors_view,  # 👈 Вставляем наш новый динамический контейнер вместо старого столбца!

                ft.Container(height=10),
                ft.Row([start_button], alignment=ft.MainAxisAlignment.CENTER)
            ],
            spacing=15
        ),
        padding=30,
        border=ft.Border.all(width=2, color="#9D00FF"),
        border_radius=15,
        bgcolor="#1A0B36"
    )

    page.add(
        ft.Column(
            controls=[
                ft.Row([title], alignment=ft.MainAxisAlignment.CENTER),
                ft.Container(height=20),
                control_panel
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )


if __name__ == "__main__":
    ft.run(main)
