import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Wetterdaten-Anzeige')
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel()
        layout.addWidget(self.label)

        self.refresh_button = QPushButton('Daten aktualisieren')
        self.refresh_button.clicked.connect(self.refresh_data)
        layout.addWidget(self.refresh_button)

        self.setLayout(layout)

    def refresh_data(self):
        # Hier einfügen: Code zum Abrufen der Wetterdaten und Aktualisieren der Anzeige
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())