# Linear Telegram Bot

Интеграционный проект, который связывает Telegram-бота, n8n и Linear.

## Что делает проект

Telegram-бот получает сообщения через Telegram Bot API. Webhook от Telegram приходит в локальный экземпляр n8n через публичный HTTPS endpoint ngrok.

В n8n workflow `linear-telegram-v1` обрабатывает входящие сообщения и взаимодействует с Linear API.

Проект предназначен для изучения и практической отработки интеграций, автоматизации и работы с API.

## Архитектура

text
Telegram - {Webhook} - > ngrok HTTPS - - > n8n (Docker) - {linear-telegram-v1} - > Linear API – - > Linear

## Технологии
Telegram Bot API — получение сообщений от Telegram и взаимодействие с ботом
n8n — автоматизация и выполнение workflow
Docker / Docker Compose — запуск локального n8n
ngrok — публичный HTTPS endpoint для Telegram webhook
Linear API — интеграция с Linear
Git / GitHub — версионирование проекта

## Структура проекта
linear-telegram-bot/
├── workflows/
│   └── linear-telegram-v1.json
├── docs/
├── .env.example
├── .gitignore
├── docker-compose.yml
└── README.md

Runtime-данные n8n хранятся в Docker volume и не находятся в Git.

## Запуск
1. Подготовить переменные окружения

Создать .env на основе .env.example:

cp .env.example .env

Заполнить необходимые значения:

N8N_HOST
N8N_PROTOCOL
WEBHOOK_URL
TELEGRAM_BOT_TOKEN
LINEAR_API_KEY

Файл .env не добавляется в Git.

2. Запустить n8n
docker compose up -d

Проверить состояние:

docker compose ps

После запуска локальный интерфейс n8n доступен по адресу:
http://localhost:5678

3. Workflow

Основной workflow:

workflows/linear-telegram-v1.json

Workflow можно импортировать в n8n через интерфейс.

Credentials для Telegram и Linear должны быть настроены непосредственно в n8n.

ngrok

Telegram должен иметь доступ к публичному HTTPS webhook endpoint.

В текущей локальной конфигурации ngrok проксирует запросы к n8n:

Telegram → ngrok → localhost:5678

Публичный URL должен быть указан в WEBHOOK_URL.

Безопасность

Секреты и runtime-данные не хранятся в Git:

.env
Telegram Bot Token
Linear API Key
n8n database
n8n logs
Docker volume
локальные backup-файлы

Для настройки окружения используется .env.example.

Текущий статус

MVP-инфраструктура настроена:

 Git repository
 Docker / Docker Compose
 локальный n8n
 persistent Docker volume
 Telegram integration
 Linear integration
 ngrok webhook endpoint
 linear-telegram-v1 workflow
 расширение набора Telegram-команд
 дальнейшая автоматизация работы с Linear
