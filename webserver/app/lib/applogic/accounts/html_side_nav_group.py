
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


class html_sidenav_complete(object):
    def __init__(self, title):
        self._title = title
        self._items = []
        self._groups = []
        pass

    def to_html(self):
        return widgets.side_nav(self._title, 
                                [g.to_html() for g in self._items], 
                                [g.to_html() for g in self._groups])

    def _side_nav_item(self, title, link, icon, text, isactive=False):
        return widgets.side_nav_item(title, link, icon, text, isactive)

    def add_item(self, item):
        self._items.append(
            html_sidenav_item(meta=item)
        )

    def add_group(self, group):
        self._groups.append(
            html_sidenav_group(meta=group)
        )
