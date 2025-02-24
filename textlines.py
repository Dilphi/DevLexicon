languages = {
        "JavaScript": 
        """
        JavaScript — язык программирования для веб-разработки, используется в браузерах.
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
        Не используй var в новом коде!
        
        Ввод значения в переменную - prompt().
        let name = prompt("Введите ваше имя");
        """,
        "C#": "C# — язык программирования от Microsoft, используется для разработки игр и приложений.",
        "C++": "C++ — мощный язык программирования, используется в разработке игр и ПО.",
        "Python": "Python — универсальный язык программирования, удобный для начинающих.",
        "SQL": "SQL — язык запросов для работы с базами данных."
    }