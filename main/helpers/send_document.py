from aiogram.types import InputFile
import os


def get_all_documents(directory_name):
    walk = os.walk(directory_name)
    result = []
    for root, dirs, files in walk:
        for file in files:
            result.append(file)
    return result


def upload_document(document_name):
    return InputFile(document_name)
