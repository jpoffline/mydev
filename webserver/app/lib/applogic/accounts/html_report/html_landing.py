from app.lib.applogic.accounts.dumpable import DUMPABLE
import htmlreport_widgets as widgets
import html_sidenav as snav
import html_topnav as tnav

class htmllanding(DUMPABLE):
    def __init__(self, meta={}):
        self._title = 'Accounts'
        self._meta = meta
        self._tnav = tnav.html_topnav_complete()

    def get(self):
        return self._main_template()

    def _head(self, title):
        return widgets.head_meta(title)

    def _body(self):
        
        html = """
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top" id="mainNav">
      <a class="navbar-brand" href="#">Start Bootstrap</a>
      <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
      """ + self._tnav.to_html() + """
        </div>
        </nav>
        <h1>Howdy!</h1>
      """
        return html

    def _main_template(self):
        return widgets.make_page(head=self._head(self._title),
                                 nav='',
                                 content=self._body(),
                                 endmatter=self._endmatter()
                                 )

    def _endmatter(self):
        return widgets.end_meta()

    def content(self):
        return self._main_template()
