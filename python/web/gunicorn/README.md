
gunicorn -w 3 -b 127.0.0.1:8080 app:app


gunicorn --workers 4 \
    --timeout 60 \
    --bind  0.0.0.0:8080 \
    --limit-request-line 0 \
    --limit-request-field_size 0 \
    --max-requests 1000 app:app
