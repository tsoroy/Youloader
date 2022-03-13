from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QDialog
from PyQt5.QtGui import QIcon

import pafy
import sys, os
import threading as th
# rrB13utjYV4

path = os.path.normpath(os.getenv('USERPROFILE') + '/Downloads/')

def download():
    def callback(total, recvd, ratio, rate, eta):
        ui.label.setText('')
        ui.label.setText('Скачано '\
        + str(round(recvd / 1000 / 1000)) + ' из '\
        + str(round(best.get_filesize() / 1000 / 1000)) + ' МБ')

    try:
        global best
        url = ui.entry_url.text()
        video = pafy.new(url)
        streams = video.streams
        best = video.getbest()

        ui.label.setText('')
        best.download(filepath=path, quiet=True, callback=callback)
        ui.label.setText('Видео успешно загружено')

    except ValueError:
        ui.label.setText('Введите верный адрес URL')
    except OSError:
        pass
    except RuntimeError:
        pass

def download_thread():
    downloaded = False
    while not downloaded:
        try:
            th.Thread(target=download).start()
        except RuntimeError:
            pass
        downloaded = True

def initUI():
    ui.btn_download.clicked.connect(download_thread)

    ui.btn_settings.setIcon(QIcon('settings.png'))
    # ui.btn_settings.clicked.connect(show_settings)

    ui.btn_info.setIcon(QIcon('info.png'))
    # ui.btn_info.clicked.connect(dialog_info)

def ICON_PATH(relative):
    if hasattr(tk.sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

if __name__ == '__main__':
    # создаем приложене
    app = QApplication(sys.argv)
    # создаем главное окно
    window = QMainWindow()
    # подключаем файл .ui для главного окна
    ui = uic.loadUi('main.ui', window)
    # подключаем файл стилей
    window.setStyleSheet(open("main.qss", "r").read())
    window.setWindowIcon(QIcon('icon.ico'))
    # отображаем окно
    window.show()
    # инициализируем дополнительные элементы GUI
    initUI()
    # запускаем приложение
    sys.exit(app.exec_())