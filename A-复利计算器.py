import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QSpinBox, QFormLayout, QDoubleSpinBox

class Interest(QDialog):
    def __init__(self):
        super(Interest, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('复利计算器')

        mainLayout = QFormLayout()

        self.principalSpinBox = QSpinBox()
        self.principalSpinBox.setPrefix('$')
        self.principalSpinBox.setRange(10,10000000)
        self.principalSpinBox.setSingleStep(10)
        self.principalSpinBox.valueChanged.connect(self.updateUI)
        mainLayout.addRow('本金:', self.principalSpinBox)

        self.rateSpinBox = QDoubleSpinBox()
        self.rateSpinBox.setRange(1.0,50.0)
        self.rateSpinBox.setSingleStep(0.1)
        self.rateSpinBox.setSuffix('%')
        self.rateSpinBox.valueChanged.connect(self.updateUI)
        self.rateSpinBox.resize(self.principalSpinBox.size())
        mainLayout.addRow('年利率:',self.rateSpinBox)

        self.yearsSpinbox = QSpinBox()
        self.yearsSpinbox.setRange(1,3)
        self.yearsSpinbox.setSingleStep(1)
        self.yearsSpinbox.setSuffix('年')
        self.yearsSpinbox.valueChanged.connect(self.updateUI)
        self.yearsSpinbox.resize(self.principalSpinBox.size())
        mainLayout.addRow('年数:',self.yearsSpinbox)

        self.amountLabel = QLabel()
        self.amountLabel.resize(self.principalSpinBox.size())
        mainLayout.addRow('本息和:',self.amountLabel)
        self.updateUI()

        self.setLayout(mainLayout)

    def updateUI(self):
        principal = self.principalSpinBox.value()
        rate = self.rateSpinBox.value()/100
        years = self.yearsSpinbox.value()

        amount = principal * ((1 + rate)**years)

        self.amountLabel.setText('$ %.2f'%amount)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    interest = Interest()
    interest.show()
    sys.exit(app.exec_())



