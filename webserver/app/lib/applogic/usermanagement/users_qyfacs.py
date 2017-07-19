
def select_distinct_username(table):
    return "SELECT distinct(username) from " + table + ";"

def select_row_for_username(table, username):
    return "SELECT realname, regdate from " + table + " where username='" + username + "';"