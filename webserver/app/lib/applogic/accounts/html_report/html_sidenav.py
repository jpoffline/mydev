
import htmlreport_widgets as widgets

class html_sidenav_group(object):
    def __init__(self, meta={}, name='', icon='', items=[]):
        self._group_name = meta.get('name', '')
        self._group_icon = meta.get('icon', '')
        self._items = meta.get('items', [])

    def add_item_to_group(self, item):
        self._items.append(item)

    def to_html(self):
        return widgets.side_nav_group(self._group_name, self._group_icon, self._items)


class html_sidenav_item(object):
    def __init__(self, meta={}):
        self._title = meta['title']
        self._link = meta['link']
        self._icon = meta['icon']
        self._title = meta['title']
        self._isactive = meta.get('isactive', False)
        pass

    def _side_nav_item(self):
        return widgets.side_nav_item(self._title, self._link,
                                     self._icon, self._title, self._isactive)

    def to_html(self):
        return self._side_nav_item()
