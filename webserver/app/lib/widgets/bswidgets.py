from app.lib.widgets.htmltags import *
import app.lib.tools.tools as tools

class inWell(object):
    def __init__(self, html=None):
        self._html = html
        
    def content(self, html):
        self._html = html

    def get(self, html=None):
        if html is not None:
            self.content(html)

        if self._html is not None:
            return """<div class="well">""" + self._html +  """</div>"""
        return False


class bsValueBox(object):
    """ Class to create a bootstrap
    value in a box """
    def __init__(self, boxes=None):
        
        self._boxes = []
        if boxes is not None:
            self.add_boxes(boxes)

    def add_boxes(self, boxes):
        for box in boxes:
            self.add_box(box)

    def add_box(self, box_meta):
        self._boxes.append(box_meta)

    def get(self):
        return self.bsValueBox_collection()
        
    def bsValueBox_collection(self):
        html = """<div class="row">"""
        for item in self._boxes:
            html += self.bsValueBox(item)
        return html + """</div>"""

    def _link_html(self, linkmeta):
        link = linkmeta['url']
        text = linkmeta['text']
        icon = linkmeta['icon']
        return """
            <a href=""""" + link + """"">
                <div class="panel-footer">
                <span class="pull-left">""" + text + """</span>
                <span class="pull-right"><i class="glyphicon glyphicon-""" + icon + """"></i></span>
                <div class="clearfix"></div>
                </div>
            </a>
            """

    def bsValueBox(self, meta):
        boxtype = meta['boxtype']
        icon = meta['icon']
        boxtext = meta['boxtext']
        boxvalue = str(meta['boxvalue'])
        boxlink = meta.get('boxlink', False)
        if boxlink is True:
            boxlink_html = self._link_html(boxlink)
        else:
            boxlink_html = """"""

        return """

    <div class="col-lg-3 col-md-6">
        <div class="panel panel-""" + boxtype + """">
        <div class="panel-heading">
            <div class="row">
            <div class="col-xs-3">
                <i class="glyphicon glyphicon-""" + icon + """" style="font-size:50px;"></i>
            </div>
            <div class="col-xs-9 text-right">
                <div style="font-size:40px;">""" + boxvalue + """</div>
                <div>""" + boxtext + """</div>
            </div>
            </div>
        </div>
        """ + boxlink_html + """
        </div>
    </div>

    """

def bsLabelInput(meta):
    icon = meta['icon']
    label = meta['label']
    id = meta['id']
    return """
            <label for="""""+id+""""">""" + label + """</label>
            <div class="input-group"> 
                <span class="input-group-addon">
                    <span class="glyphicon glyphicon-""" + icon + """" aria-hidden="true"></span>
                </span>
                <input type=text class="form-control" size=30 name="""""+id+""""" id = """""+id+""""">
            </div>
            """
