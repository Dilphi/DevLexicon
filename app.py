import flet as ft
import sqlite3

def main(page: ft.Page):
    page.title = "DevLexicon"
    page.theme_mode = "dark"
    page.window_width = 350
    page.window_height = 400
    page.window_resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def validate(e):
        if all([student_name.value, student_surname.value, student_group.value]):
            btn_reg.disabled = False
        
        elif student_name.value == "Адольф":
            btn_reg.text = "А ты шутник"
            btn_reg.disabled = False

        else:
            btn_reg.disabled = True
        page.update()

    def register(e):
        db = sqlite3.connect('students.mab')

        cur = db.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY,
                name TEXT,
                surname TEXT,
                group_name TEXT
            )
        """)
        cur.execute("INSERT INTO students (name, surname, group_name) VALUES (?, ?, ?)", 
            (student_name.value, student_surname.value, student_group.value))

        db.commit()
        db.close()

        student_name.value = ''
        student_surname.value = ''
        student_group.value = ''

        page.update()

    def auth_student(e):
        db = sqlite3.connect('students.mab')

        cur = db.cursor()
        cur.execute("SELECT * FROM students WHERE name = ? AND surname = ? AND group_name = ?", 
                (student_name.value, student_surname.value, student_group.value))
        if cur.fetchone() != None:
            student_name.value = ''
            student_surname.value = ''
            student_group.value = ''
            
            if len(page.navigation_bar.destinations) == 2:
                page.navigation_bar.destinations.append(ft.NavigationDestination(
                    icon = ft.Icons.BOOK,
                    selected_icon = ft.Icons.BOOKMARK
                ))

            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text('Увы, но такого студента нет'))
            page.snack_bar.open = True
            page.update()
        db.commit()
        db.close()

    def change_theme(e):
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        page.update()
    
    
    def show_language_info(language, description):
        page.clean()
        page.add(
            ft.Column(
                [
                    ft.Text(language, size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(description),
                    ft.OutlinedButton("Назад", on_click=lambda e: navigate(None))
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
        page.update()
    
    languages = {
        "JavaScript": "JavaScript — язык программирования для веб-разработки, используется в браузерах.",
        "C#": "C# — язык программирования от Microsoft, используется для разработки игр и приложений.",
        "C++": "C++ — мощный язык программирования, используется в разработке игр и ПО.",
        "Python": "Python — универсальный язык программирования, удобный для начинающих.",
        "SQL": "SQL — язык запросов для работы с базами данных."
    }
    student_name = ft.TextField(label="Имя", width=150, on_change=validate)
    student_surname = ft.TextField(label="Фамилия", width=150, on_change=validate)
    student_group = ft.TextField(label="Группа", width=100, on_change=validate)
    
    btn_reg = ft.OutlinedButton(text="Добавить", width=200, on_click=register, disabled=True)
    btn_auth = ft.OutlinedButton(text="Войти", on_click=auth_student)


        # Создаем row для темы
    theme = ft.Row(
        [
            ft.IconButton(ft.Icons.SUNNY, on_click=change_theme)
        ]
    )

    # Основная панель с регистрацией
    panel_register = ft.Row(
        [
            ft.Column(
                [
                    theme
                ]
            ),
            ft.Column(
                [
                    ft.Text("Ну привет"),
                    student_name,
                    student_surname,
                    student_group,
                    btn_reg
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    panel_auth =  ft.Row(
        [   
             
            ft.Column(
                [
                    theme
                ]
            ),
            ft.Column(
                [
                    ft.Text("Добро пожаловать"),
                    student_name,
                    student_surname,
                    student_group,
                    btn_auth
                ]
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    panel_app = ft.Column(
        [
            theme,
            ft.Text("Выберите язык программирования"),
            *[ft.OutlinedButton(text=lang, on_click=lambda e, l=lang: show_language_info(l, languages[l])) for lang in languages.keys()],
            ft.OutlinedButton(text="Пройти тест")
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    def navigate(e):
        select_index = page.navigation_bar.selected_index
        page.clean()

        if select_index == 0:
            page.add(panel_register)
        elif select_index == 1:
            page.add(panel_auth)
        elif select_index == 2:
            page.add(panel_app)
        
        page.update()

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.Icons.VERIFIED_USER),
            ft.NavigationDestination(icon=ft.Icons.VERIFIED_USER_OUTLINED),
        ],
        on_change=navigate
    )

    page.add(panel_register)

ft.app(target=main)
