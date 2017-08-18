
import htmlreport_widgets as widgets


class htmlreport(object):
    def __init__(self, meta={}):
        self._title = meta.get('title', 'Admin')
        self._cards = meta.get('cards', None)
        self._update_datetime = meta.get('update', '')
        self._sidenav_items = []
        self._main_boxes = []
        self._side_nav_groups = []
        self._top_matter = ''
        pass

    def get(self):
        return self._main_template()

    def _main_template(self):
        return """
        <!DOCTYPE html>
        <html lang="en">
            <head>""" + self._head(self._title) + """</head>
            <body class="fixed-nav" id="page-top">
                """ + self._side_nav() + """
                <div class="content-wrapper py-3">
                    <div class="container-fluid">
                    """ + self._content() + """
                    </div>
                </div>
                """ + self._endmatter() + """
            </body>
        </html>
        """

    def set_top_matter(self, matter):
        self._top_matter = matter

    def _content(self):
        return self._breadcrumbs({}) + self._top_matter + """

    <!-- Icon Cards -->
        <div class="row">
          """ + \
            self._value_card('primary', 'comments',
                             '26 New Messages!', '#', 'View Details') + \
            self._value_card('warning', 'list',
                             '11 New Tasks!', '#', 'View Details') + \
            """</div>""" + \
            ''.join(self._main_boxes)

    def add_main_box(self, info):
        self._main_boxes.append(
            self._main_box(info['icon'], info['title'],
                           info['content'],
                           info.get('footer', 'last update ' +
                                    self._update_datetime),
                           info.get('id', None))
        )

    def add_side_nav_item(self,info):
        self._sidenav_items.append(
            self._side_nav_item(
                info['title'],
                info['link'],
                info['icon'],
                info['title']
            )
        )

    def _value_card(self, card_type, icon, body, link, footer):
        return widgets.value_card(card_type, icon, body, link, footer)

    def _main_box(self, icon, title, body, footer, id=None):
        return widgets.main_box(icon, title, body, footer, id)

    def _head(self, title):
        return widgets.head_meta(title)

    def _endmatter(self):
        return widgets.end_meta()

    def _side_nav_item(self, title, link, icon, text, isactive=False):
        return widgets.side_nav_item(title, link, icon, text, isactive)

    def _breadcrumbs(self, items):
        return """
        <ol class="breadcrumb">
          <li class="breadcrumb-item">
            <a href="#">fhdjsk</a>
          </li>
          <li class="breadcrumb-item">
            <a href="#">Dashboard</a>
          </li>
          <li class="breadcrumb-item active">My Dashboard</li>
        </ol>
        """

    def _side_nav(self, title='Admin'):
        return widgets.side_nav(title, self._sidenav_items, self._side_nav_groups)

    def _side_nav_group(self):

        group_name = 'Components'
        group_icon = 'wrench'

        group_items = [
            {
                'link': '',
                'label': 'Static Navigation'
            }, {
                'link': '',
                'label': 'Custom Card Examples'
            }
        ]

        return widgets.side_nav_group(group_name, group_icon, group_items)

    def add_side_nav_group(self, group):
        self._side_nav_groups.append(
            widgets.side_nav_group(group['name'], group['icon'], group['items'])
        )