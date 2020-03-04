def untwist(l, k):
        if type(l) == list:
            for el in l:
                if type(el) == list:
                    k = untwist(el, k)
                else:
                    if (type(el) == range) or (type(el) == str) or (type(el) == tuple):
                        k += list(el)
                    else:
                        k.append(el)
        else:
            if (type(el) == range) or (type(el) == str) or (type(el) == tuple):
                k += list(el)
            else:
                k.append(el)
        return k

class linearize:
    def __init__(self, slit_list):
        self.new_list = []
        for item in slit_list:
            if type(item) == int:
                self.new_list.append(item)
            elif (type(item) == range) or (type(item) == str) or (type(item) == tuple):
                self.new_list += list(item)
            elif type(item) == list:
                k = []
                self.new_list += list(untwist(item, k))
            else:
                self.new_list.append(item)
    
    def __iter__(self):
        self.i = -1
        return self
    
    def __next__(self):
        self.i +=1
        if len(self.new_list) > self.i:
            return(self.new_list[self.i])
        raise StopIteration