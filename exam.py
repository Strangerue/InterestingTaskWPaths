inp = open('C://Users//Strange//Desktop//text.txt', 'r')
out = open('C://Users//Strange//Desktop//text1.txt', 'w')

class Direct:
    def __init__(self, a, c):
        self.name = a.split()[0]
        self.inner = []
        self.depth = len(c)
        self.is_file = (a == a.lower())
        self.w = 0
        if self.is_file and len(a.split()) > 1:
            self.w = a.split()[1]
    
    def get_child(self, s):
        for o in self.inner:
            if o.name == s:
                return o
        return False
    
    def add_child(self, a, c):
        o = Direct(a, c)
        self.inner.append(o)
        self.sorter()
        return o
    
    def print_in(self):
        print(' ' * (self.depth - 1) + self.name)
        out.write(' ' * (self.depth - 1) + self.name + '\n')
        for o in self.inner:
            o.print_in()
            
    def sorter(self):
        files = []
        dirs = []
        for o in self.inner:
            if o.is_file:
                files.append([o, o.w])
            else:
                dirs.append(o)
        files.sort(key=lambda x: x[0].name)
        files.sort(key=lambda x : x[1], reverse = True)
        dirs.sort(key=lambda x: x.name)
        self.inner = dirs + [i[0] for i in files]

obj = Direct('root', [])
obj1 = obj
a = []

for l in inp:
    i = l.replace('\n', '').split('\\')
    path = []
    for j in i:
        path.append(j)
        if obj.get_child(j):
            obj = obj.get_child(j)
        else:
            obj = obj.add_child(j, path)
    obj = obj1
    
for obj in obj1.inner:
    obj.print_in()