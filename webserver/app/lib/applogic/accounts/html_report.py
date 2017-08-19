
import htmlreport_widgets as widgets
import html_side_nav_group as snav


class htmlreport(object):
    def __init__(self, meta={}):
        self._title = meta.get('title', 'Admin')
        self._cards = meta.get('cards', None)
        self._update_datetime = meta.get('update', '')
        self._sidenav_items = []
        self._main_boxes = []
        self._side_nav_groups = []
        self._value_cards = []
        self._top_matter = ''
        self._snav = snav.html_sidenav_complete('Admin')
        self._pie_charts = []
        pass

    def add_main_box(self, info):
        self._main_boxes.append(
            self._main_box(info['icon'], info['title'],
                           info['content'],
                           info.get('footer', 'last update ' +
                                    self._update_datetime),
                           info.get('id', None))
        )

    def add_value_card(self, info):
        self._value_cards.append(
            self._value_card(info['state'], info['icon'],
                             info['body'], info.get('link', None), 
                             info.get('linklabel', None)
                             )
        )

    def add_side_nav_item(self, info):
        self._snav.add_item(info)

    def add_side_nav_group(self, group):
        self._snav.add_group(group)

    def add_pie(self, pie=None, title='',footer=''):
        if footer == '':
            footer = 'last update ' +self._update_datetime
        self._pie_charts.append(
            widgets.pie_chart_area(
                content=pie,title=title,
                footer=footer
                )
        )

    def get(self):
        return self._main_template()

    def _main_template(self):
        return widgets.make_page(self._head(self._title),
                                 self._snav.to_html(),
                                 self._content(),
                                 self._endmatter()
                                 )

    def set_top_matter(self, matter):
        self._top_matter = matter

    def _content(self):
        return self._breadcrumbs(self._top_matter) + \
            """<div class="row">
                <div class="col-lg-4">
                   <div class="row">""" +\
                      ''.join(self._value_cards)+\
                """</div>
                </div>""" +\
            """<div class="col-lg-8">""" +\
                ''.join(self._pie_charts) +\
             """</div>
             </div>""" +\
                ''.join(self._main_boxes)

    def _value_card(self, card_type, icon, body, link, footer):
        return widgets.value_card(card_type, icon, body, link, footer,width=6)

    def _main_box(self, icon, title, body, footer, id=None):
        return widgets.main_box(icon, title, body, footer, id)

    def _head(self, title):
        return widgets.head_meta(title)

    def _endmatter(self):
        return widgets.end_meta()

    def _breadcrumbs(self, items):

        crbs = []
        for item in items:
            crbs.append("""<li class="breadcrumb-item">""" +
                        item + """</li>""")
        return """
        <ol class="breadcrumb">
          """ + ''.join(crbs) + """
        </ol>
        """
