# Linear Telegram Bot v2

## Что делает
Telegram-бот для работы с задачами Linear:
- /start
- /new
- /tasks
- /today
- /help

## Архитектура

Telegram - {Webhook} - > ngrok HTTPS - - > n8n (Docker) - {linear-telegram-v1} - > Linear API – - > Linear

## Технологии
Telegram Bot API — получение сообщений от Telegram и взаимодействие с ботом
n8n — автоматизация и выполнение workflow
Docker / Docker Compose — запуск локального n8n
ngrok — публичный HTTPS endpoint для Telegram webhook
Linear API — интеграция с Linear
Git / GitHub — версионирование проекта

## Стек
- Python — если используется
- n8n
- Docker / Docker Compose
- Telegram Bot API
- Linear API
- ngrok

## Запуск

1. Создать .env на основе .env.example
2. Заполнить секреты
3. Запустить:

docker compose up -d

4. Проверить:

docker compose ps

После запуска локальный интерфейс n8n доступен по адресу:
http://localhost:5678

3. Workflow
## Остановка

docker compose down

## Команды

| Команда | Назначение |
|---|---|
| /start | Запустить бота |
| /stop | Остановить |
| /new | Создать задачу |
| /tasks | Список задач |
| /today | Задачи на сегодня |
| /help | Помощь |

## Error handling

Ошибки workflow обрабатываются отдельным Error Workflow.

## Структура

.
- docker-compose.yml
- .env.example
- .gitignore
- README.md
- workflows/
