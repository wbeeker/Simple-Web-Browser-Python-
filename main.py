from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class CustomWebPage(QWebEnginePage):
    def userAgentForUrl(self, url):
        return (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        )

class MyWebBrowser(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Web Browser")
        self.setGeometry(100, 100, 1200, 800)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        nav_bar = QHBoxLayout()
        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)

        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)

        self.back_btn = QPushButton("Back")
        self.back_btn.setMinimumHeight(30)

        self.forward_btn = QPushButton("Forward")
        self.forward_btn.setMinimumHeight(30)

        nav_bar.addWidget(self.url_bar)
        nav_bar.addWidget(self.go_btn)
        nav_bar.addWidget(self.back_btn)
        nav_bar.addWidget(self.forward_btn)

        self.browser = QWebEngineView()
        self.browser.setPage(CustomWebPage(self.browser))
        self.browser.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.browser.setUrl(QUrl("http://google.com"))

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        self.browser.urlChanged.connect(self.update_url_bar)


        main_layout.addLayout(nav_bar)
        main_layout.addWidget(self.browser)

        self.show()

    def navigate(self, url):
        if not url.startswith("http"):
            url = "https://" + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))

    def update_url_bar(self, q):
        self.url_bar.setText(q.toString())


if __name__ == "__main__":
    app = QApplication([])
    window = MyWebBrowser()
    app.exec_()










