# a = '123'
# b= 123
# c= [1,2,3]
# d= ['1','2','3']


# def reverse():
#     l = len(s)
#     t = list(s)
#     for i in range(10):
#         t[i], t[l-i-1] = t[l-i-1], t[i]
import sys
sys.stdin = open('input.txt','r')

T = int(input())
for test_case in range(1,T+1):
    N = list(input().split())
    string = input().split()
    numbers = [0]*10
    list_string = list(string)
    for st in list_string:
        # print(numbers)
        if st == "ZRO":
            numbers[0] += 1 
        elif st == "ONE":
            numbers[1] += 1 
        elif st == "TWO":
            numbers[2] += 1 
        elif st == "THR":
            numbers[3] += 1 
        elif st == "FOR":
            numbers[4] += 1 
        elif st == "FIV":
            numbers[5] += 1 
        elif st == "SIX":
            numbers[6] += 1 
        elif st == "SVN":
            numbers[7] += 1 
        elif st == "EGT":
            numbers[8] += 1 
        elif st == "NIN":
            numbers[9] += 1 
    temp = []
    temp.append('ZRO '* numbers[0])
    temp.append('ONE '* numbers[1])
    temp.append('TWO '* numbers[2])
    temp.append('THR '* numbers[3])
    temp.append('FOR '* numbers[4])
    temp.append('FIV '* numbers[5])
    temp.append('SIX '* numbers[6])
    temp.append('SVN '* numbers[7])
    temp.append('EGT '* numbers[8])
    temp.append('NIN '* numbers[9])
    print('#{}'.format(test_case))
    print('{}'.format(''.join(temp)))


####
T = int(input())
 
new = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
 
for tc in range(1,T+1):
    t, N = input().split()
    t = int(t[1:])
    temp = []
    result = []
    input_list = input().split()
 
    for i in input_list:
        temp.append(new.index(i))
    
    temp.sort()
 
    for i in temp:
        result.append(new[i])
    print('#{}'.format(t))
    print(' '.join(result))