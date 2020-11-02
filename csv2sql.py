#!python3

def open_file(aFile):
    return open(aFile)

def add_escape(value):
    return value.replace("'", "\\'")

def parse_columns(columns):
    return columns.split(',')

def get_titles(aFile):
    titles = aFile.readline().rstrip()
    return parse_columns(titles)

def get_rows(aFile):
    lines = aFile.readlines()
    rows = []
    for i in lines:
        rows.append(parse_columns(i.rstrip()))
    return rows

def generate_sql(titles, rows):
    sql = 'select'
    count = 1
    for i in titles:
        sql += '\n\tcolumn' + str(count) + ' as ' + i + ','
        count += 1
    sql = sql[:-1] + '\n'
    sql += 'from values'
    for i in rows:
        sql += '\n\t('
        for j in i:
            if j == '':
                sql += 'null,'
            else:
                sql += "'" + add_escape(j) + "'," 
        sql = sql[:-1] + '),'
    sql = sql[:-1] + '\n;'
    return sql

if __name__ == '__main__':
    pass
