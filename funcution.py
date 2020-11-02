def lowestMean (mean1, mean2):
    mean1 = sum(mean1) / len(mean1)
    mean2 = sum(mean2) / len(mean2)

    return min(mean1,mean2)

mean1 = [1,2]
mean2 = [2,3]
print(lowestMean(mean1,mean2))

#-------------------------
def pytagoes (a,b):
    c = a**2+b**2
    return c

print(pytagoes(2,3))

#----------------------
def maxGrade (grades):
    maxim = grades[0]
    for element in grades:
        if maxim < element:
            maxim = element
            return maxim

grades = [1,2]
print(maxGrade(grades))

#--------------------------

# def maxGradeAndName (names, grades):
#     maxiGrade = maxGradeAndName(grades)
#     maxi = grades[0]
#     for i in range(len(maxGradeAndName)):
#         if maxi < i:
#             maxi = i
#             return names[i]
#
# names = ["sahar","omer"]
# grades = [1,2]
# print(maxGradeAndName(names,grades))

#----------------------
def is_all_letter_the_same(str_a):
    for i in range(len(str_a)):
        if str_a [i] == str_a[i-1]:
            return False
        else:
            return True


print(is_all_letter_the_same("aa"))
print(is_all_letter_the_same("ab"))