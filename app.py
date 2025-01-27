# Перед началом работы с кодом нужно установить библиотеку Flet с помощью pip install flet. Если не получилось установить то нужно ввести команду в cmd для откытия в vs code Ctrl + Shift + ~ или же Ё на Windows и ввести venv\venv\activate либо venv/bin/activate


import flet as ft # Библеотека Flet для разработки GUI.
#Основная фукция
def main(page: ft.Page): #Функция для создания приложения, а (параметр: ft.Page) включение подсказок
        
    page.title = "" #Название приложения
    #Тема приложения.
    page.theme_mode = "dark" # Можно изменить на сетлую light
    #Вертикальное расположение элементов.
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # Все элементы будут по центру
    
    # Вывод текста ft.Text('текст который нужно вывести', color='цвет'). Если не указывать цвет, то подберётся цвет изходя из выбранной темы
    user_label = ft.Text('Info')
    # Поле дял ввода 
    user_input = ft.TextField(value="0", width=150, text_align=ft.TextAlign.CENTER) # value первоначальное значение, width для указания ширины, text_align=ft.TextAlign.CENTER расположение текста
    
    def get_info(e):
        user_label.value = user_input.value
        page.update()
    
    page.add( #Вывод объектов на окно
        ft.Row( #Создание определённого ряда в приложении
            [ #Для указания создания списка выводва элементов используются []
                ft.IconButton(ft.Icons.PLAY_ARROW, on_click=get_info), # Элемент иконки которую можно нажать
                ft.Icon(ft.Icons.PAUSE), # Просто иконки
                ft.ElevatedButton(text='Нажми меня', on_click=get_info),
                ft.OutlinedButton(text='Нажми меня', on_click=get_info)          
            ],
            alignment=ft.MainAxisAlignment.CENTER # Горизонтальное расположения элементов
        ),
        ft.Row(
            [   
                user_label,
                user_input
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
# Запуск функции при запуске приложения
ft.app(target=main) # Можно из обычного приложения сделать веб-приложение, после main помтавить запятую и написать view=ft.AppView.WEB_BROWSER