на вашем компьютере должен быть установлен git и docker.

первое, что вы должны сделать - это клонирование этого репозитория из GitHub на свой комп.
для этого вы должны открыть терминал и ввести эту команду: git clone https://github.com/gazik05/url_shortener.git

далее в терминале переходим в папку с проектом и вводим команду для создания docker образов: docker-compose build
как только образы будут собраны, запускаем контейнеры командой: docker-compose up -d

делаем миграции базы данных, в терминале вводим: 'docker-compose exec backend python manage.py makemigrations' и 'docker-compose exec backend python manage.py migrate'

используйте команду 'docker-compose logs -f' для проверки логов в журналах.

для приостановки docker контейнеров используйте команду 'docker-compose down'