import glob
import os
import userpaths as usr


filepath = os.path.join(usr.get_my_documents(), 'temp')
os.makedirs(filepath, exist_ok=True)

landzonepath = os.path.join(filepath, 'landing zone')
os.makedirs(landzonepath, exist_ok=True)

credspath = os.path.join(os.path.dirname(__file__).replace('utils', 'googleapis'), 'credentials.json')


def kill_folders():
    try:
        [os.remove(os.path.join(landzonepath, i)) for i in os.listdir(landzonepath)]
        os.rmdir(landzonepath)
        os.rmdir(filepath)
    except PermissionError:
        print(f"ERRO: Permissão negada para exclusão das pastas locais. Lista de pastas a serem excluídas:\n {landzonepath}\n {filepath}")

