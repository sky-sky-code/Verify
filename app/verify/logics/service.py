from pathlib import Path

import pandas as pd
from verify.logics.clients import MillionVerifierClient
from app.verify.models import Verify


def format_path(path: str):
    path_list = path.split('\\')
    return '/'.join(path_list)

def excel_check_email(file_path: str, file_uid):
    df = pd.read_excel(Path(file_path))
    df_notnull = df.where(pd.notnull(df), None)
    for i, row in df_notnull.iterrows():
        client = MillionVerifierClient()
        email = row['email']
        code_response = client.check_email(email=email)
        Verify.objects.create(
            email=email,
            file= file_uid,
            result_code=code_response
        )


def txt_check_email(file_path, file_uid):
    with open(file_path, 'r') as file:
        for line in file:
            for email in line.split(','):
                if " " in email: email.replace(' ', '')
                client = MillionVerifierClient()
                code_response = client.check_email(email)
                Verify.objects.create(
                    email=email,
                    file= file_uid,
                    result_code=code_response
                )
