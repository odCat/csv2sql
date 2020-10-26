def open_file(aFile):
    return open(aFile)

def parse_columns(columns):
    return columns.split(',')

def get_titles(aFile):
    titles = aFile.readline().rstrip()
    return titles.split(',')
