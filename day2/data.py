class Data:
    def __init__(self, rows):
        self.rows = rows

    @property
    def rows(self):
        return self.rows

class Row:
    def __init__(self, element):
        self.element = element

    @property
    def max(self):
        max = 0
        for i in self.element:
            if i > max:
                max = i
        return int(max)

    @property
    def min(self):
        min = 10000
        for i in self.element:
            if i < min:
                min = i
        return int(min)

    @property
    def content(self):
        return self.element
        

def parse(data):
    rows = []
    raw_rows = data.split('\n')
    for raw_row in raw_rows:
        ei = []
        for e in raw_row.split('\t'):
            ei.append(int(e))
        rows.append(Row(ei))
    return Data(rows)