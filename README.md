# Fanfiction-Project Selenium (WebDriver) Testing
Тестирование имеющегося функционала проводилось по следующим тестовым сценариям:
№	1
Название:	Попытка входа с некорректными данными.
Предусловие:	Пользователь не в системе, открыта страница входа в систему («Log In»).
Последовательность действий:	
1. В поле Login ввести «random_user»;
2. Поле Password оставить пустым;
3. Нажать кнопку «Log In».
Ожидаемый результат	Пользователь не авторизован, валидация формы выдала надпись «Wrong credentials».

№	2
Название:	Попытка входа с корректными данными.
Предусловие:	Пользователь не в системе, открыта страница входа в систему («Log In»).
Последовательность действий:	
1. В поле Login ввести «tissue_12»;
2. В поле Password ввести «QWESZXCqweszxc123!»;
3. Нажать кнопку «Log In».
Ожидаемый результат	Пользователь авторизован, открыта главная страница сайта («Home»).

№	3
Название:	Выход из системы.
Предусловие:	Пользователь в системе.
Последовательность действий:	
1. Нажать на синий дропдаун в правой части меню навигации;
2. Нажать на «Log out».
Ожидаемый результат	Пользователь не авторизован, открыта главная страница сайта («Home»)