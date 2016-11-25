import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from lxml import html


class Render(QWebPage="https://familysearch.org/search/collection/results?count=20&query=%2Bdeath_place%3Aseattle~%20%2Bdeath_year%3A2001-2003~&collection_id=1202535"):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def _loadFinished(self, result):
        self.frame = self.mainFrame()
        self.app.quit()