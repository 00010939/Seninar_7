# eng2uz = dict()
# eng2uz2 = {}
#
# eng2uz['one'] = "bir"
# eng2uz['Something'] = "bla"
# eng2uz['two'] = 2.6
# eng2uz2['two'] = 2.6
#
#
# print(eng2uz)
# print(eng2uz2)
#
# print(eng2uz['one'])
#
# print(len(eng2uz))
#
# print('one' in eng2uz)    #--------> BOOLEAN
#
# valz = eng2uz.values()   # ------> if there is a value
# print('bir'in valz)



#SUM OF VALUES
# myFinalMarks = {'CSF': 75, 'FunPro': 80, 'WT': 85}
#
# def calculate(finalMarks):
#      total = 0
#
#      for x in finalMarks:
#
#       total = total  + finalMarks[x]
#
#      average = total /len(finalMarks)
#
#      return average
#
#
# print(calculate(myFinalMarks))





#REPATING LETTER
# def histogram(s):
#   word = dict()   #empty dictionary is created
#   for c in s:         #it loops the letter
#    if c not in word:
#      word[c] = 1
#    else:
#     word[c] += 1
#   return word
#
#
# print(histogram('aaaffew'))
# print(histogram('aaaffew'))
# h = histogram('brontosaurus')
#
#
#
# print(h.get('a', 0))




csf = {
'cw1-weight': 0.4,
'cw1-mark':79,
'exam-weight':0.6,
'exam-mark':65
}
def calcu(finalMarks):
     total = 0

     for x in finalMarks:

      total = total  + finalMarks[x]

     return total




print(calcu(csf))









