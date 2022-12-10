class listManipulations:
    def __init__(self,i,b):
        self.i = i
        self.b = b
    def objectMaxFrequency(list1):
        maxvalue = -100000000000000
        for c in list1:
            if c > maxvalue:
                maxvalue = c
            else:
                continue
        return maxvalue
    def certainFrequency(list1,value):
        frequencycount = 0
        for i in list1:
            if i == value:
                frequencycount += 1
            else:
                continue
        return frequencycount
    def certainFrequencies(list1, listofvalues):
        frequencycount = 0
        for i in list1:
            if i in listofvalues:
                frequencycount += 1
            else:
                continue
        return frequencycount


class dictionaryManipulations:
    def __init__(self,a):
        self.a = a
    def dictFrequencies(list1):
        count = {}
        for i in list1:
            reps = count.get(i, 0) + 1
            count[i] = reps
        return count
    def dictSecondMax(list1,frequencyornumber):
        fm, sm, = -1, -1
        fn, sn = None, None
        #find the frequencies
        count = {}
        for i in list1:
            reps = count.get(i, 0) + 1
            count[i] = reps
        #return the second most frequent number after evaluation


        for k, v in count.items():
            if v > fm:
                sm = fm
                sn = fn
                fm = v
                fn = k
            elif v > sm:
                sm = v
                sn = k
        """
        Siddhu Notes: If there are two numbers with the same frequency, and the frequency or number variable is "n", 
        then only one of the numbers is returned. It is usually the bigger of the two. 
        
        """
        if frequencyornumber == "f":
            return sm
        elif frequencyornumber == "n":
            return sn
        else:
            return sm,sn
