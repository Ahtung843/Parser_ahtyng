import flet as ft
from core.engine import run


def main(page: ft.Page):
    page.title = "Parser IMB - Cyber Engine"
    page.window.width = 800
    page.window.height = 750  # Немного увеличили высоту под новые элементы
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

    # Выбор движка парсинга
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

    # --- НОВЫЕ ПОЛЯ ДЛЯ НАСТРОЙКИ ЭКСПОРТА ---
    # Поле для ввода имени сохраняемого файла
    filename_input = ft.CupertinoTextField(
        placeholder_text="Имя файла (например: steam_data)",
        border_color="#00FFFF",
        cursor_color="#00FFFF",
        placeholder_style=ft.TextStyle(color="#63458A"),
        text_style=ft.TextStyle(color="#FFFFFF"),
        padding=12
    )

    # Выпадающий список для выбора формата (xlsx, csv, json)
    format_dropdown = ft.Dropdown(
        label="File Format",
        border_color="#00FFFF",
        focused_border_color="#FF007F",
        label_style=ft.TextStyle(color="#00FFFF"),
        color="#FFFFFF",
        options=[
            ft.dropdown.Option("xlsx"),
            ft.dropdown.Option("csv"),
            ft.dropdown.Option("json"),
        ],
        value="xlsx"  # По умолчанию будет стоять Excel
    )

    # --- ДИНАМИЧЕСКИЕ ПОЛЯ КЛАССОВ ---
    def create_selector_field(number):
        return ft.CupertinoTextField(
            placeholder_text=f"Class/Selector #{number} (example: .title)",
            border_color="#9D00FF",
            cursor_color="#00FFFF",
            placeholder_style=ft.TextStyle(color="#63458A"),
            text_style=ft.TextStyle(color="#FFFFFF"),
            padding=12
        )

    selectors_view = ft.ListView(
        controls=[create_selector_field(1)],
        spacing=10,
        height=120,
        expand=True
    )

    def add_field_click(e):
        next_number = len(selectors_view.controls) + 1
        new_field = create_selector_field(next_number)
        selectors_view.controls.append(new_field)
        page.update()

    add_button = ft.IconButton(
        icon=ft.Icons.ADD,
        icon_color="#00FFFF",
        icon_size=30,
        tooltip="Добавить еще один класс",
        on_click=add_field_click
    )

    # --- КЛИК НА ЗАПУСК ПАРСЕРА ---
    def on_button_click(e):
        target_url = url_input.value
        engine = engine_dropdown.value

        # Забираем новые настройки экспорта из ГУИ
        chosen_format = format_dropdown.value
        # Если пользователь забыл ввести имя, даем дефолтное 'parsed_result'
        chosen_filename = filename_input.value if filename_input.value else "parsed_result"

        active_selectors = [field.value for field in selectors_view.controls if field.value]

        print(f"[UI] Выбран формат: {chosen_format}, Имя файла: {chosen_filename}")

        # Отправляем ВСЕ данные (включая формат и имя файла) дальше в engine.py
        run(
            url=target_url,
            engine=engine,
            selectors=active_selectors,
            file_format=chosen_format,
            file_name=chosen_filename
        )

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

                # Ряд с настройками сохранения (Имя + Формат)
                ft.Text("Export Settings", color="#00FFFF", weight=ft.FontWeight.BOLD),
                ft.Row(
                    controls=[
                        ft.Container(content=filename_input, expand=2),
                        ft.Container(content=format_dropdown, expand=1)
                    ],
                    spacing=10
                ),

                ft.Row(
                    controls=[
                        ft.Text("CSS Selectors / Classes", color="#FF007F", weight=ft.FontWeight.BOLD),
                        add_button
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                selectors_view,
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
