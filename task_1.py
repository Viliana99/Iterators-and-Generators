import numpy as np


class  RleSequence:
    def __init__(self, input_sequence):
        self.seq, self.count = self.encode_rle(input_sequence)
        if type(self.count) == int:
            self.count = [self.count]
        self.len = len(input_sequence)
    
    def __getitem__(self, index):
        if isinstance(index, slice):
            start = index.start if (index.start != None) else 0
            stop = index.stop if (index.stop != None) else self.len
            step = index.step if (index.step != None) else 1
            start = start if (start >= 0) else (self.len + start)
            stop = stop if (stop >= 0) else (self.len + stop)
            self.full_off = start + step - 1
            start_f = True
            ans = []
            self.remainder = 0
            if start >= stop:
                return []
            for i,count in enumerate(self.count):
                if start_f:
                    if start < count:
                        start_f = False
                        #print('STAAART:', i, self.seq[i])
                        ans.append(self.seq[i])
                        self.remainder = start + step
                        #print(self.full_off, self.remainder, i)
                        
                        self.off = self.remainder
                        #print('vhod',self.full_off, self.off, i)
                        while (self.full_off < stop - 1) and (count > self.off):
                            #print('iiiiiii:', i, self.seq[i])
                            ans.append(self.seq[i])
                            self.off += step
                            self.full_off += step
                            #print('whi')
                        #print(self.full_off, self.remainder, i)
                        self.remainder = self.off - count
                        #print(self.full_off, self.remainder, i)
                        if self.full_off > (stop - 1):
                            break
                    else:
                        start -= count
                else:
                    self.off = self.remainder
                    #print('vhod',self.full_off, self.off, i)
                    while (self.full_off < stop - 1) and (count > self.off):
                        #print('iiiiiii:', i, self.seq[i])
                        ans.append(self.seq[i])
                        self.off += step
                        self.full_off += step
                        #print('whi')
                    #print(self.full_off, self.remainder, i)
                    self.remainder = self.off - count
                    #print(self.full_off, self.remainder, i)
                    if self.full_off > (stop - 1):
                        break
            return np.array(ans)
        else:
            index = index if index >= 0 else self.len + index
            for i,count in enumerate(self.count):
                if index < count:
                    return self.seq[i]
                else:
                    index -= count
    
    def __iter__(self):
        for kk,i in enumerate(self.count):
            for j in range(i):
                yield self.seq[kk]
            
    def __contains__(self, target_elem):
        for elem in self.seq:
            if elem == target_elem:
                return True
        return False
            
    def encode_rle(self, x):
        if np.all(x == x[0]):
            return [x[0]], len(x)
        x = np.concatenate([x,[x[len(x) - 1] + 1]])
        v = x[np.where(np.diff(x) != 0)[0]]
        i = np.hstack((np.where(np.diff(x) != 0)[0][0] + 1, np.diff(np.where(np.diff(x) != 0)[0])))
        return v, i