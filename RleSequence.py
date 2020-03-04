import numpy as np


class  RleSequence:
    def __init__(self, input_sequence):
        self.seq, self.count = self.encode_rle(input_sequence)
    
    def __getitem__(self, index):
        if isinstance(index, slice):
            count_i = 0
            index1 = index.start
            start_f = False
            ans = np.array([])
            step_count = index.step
            remainder = 0
            for i,count in enumerate(self.count):
                if (not start_f) and (index1 < count):
                    index_seq = i
                    start_f = True
                    count_i += index1
                    if (count_i >= index.stop):
                        break
                    print('NASHELLLLLLLLLLLLLLL', count, index1, (count - 1 - index1)//index.step)
                    ans = np.append(ans, self.seq[i])
                    for _ in range((count - index1 - 1)//index.step): # +1 and ^ ubrat
                        count_i += index.step
                        if (count_i >= index.stop):
                            break
                        ans = np.append(ans, self.seq[i])
                    if (count_i >= index.stop):
                        break
                    remainder = index.step - (count - 1 - index1) % index.step
                else :
                    index1 -= count
                    print(ans, '\n', count, remainder)
                    if count - remainder >0:
                        count_tmp = count - remainder #- 1
                        print('tmp: ', count_tmp)
                        count_i += remainder
                        if (count_i >= index.stop):
                            break
                        ans = np.append(ans, self.seq[i])
                        for _ in range(count_tmp // index.step):
                            count_i += index.step
                            if (count_i >= index.stop):
                                break
                            ans = np.append(ans, self.seq[i])
                        if (count_i >= index.stop):
                            break
                        remainder = index.step - count_tmp % index.step
                    elif not (count - remainder):
                        count_i += remainder
                        if (count_i >= index.stop):
                            break
                        ans = np.append(ans, self.seq[i])
                        remainder = index.step#&???????????
                    else:
                        remainder = remainder - count
                        count_i += count
                        if (count_i >= index.stop):
                            break
        else:
            for i,count in enumerate(self.count):
                if  (count - index) > 0:
                    return self.seq[i]
                #print('ind:' , index ,' count:' , count)
                index -= count
            raise IndexError
        return ans
        
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