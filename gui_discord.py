from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import sys
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")

client = discord.Client()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("RAKOTOSON MALALANIRINA Tahina Lauren")
        self.setFixedSize(200, 150)

        self.label = QLabel("Text area", self)
        self.text = QLineEdit(self)
        self.label.move(10,25)
        self.text.move(10,50)
        self.text.adjustSize()

        self.button = QPushButton("Send", self)
        self.button.move(10, 75)

        self.button.pressed.connect(self.on_click)
        self.show()

        MainWindow.value = 0

    def on_click(self):
        MainWindow.retrieve = self.text.text()
        MainWindow.value = 1

class MyBot(commands.Bot):
    def _init_(self):
        self.Text = MainWindow.retrieve
        self.value = MainWindow.value

    async def on_ready(self):
        print(f"Bonjour {self.user.display_name} :)!")

    async def on_message(self, message):
        if self.value == 1:
            await message.channel.send(self.Text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()
    client = MyBot()
    client.run("OTY1ODg3NTEwMzE0MTE5MTc4.Yl5u1w.jtUkij0QyqQhNbVXy9G9l5sQY8k")
    
    #Cette commande ne fonctionne pas, je l'ai donc mis en commentaire
    #client.run(os.getenv("token"))
