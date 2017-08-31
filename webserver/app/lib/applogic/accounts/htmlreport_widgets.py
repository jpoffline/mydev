

def make_page(head='', nav='', content='', endmatter=''):
    return """
        <!DOCTYPE html>
        <html lang="en">
            <head>""" + head + """</head>
            <body class="fixed-nav" id="page-top">
                """ + nav + """
                <div class="content-wrapper py-3">
                    <div class="container-fluid">
                    """ + content + """
                    </div>
                </div>
                """ + endmatter + """
            </body>
        </html>
        """


def value_card(card_type, icon, body, link=None, footer=None, width=3):
    if link is not None and footer is not None:
        link_part = """
        <a href=" """ + link + """ " class="card-footer text-white clearfix small z-1">
            <span class="float-left">""" + footer + """</span>
            <span class="float-right">
                <i class="fa fa-angle-right"></i>
            </span>
            </a>
            """
    elif footer is not None:
        link_part = """
        <a class="card-footer text-white clearfix small z-1">
        <span class="float-left">""" + footer + """</span></a>"""
    else:
        link_part = ''
    return """
        <div class="col-xl-""" + str(width) + """ col-sm-6 mb-3">
        <div class="card text-white bg-""" + card_type + """ o-hidden h-100">
            <div class="card-body">
            <div class="card-body-icon">
                <i class="fa fa-fw fa-""" + icon + """"></i>
            </div>
            <div class="mr-5">
                """ + body + """
            </div>
            </div>
            """ + link_part + """
        </div>
        </div>
        """


def link(url=None):
    if url is not None:
        return """<div style='height:80px;' id='""" + url + """'></div>"""
    return ''


def main_box(icon, title, body, footer, id=None):
    return link(id) + """
        <div class="card mb-3">
        <div class="card-header">
        <i class="fa fa-""" + icon + """"></i>
        """ + title + """
        </div>
        <div class="card-body">
            """ + body + """
        </div>
        <div class="card-footer small text-muted">
        """ + footer + """
        </div>
    </div>
    """


def side_nav_item(title, link, icon, text, isactive=False):
    if isactive is False:
        isactive = ''
    else:
        isactive = 'active'
    return """
        <li class="nav-item """ + isactive + """" data-toggle="tooltip" data-placement="right" title=" """ + title + """ ">
        <a class="nav-link" href='#""" + link + """'>
            <i class="fa fa-fw fa-""" + icon + """"></i>
            <span class="nav-link-text">
            """ + text + """</span>
        </a>
        </li>
        """


def static_item_link(assest_dir, item, meta=None):
    m = "rel='stylesheet'"
    if meta is not None:
        m = m + " " + meta
    return """<link href='""" + assest_dir + item + """' """ + m + """>"""

def static_item_script(assest_dir, item):
    return """<script src='""" + assest_dir + item + """'></script>"""

def head_meta(title, assest_dir='../static/'):
    return """

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <meta name="description" content="">
    <meta name="author" content="">
    <title>""" + title + """</title>



    <!-- Bootstrap core CSS -->
    """ + static_item_link(assest_dir, "vendor/bootstrap/css/bootstrap.min.css") + """
    <!-- Custom fonts for this template -->
    """ + static_item_link(assest_dir, "vendor/font-awesome/css/font-awesome.min.css", "type='text/css'") + """
    <!-- Plugin CSS -->
    """ + static_item_link(assest_dir, "vendor/datatables/dataTables.bootstrap4.css") + """
    <!-- Custom styles for this template -->
    """ + static_item_link(assest_dir, "css/sb-admin.css") + """
    """ + static_item_script(assest_dir, "js/plotly-180717.js") + """

    <!-- Bootstrap core JavaScript -->
    """ + static_item_script(assest_dir, "vendor/jquery/jquery.min.js") + """
    """ + static_item_script(assest_dir, "vendor/popper/popper.min.js") + """
    """ + static_item_script(assest_dir, "vendor/bootstrap/js/bootstrap.min.js") + """

    <!-- Plugin JavaScript -->
    """ + static_item_script(assest_dir, "vendor/jquery-easing/jquery.easing.min.js") + """
    """ + static_item_script(assest_dir, "vendor/chart.js/Chart.min.js") + """
    """ + static_item_script(assest_dir, "vendor/datatables/jquery.dataTables.js") + """
    """ + static_item_script(assest_dir, "vendor/datatables/dataTables.bootstrap4.js") + """
  """


def end_meta(assest_dir = '../static/'):
    return """
    <!-- Scroll to Top Button -->
    <a class="scroll-to-top rounded" href="#page-top">
      <i class="fa fa-angle-up"></i>
    </a>
    <!-- Custom scripts for this template -->
    """ + static_item_script(assest_dir, "js/sb-admin.min.js") + """
    """


def side_nav(title, items, groups='',top_nav=''):
    items_html = "".join(items)
    groups = "".join(groups)
    return """
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top" id="mainNav">
      <a class="navbar-brand" href="#">""" + title + """</a>
      <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarResponsive">
        <ul class="navbar-nav navbar-sidenav">
        """ + items_html + groups + """
        </ul>
        """ + top_nav + """
        <ul class="navbar-nav sidenav-toggler">
          <li class="nav-item">
            <a class="nav-link text-center" id="sidenavToggler">
              <i class="fa fa-fw fa-angle-left"></i>
            </a>
          </li>
        </ul>
      </div>
    </nav>
    """


def side_nav_group_item(info):
    link = info['link']
    label = info['label']
    icon = info['icon']
    return """
            <li>
                <a href='""" + link + """'>
                  <i class="fa fa-fw fa-""" + icon + """"></i>
                  """ + label + """
                </a>
            </li>
              """


def side_nav_group(group_name, group_icon, group_items):
    group_html = []
    for item in group_items:
        group_html.append(side_nav_group_item(
            item))
    return """
              <li class="nav-item" data-toggle="tooltip" data-placement="right" title='""" + group_name + """'>
            <a class="nav-link nav-link-collapse collapsed" data-toggle="collapse" href="#collapse""" + group_name + """">
              <i class="fa fa-fw fa-""" + group_icon + """"></i>
              <span class="nav-link-text">
                """ + group_name + """
              </span>
            </a>
            <ul class="sidenav-second-level collapse" id="collapse""" + group_name + """">
              """ + ''.join(group_html) + """
            </ul>
          </li>
        """


def pie_chart_area(icon='pie-chart', title='', content='', footer=''):
    return """
     <div class="card mb-3">
              <div class="card-header">
                <i class='fa fa-""" + icon + """'></i>
                """ + title + """
              </div>
              <div class="card-body">
                """ + content + """
              </div>
              <div class="card-footer small text-muted">
                """ + footer + """
              </div>
            </div>
    """
