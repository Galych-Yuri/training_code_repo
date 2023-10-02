# PIP
# pip У ньому прописані всі легальні існуючі бібліотеки

# pip --version -V   - checks version pip

# pip install [package_name], якщо треба встановити конкретну версію (package_name==1.0.1)

# pip install -r requirements.txt  - install all package in file

# pip freeze  - checks what package install
# pip freeze > requirements.txt  - Зберігає у файл всі встановлені сторонні бібліотеки.
# Зручно тим що зберігаються коди версій цих бібліотек

# pip uninstall [package_name]

# ----------

"""
За допомогою PIP встановити такі пакети:
requests (версії 2.26.0);
lxml (останньої версії).
Записати встановлені залежності у файл requirements.txt.
Видалити ці залежності і потім встановити їх із файлу requirements.txt.
Для перевірки надіслати файл requirements.txt і скріншот виконаних дій.
"""


import subprocess


def uninstall_all_packages():
    # Вивести список всіх встановлених бібліотек Python та їх версій
    output = subprocess.check_output(['pip', 'freeze']).decode()
    installed_packages = [line.split('==')[0] for line in output.split('\n') if line]

    # # Видалити кожну бібліотеку окремо
    for package in installed_packages:
        subprocess.call(['pip', 'uninstall', '-y', package])


uninstall_all_packages()

# Вивести список всіх встановлених бібліотек Python та їх версій

# Видалити кожну бібліотеку окремо
