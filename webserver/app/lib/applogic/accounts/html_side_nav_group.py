
import htmlreport_widgets as widgets


class html_sidenavgroup(object):
    def __init__(self, name='', icon=''):
        self._group_name = name
        self._group_icon = icon
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def get_html(self):
        return widgets.side_nav_group(self._group_name, self._group_icon, self._items)


