#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QMainWindow,
    QLabel, QApplication, QGridLayout, QPushButton, QAction, QDesktopWidget)
from PyQt5.QtGui import QPixmap, QIcon
# from first_step import FirstStep
from PyQt5.QtCore import QCoreApplication
import os
import inspect
import pygame


class Game(QWidget):

    dir = os.path.dirname(os.path.abspath(__file__))
    # dir = dir.replace('\\', '/')

    def __init__(self):
        super().__init__()

        self.initUI()
        self.music()


    def initUI(self):


        # Получаем путь до файла
        self.center()
        # Размещаем нашу программу по центру
        vbox = QVBoxLayout(self)
        # Главный макет окна

        pixmap = QPixmap(os.path.join(self.dir, "images/logo.jpg"))
        # QPixMap – это один из виджетов, использующихся для работы с изображениями.
        # Он оптимизирован для показа изображений на экране.

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        # Мы поместили изображение в виджет QLabel.

        # Текст квеста
        vbox.addWidget(lbl)

        # Макет с кнопками действий
        hbox = QHBoxLayout(self)

        # TODO Кнопка старта
        startBtn = QPushButton('Начать', self)
        startBtn.resize(startBtn.sizeHint())
        hbox.addWidget(startBtn)

        # Событие кнопки старта
        startBtn.clicked.connect(self.buttonClicked)

        # Помешение кнопки в главный макет
        vbox.addLayout(hbox)

        # TODO Установка главного макета в программу
        self.setLayout(vbox)

        # Название, иконка
        self.setWindowTitle('One shot')
        self.setWindowIcon(QIcon(os.path.join(self.dir, 'images/icon.png')))


        # Отображение
        self.show()

    def center(self):
        # Метод, центрирующий окно по центру
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        # В первой строчке мы получаем размеры нашего окна
        # Во второй строке мы: получаем разрешение экрана, определяем его центр
        # В третьей строке мы создаем прямоугольник,
        # состоящий из четырех прямоугольников нашего приложения. Назовём его Основным.
        # Левый верхний прямоугольник Основного прямоугольника распологается точно по центру экрана
        # Функцией move() в четвертой строке мы перемещаем наше приложение
        # по координатам этого прямоугольника

    def music(self):
        """Программа включает песню"""
        pygame.init()
        pygame.mixer.music.load(os.path.join(self.dir, 'music\logo-song.mp3'))
        pygame.mixer.music.play()

    def buttonClicked(self):
        """Событие кнопки startButton"""

        pygame.mixer.music.stop()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Game()
    sys.exit(app.exec_())