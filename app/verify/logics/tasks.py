import os
from config.celery import app
from verify.logics.service import excel_check_email, txt_check_email


@app.task()
def check_email_task(file_path, file_url):
    filename, file_extension = os.path.splitext(file_url)
    if file_extension != '.txt':
        excel_check_email(file_path, file_url)
    else:
        txt_check_email(file_path, file_url)