from app.lib.widgets.htmltags import *
import app.lib.tools.tools as tools

def bsValueBox(meta):
    boxtype = meta['boxtype']
    icon = meta['icon']
    boxtext = meta['boxtext']
    boxvalue = str(meta['boxvalue'])
    boxlink = meta.get('boxlink', False)
    if boxlink is True:
        boxlink_html = """
        <a href="#">
            <div class="panel-footer">
            <span class="pull-left">View Details</span>
            <span class="pull-right"><i class="glyphicon glyphicon-circle-arrow-right"></i></span>
            <div class="clearfix"></div>
            </div>
        </a>
        """
    else:
        boxlink_html = """"""

    return """
<div class="row">
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
</div>
"""