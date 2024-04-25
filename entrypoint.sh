# Запуск Redis
apt update
apt install redis-server
redis-server --port 6379 &

# Ожидание запуска Redis (дополнительная команда, если необходимо)
sleep 5

python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 4 --timeout 60

# Запускаем Celery worker
celery -A config worker --loglevel=info --detach

# Запускаем Celery beat
celery -A config beat --loglevel=info --detach

# Ожидаем завершения Gunicorn (или любого другого процесса, запущенного перед)
wait -n

