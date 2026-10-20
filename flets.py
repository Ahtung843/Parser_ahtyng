import flet as ft


def main(page: ft.Page):
    # Настройки окна для Flet 1.0+
    page.title = "Parser IMB - Cyber Engine"
    page.window.width = 800
    page.window.height = 600
    page.window.resizable = False

    # Неоновая палитра
    page.bgcolor = "#12072B"
    page.theme_mode = ft.ThemeMode.DARK

    # Заголовок с неоновой тенью
    title = ft.Text(
        value="PARSER IMB",
        size=40,
        weight=ft.FontWeight.BOLD,
        style=ft.TextStyle(
            shadow=ft.BoxShadow(
                spread_radius=5,
                blur_radius=15,
                color="#FF007F",  # Ярко-розовый неон
            )
        ),
        spans=[
            ft.TextSpan(
                text=" ARCHITECTURE",
                style=ft.TextStyle(color="#00FFFF")  # Бирюзовый акцент
            )
        ]
    )

    # Инпуты по новому стандарту
    url_input = ft.CupertinoTextField(
        placeholder_text="https://example.com",
        border_color="#FF007F",
        cursor_color="#FF007F",
        placeholder_style=ft.TextStyle(color="#63458A"),
        text_style=ft.TextStyle(color="#FFFFFF"),
        padding=12
    )

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
        value="Playwright (Dynamic JS)"
    )

    selector_input = ft.CupertinoTextField(
        placeholder_text="example: .product-title or h1",
        border_color="#FF007F",
        cursor_color="#FF007F",
        placeholder_style=ft.TextStyle(color="#63458A"),
        text_style=ft.TextStyle(color="#FFFFFF"),
        padding=12
    )

    #Функция передает в engine юрл, движок
    def on_button_click(e):
        target_url = url_input.value
        engine = engine_dropdown.value

        from core.engine import run
        run(url=target_url, engine=engine)

    # Исправленная кнопка с контентом внутри
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

    # ИСПРАВЛЕНО: Теперь используется ft.Border.all (с большой буквы)
    control_panel = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Target URL", color="#FF007F", weight=ft.FontWeight.BOLD),
                url_input,
                engine_dropdown,
                ft.Text("CSS Selector or Class", color="#FF007F", weight=ft.FontWeight.BOLD),
                selector_input,
                ft.Row([start_button], alignment=ft.MainAxisAlignment.CENTER)
            ],
            spacing=15
        ),
        padding=30,
        border=ft.Border.all(width=2, color="#9D00FF"),  # Новый синтаксис границ
        border_radius=15,
        bgcolor="#1A0B36"
    )

    # Вывод на экран
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



