                                                  PeerPro


Цель проекта
Данный сервис будет помогать командам разработчиков писать отчеты о своей работе чтобы улучшить менеджмент команд

Стэк - технологии:
- PostreSQL
- Python 3.10
- Django Rest Framework
- Docker Compose

Задеплоенный проект:
https://peer.pythonanywhere.com/



                                              Настройка проекта
                                              
 Склонируйте проект:
 
 git clone https://github.com/iimgera/PeerPro.git
 
 
Установите и активируйте виртуальное окружение:

python3 -m venv venv
source venv/bin/activate


Создайте и запустите docker compose:

docker compose build
docker ps (для просмотра id контейнера)

docker exec -it <container id> bash

Сделайте миграции:

python manage.py makemigrations
python manage.py migrate

Создайте суперюзера в Админ панели Django:

python manage.py createsuperuser

Запустите контейнер:

docker compose up


