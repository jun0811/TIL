class ClassHelper:
    
    def __init__(self, member):
        self.member = member
        print(self.member)
    def pick(self, n):
        random.shuffle(self.member)
        return self.member[:n]
    
    def match_pair(self):
        random.shuffle(self.member)
        #print(len(self.member))
        if len(self.member)%2==0:
            pair =  [self.member[i:2+i] for i in range(0,len(self.member),2)]
            return pair
        else:
            pair = [self.member[i:2+i] for i in range(0,len(self.member)-3,2)]
            pair.append(self.member[len(self.member)-3:])
            return pair
   # 아래에 코드를 작성하시오.

   ch = ClassHelper(['김싸피', '이싸피', '조싸피', '박싸피', '정싸피'])

   print(ch.match_pair())