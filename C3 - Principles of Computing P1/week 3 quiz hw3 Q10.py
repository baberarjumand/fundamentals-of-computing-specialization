"""
Program to catch incorrect input to format() function
Answer to Week 3 Quiz Q10
TEST_CASES = [0, 11, 321, 613, 5999, 10, 100, 670]
"""

# Replace the bad format format with the function shown by OwlTest

#def bad_format(t):
#    a = (t // 600)
#    b = (((t % 600) / 10) / 10)
#    c = '0'
#    if (t > 10):
#        c = str(t)[(-2)]
#    d = str(t)[(-1)]
#    formatedTime = (((((str(a) + ':') + str(b)) + c) + '.') + d)
#    return formatedTime

def bad_format(t):
    if (t <= 9):
        A = '0'
        B = '0'
        C = '0'
    elif (len(str(t)) == 2):
        A = '0'
        B = '0'
        C = (t // 10)
    else:
        A = (t // 600)
        t = (t % 600)
        if (len(str(t)) == 3):
            B = ((t // 10) // 10)
            C = ((t // 10) % 10)
        elif (len(str(t)) < 3):
            if (t <= 59):
                B = '0'
                C = (t // 10)
            else:
                B = (((t % 60) // 10) % 10)
                C = (t // 10)
    D = (t % 10)
    return (((((str(A) + ':') + str(B)) + str(C)) + '.') + str(D))


def good_format(t):
    a = t / 600
    b = t / 100 % 6
    c = t / 10 % 10
    d = t % 10
    return str(int(a)) + ":" + str(int(b)) + str(int(c)) + "." + str(int(d))

TEST_CASES = []
for n in TEST_CASES:
    print 'good: '+good_format(n)+'\nbad:  '+bad_format(n)
    
print('-----------------------------')


mistake_found = False
wrong_list = []

def Checker():
    TEST_CASES = list(range(6000))
    mistake_found = False
    while not mistake_found:
        for item in TEST_CASES:
            bad_result = bad_format(item)
            good_result = good_format(item)
            for str_idx in range(6):
                if bad_result[str_idx] != good_result[str_idx]:
                    mistake_found = True
            if mistake_found:
                print 'wrong: '+str(item)
                return 'Mistake at list index ' + str(item) + '\n' + 'Returned ' + bad_result + '\n' + 'Expected ' + good_result            
print Checker()
