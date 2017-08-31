
import htmlreport_widgets as widgets
from dumpable import DUMPABLE
import html_topnav as tnav
import html_sidenav as snav


class html_nav_complete(DUMPABLE):
    def __init__(self, title):
        self._title = title
        self._items = []
        self._groups = []
        self._content = ''
        self._tnav = tnav.html_topnav_complete()
        pass

    def content(self):
        return self._content

    def add_top_collection(self, collection):
        self._tnav.add_collection(collection)

    def add_top_item_to_collection(self, coll_key, item):
        self._tnav.add_item_to_collection(coll_key, item)

    def to_html(self):
        self._content = widgets.side_nav(self._title, 
                                [g.to_html() for g in self._items], 
                                [g.to_html() for g in self._groups],
                                top_nav=self._tnav.to_html())
        return self.to_php_partial('menu.php')


    def add_item(self, item):
        self._items.append(
            snav.html_sidenav_item(meta=item)
        )

    def add_group(self, group):
        self._groups.append(
            snav.html_sidenav_group(meta=group)
        )
