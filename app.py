import flet as ft  # Библиотека Flet для разработки GUI.
import sqlite3

def main(page: ft.Page):  # Функция для создания приложения
        
    page.title = "DevLexicon"  # Название приложения
    page.theme_mode = "dark"  # Можно изменить на светлую light
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Все элементы будут по центру

    # Исправленные параметры окна
    page.window.width = 350
    page.window.height = 400
    page.window.resizable = False

    # Определение полей ввода
    student_name = ft.TextField(label='Имя', width=200, on_change=lambda e: validate())
    student_surname = ft.TextField(label='Фамилия', width=200, on_change=lambda e: validate())
    student_group = ft.TextField(label='Группа', width=150, on_change=lambda e: validate(), text_align=ft.TextAlign.CENTER)
    btn_reg = ft.OutlinedButton(text='Начать', width=150, on_click=lambda e: register(), disabled=True)

    # Функция для регистрации пользователя
    def register():
        db = sqlite3.connect('student.mab')
        cur = db.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                groub TEXT NOT NULL
            )
        """)
        cur.execute(
            "INSERT INTO students (name, surname, groub) VALUES (?, ?, ?)", 
            (student_name.value, student_surname.value, student_group.value)
        )

        db.commit()
        db.close()

        # Очистка полей ввода после регистрации
        student_name.value = ''
        student_surname.value = ''
        student_group.value = ''
        btn_reg.text = 'Успешно!'
        btn_reg.disabled = True  # Делаем кнопку неактивной после регистрации

        page.update()

    # Функция проверки заполненности полей
    def validate():
        if all([student_name.value, student_surname.value, student_group.value]):
            btn_reg.disabled = False
        else:
            btn_reg.disabled = True
        page.update()

    # Функция смены темы
    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()

    # Добавление виджетов на страницу
    page.add(
        ft.Row([ft.IconButton(ft.Icons.SUNNY, on_click=change_theme)]),
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Text('Начало тестирования'),
                        student_name,
                        student_surname,
                        student_group,
                        btn_reg
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER  # Горизонтальное расположение элементов
        )
    )

# Запуск функции при запуске приложения
ft.app(target=main)  # Можно из обычного приложения сделать веб-приложение, добавив view=ft.AppView.WEB_BROWSER
