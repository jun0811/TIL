################# 1번 ###########################
# def count_vowels(word):
#     vowel = 0
#     vowel += word.count('a','e')
#     vowel += word.count('e')
#     vowel += word.count('i')
#     vowel += word.count('u')
#     vowel += word.count('o')
#     return vowel

# print(count_vowels('apple'))
# print(count_vowels('banana'))
# def count_vowels(word):
#     vowel = 'AaEeIiOoUu'
#     count = 0
#     for w in word:
#         if w in vowel:
#             count +=1
#     return count

# print(count_vowels('apple'))
# print(count_vowels('banana'))
################# 2번 ################### 
# word ='   apple  1  '
# print(word.strip())
################ 3번 #####################
def only_square_area(width, height):
    area =[]
    for w in width:
        if w in height:
           area += [w*w]
    return area

print(only_square_area([32,55,64],[13,32,40,55])) 