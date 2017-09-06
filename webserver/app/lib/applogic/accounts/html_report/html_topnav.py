import htmlreport_widgets as widgets
from app.lib.applogic.accounts.dumpable import DUMPABLE


class tnav_item(object):
    def __init__(self, meta):
        self._link = meta.get('link', '#')
        self._title = meta.get('title', '')
        self._short = meta.get('short', '')
        self._body = meta.get('body', '')
        pass

    def to_html(self):
        return """
              <a class="dropdown-item" href='""" + self._link + """'>
                <strong>""" + self._title + """</strong>
                <span class="small float-right text-muted">""" + self._short + """</span>
                <div class="dropdown-message small">""" + self._body + """</div>
              </a>
              """

class tnav_collection(object):
    def __init__(self, meta={}):
        self._items = []
        self._name = meta['name']
        self._icon = meta['icon']
        self._meta = meta
        pass

    def add_item(self, item):
        self._items.append(tnav_item(item))

    def to_html(self):
        this_id = self._name + 'Dropdown'
        count = str(len(self._items))
        html = """
                  <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle mr-lg-2" href="#" id='""" + this_id + """' data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              <i class='fa fa-fw fa-""" + self._icon + """'></i>
              <span class="d-lg-none">""" + self._name + """
                <span class="badge badge-pill badge-primary">""" + count +""" items</span>
              </span>
              <span class="new-indicator text-primary d-none d-lg-block">
                <i class="fa fa-fw fa-circle"></i>
                <span class="number">""" + count + """</span>
              </span>
            </a>
            <div class="dropdown-menu" aria-labelledby='""" + this_id + """'>
                """ + ''.join([g.to_html() for g in self._items]) + """
            </div>
          </li>
          """
        return html


class html_topnav_complete(DUMPABLE):
    def __init__(self):
        self._collections = {}
        pass



    def add_collection(self, collection):
        name = collection['name']
        if name not in self._collections:
            self._collections[name] = tnav_collection(collection)

    def add_item_to_collection(self, coll_key, item):
        self._collections[coll_key].add_item(item)

    def _content(self):
        items = ''
        for _,v in self._collections.iteritems():
            items += v.to_html()

        return """
        <ul class="navbar-nav ml-auto">
          """ + items + """
          <li class="nav-item">
            <div style="width:500px;"></div>
          </li>
        </ul>
        """

    def to_html(self):
        return self._content()