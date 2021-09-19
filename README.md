# Обрезка ссылок с помощью Битли

Этот проект создан для того, что бы вы могли сокращать ссылки и узнавать сколько людей 
перешло по ссылке. 

### Как установить

Создайте файл .env и далее вам надо зайти на сайт [бит ли](https://bitly.com/), далее вы должны получить токен
и вставить в env 
```
BITLY_TOKEN='ваш токен'
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как запустить код

для того чтобы код работал, надо открыть терминал и написать

```
python main.py 'ссылка которую надо сократить'
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
