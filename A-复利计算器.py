import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QSpinBox, QFormLayout, QGridLayout, QDoubleSpinBox


class Interest(QDialog):
    def __init__(self):
        super(Interest, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('复利计算器')

        mainGridLayour = QGridLayout()

        label1 = QLabel('本金:')
        self.principalSpinBox = QSpinBox()
        self.principalSpinBox.setPrefix('$')
        self.principalSpinBox.setRange(10, 10000000)
        self.principalSpinBox.setSingleStep(10)
        self.principalSpinBox.valueChanged.connect(self.updateUI)
        mainGridLayour.addWidget(label1, 0, 0)
        mainGridLayour.addWidget(self.principalSpinBox, 0, 1)

        label2 = QLabel('年利率:')
        self.rateSpinBox = QDoubleSpinBox()
        self.rateSpinBox.setRange(1.0, 50.0)
        self.rateSpinBox.setSingleStep(0.1)
        self.rateSpinBox.setSuffix('%')
        self.rateSpinBox.valueChanged.connect(self.updateUI)
        mainGridLayour.addWidget(label2, 1, 0)
        mainGridLayour.addWidget(self.rateSpinBox, 1, 1)

        label3 = QLabel('年数:')
        self.yearsSpinbox = QSpinBox()
        self.yearsSpinbox.setRange(1, 30)
        self.yearsSpinbox.setSingleStep(1)
        self.yearsSpinbox.setSuffix('年')
        self.yearsSpinbox.valueChanged.connect(self.updateUI)
        mainGridLayour.addWidget(label3, 2, 0)
        mainGridLayour.addWidget(self.yearsSpinbox, 2, 1)

        label4 = QLabel('本息和:')
        self.amountLabel = QLabel()
        mainGridLayour.addWidget(label4, 3, 0)
        mainGridLayour.addWidget(self.amountLabel, 3, 1)

        self.updateUI()

        self.setLayout(mainGridLayour)

    def updateUI(self):
        principal = self.principalSpinBox.value()
        rate = self.rateSpinBox.value() / 100
        years = self.yearsSpinbox.value()

        amount = principal *     ((1 + rate)**years)

        self.amountLabel.setText('$ %.2f'%amount)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    interest = Interest()
    interest.show()
    sys.exit(app.exec_())
