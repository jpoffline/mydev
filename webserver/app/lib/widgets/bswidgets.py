from app.lib.widgets.htmltags import *
import app.lib.tools.tools as tools

def bsValueBox():
    return """
<div class="row">
  <div class="col-lg-3 col-md-6">
    <div class="panel panel-primary">
      <div class="panel-heading">
        <div class="row">
          <div class="col-xs-3">
            <i class="glyphicon glyphicon-comment" style="font-size:50px;"></i>
          </div>
          <div class="col-xs-9 text-right">
            <div style="font-size:40px;">26</div>
            <div>New Comments!</div>
          </div>
        </div>
      </div>
      <a href="#">
        <div class="panel-footer">
          <span class="pull-left">View Details</span>
          <span class="pull-right"><i class="glyphicon glyphicon-circle-arrow-right"></i></span>
          <div class="clearfix"></div>
        </div>
      </a>
    </div>
  </div>
</div>
"""