import flet as ft
import sqlite3

def main(page: ft.Page):
    page.title = "DevLexicon"
    page.theme_mode = "dark"
    page.window.width = 350
    page.window.height = 400
    page.window.resizable = False
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
                page.navigation_bar.destinations.append(ft.NavigationBarDestination(
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
                    ft.Container(
                        content=ft.ListView(
                            controls=[ft.Text(description, selectable=True)],  
                            auto_scroll=False,  # Отключаем авто-прокрутку
                            expand=True  
                        ),
                        expand=True  
                    ),
                    ft.OutlinedButton("Назад", on_click=lambda e: navigate(None))
                ],
                expand=True,  
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
        page.update()

    
    languages = {
        "JavaScript": """JavaScript — язык программирования для веб-разработки, используется в браузерах.
        JavaScript позволяет создавать интерактивные сайты и веб-приложения. Для ввывода сообщений используется функция alert(), а для ввывод в консоль console.log().Пример кода:
        // Выводим сообщение пользователю
        alert("Привет! Это всплывающее сообщение.");

        // Выводим текст в консоль
        console.log("Этот текст появился в консоли");

        В JavaScript есть три способа объявить переменную:
        var — устаревший, но всё ещё работающий вариант.
        let — современный и предпочтительный способ.
        const — для значений, которые не изменяются.
        
        1. var — старый способ объявления переменных.
        🔹 var существовал с самого начала JavaScript и имеет некоторые проблемы, поэтому его заменили на let и const.

        Особенности var:
        ✅ Можно переопределять значение.
        ✅ Можно объявлять заново (даже в одной области видимости).
        ⚠ Переменная создаётся в глобальной области видимости или в функции.
        ⚠ Поднимается (hoisting) в начало кода, но без инициализации.
        ⚠ Игнорирует блоки {}, что может привести к ошибкам.
        
        var name = "Иван";
        console.log(name); // Иван

        var name = "Анна"; // Можно заново объявить переменную
        console.log(name); // Анна

        if (true) {
            var age = 25; // Объявлена внутри блока, но доступна ВНЕ его
        }
        console.log(age); // 25 (из-за игнорирования блока)

        2. let — безопасный способ объявления переменных
        🔹 Введён в ES6 (2015) и исправляет проблемы var.
        Особенности let:
        ✅ Можно переопределять значение.
        🚫 Нельзя объявлять заново в одной области видимости.
        ✅ Работает только в своём блоке {}.
        ✅ Поднимается (hoisting), но без инициализации.

        let city = "Москва";
        console.log(city); // Москва

        city = "Санкт-Петербург"; // Можно изменить значение
        console.log(city); // Санкт-Петербург

        if (true) {
            let country = "Россия"; 
            console.log(country); // Россия (внутри блока)
        }
        console.log(country); // ОШИБКА! (country существует только внутри блока if)

        3. const — неизменяемые переменные
        🔹 Используется для значений, которые не должны изменяться.
        Особенности const:
        🚫 Нельзя изменять значение после объявления.
        🚫 Нельзя объявлять заново в одной области видимости.
        ✅ Работает только в своём блоке {}.
        ✅ Поднимается (hoisting), но без инициализации.

        const pi = 3.14;
        console.log(pi); // 3.14

        pi = 3.1415; // ОШИБКА! (нельзя изменить значение)

        Когда использовать что?

        Используй const, если значение не должно изменяться.
        Используй let, если значение может измениться.
        Не используй var в новом коде!""",
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
            ft.ListView(
                controls=[
                    ft.OutlinedButton(text=lang, on_click=lambda e, l=lang: show_language_info(l, languages[l])) for lang in languages.keys()
                ],
                expand=True
            ),
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
            ft.NavigationBarDestination(icon=ft.Icons.VERIFIED_USER),
            ft.NavigationBarDestination(icon=ft.Icons.VERIFIED_USER_OUTLINED),
        ],
        on_change=navigate
    )

    page.add(panel_register)

ft.app(target=main)