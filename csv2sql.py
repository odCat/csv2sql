#!python

from sys import exit as sysexit
from sys import argv

def open_file(aFile):
    try:
        return open(aFile, 'r', encoding="utf-8")
    except FileNotFoundError:
        print('Wrong file or path: ' + aFile)
        sysexit()

def add_escape(value):
    return value.replace("'", "''")

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
    sql += 'from\n\t(values'
    for i in rows:
        sql += '\n\t('
        for j in i:
            if j == '':
                sql += 'null'
            elif j == 'TRUE' or j == 'FALSE':
                sql += j
            else:
                sql += "'" + add_escape(j) + "'" 
            sql += ','
        sql = sql[:-1] + '),'
    sql = sql[:-1] + '\n;'
    return sql

if __name__ == '__main__':
    if len(argv) == 2:
        f = open_file(argv[1])

        titles = get_titles(f)
        rows = get_rows(f)
        sql = generate_sql(titles, rows)

        print(sql)
    else:
        print('Usage: csv2sql file')
