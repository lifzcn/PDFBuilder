# -*- coding: utf-8 -*-

import os
import sys
import time
from PyPDF2 import PdfFileMerger
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from interface import Ui_Form


class mainWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.progressBar_Process.setProperty("value", 0)
        self.pushButton_Select.clicked.connect(self.open)
        self.pushButton_Confirm.clicked.connect(self.combine)

    def open(self, parent=None):
        os.startfile("D:\Python_Project\PDFBuilder\source")

    def combine(self, parent=None):
        target_path = "D:\Python_Project\PDFBuilder\source"
        pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]
        pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]
        str2 = self.lineEdit_Name.text()
        file_merger = PdfFileMerger()
        for pdf in pdf_lst:
            file_merger.append(pdf)
        for value in range(100):
            value += 5
            time.sleep(0.1)
            self.progressBar_Process.setProperty("value", value)
        self.lineEdit_Statement.setText("PDF文件合并完成！")
        file_merger.write("{}.pdf".format(str2))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = mainWindow()
    myWin.show()
    sys.exit(app.exec_())
