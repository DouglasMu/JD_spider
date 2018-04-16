import sys

from PyQt5.QtGui import QIcon, QFont  # 创建图标
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton


# if __name__ == "__main__":
#     # 创建一个应用程序对象
#     app = QApplication(sys.argv)
#     # QWidget 提供默认的构造函数
#     w = QWidget()
#     w.resize(150,150)
#     w.move(300,300)
#     w.show()
#
#
#     sys.exit(app.exec_())
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('楷体', 14))
        self.setToolTip('这是一个<b>QWidge</b>控件')
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('工具提示')
        self.setWindowIcon(QIcon('E:\h10.png'))
        btn = QPushButton('按钮', self)
        btn.setToolTip('这是一个<b>QPushButton</b>控件')
        btn.resize(btn.sizeHint())
        btn.move(80, 60)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
