# https://ideone.com/1L2cnr

# your code goes here
import math
import itertools
 
# helper functions
 
def gen_all_sequences(outcomes, length):
    '''
    function that enumerates the set of all sequences of outcomes of given length;
    original code from the lecture, do not modify
    '''
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set
 
#state = gen_all_sequences((1, 2, 3, 4), 2)
#print state, len(state)
 
 
# Question 3
 
def sequence_trials():
    '''
    fair four-sided die (with faces numbered 1-4) is rolled twice
    returns expected value of the product of the two die rolls
    '''
    state = gen_all_sequences((1, 2, 3, 4), 2)
    product = 0
 
    for item in state:
        product += item[0] * item[1]
    return product * 1 / 16.0
 
print 'Question 3 answer:', sequence_trials()
 
 
# Question 4
 
def sequence_all():
    '''
    what is the probability that this five-digit string consists of five
    consecutive digits in either ascending or descending order (e.g; "34567" or "43210")
    '''
    possibilities = gen_all_sequences((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 5)
    count = 0
 
    for item in possibilities:
        for element in item:
            if all(earlier + 1 == later for earlier, later in zip(item, item[1:])):
                count += 1
    # counter kept track of each element in item (thus 30 / 5), also must count
    # both ascending and descending sequences (thus 6 * 2)
    count /= len(item)
    return count * 2.0 / len(possibilities)
 
print 'Question 4 answer:', sequence_all()
 
 
# Question 5
 
def sequence_perm():
    '''
    what is the probability that this five-digit string consists of five
    consecutive digits in either ascending or descending order (e.g; "34567" or "43210")
    '''
    # same ascending and descending sequences (12 in total) from Question 4
    return 12.0 / (math.factorial(10) / math.factorial(10 - 5))
 
print 'Question 5 answer:', '{:03.7f}'.format(sequence_perm())
 
 
# Question 6
 
'''
function to generate permutations of outcomes, repetition of outcomes not allowed
provided at: http://w...content-available-to-author-only...r.org/#poc_permutations_template.py
'''
 
def gen_permutations(outcomes, length):
    '''
    iterative function that generates set of permutations of outcomes of length num_trials,
    repeated outcomes allowed
    '''  
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                if item not in new_seq:
                    new_seq.append(item)              
                    temp.add(tuple(new_seq))
        ans = temp
    return ans
 
 
def run_example():
 
    # example for digits
    outcome = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #outcome = [0, 1]
    #outcome = ["Red", "Green", "Blue"]
    #outcome = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
 
    length = 2
    permutations = gen_permutations(outcome, length)
    print "Computed", len(permutations), "permutations of length", str(length)
    print "Permutations were", permutations
 
 
outcome = set(['a', 'b', 'c', 'd', 'e', 'f'])
 
permutations = gen_permutations(outcome, 4)
permutation_list = list(permutations)
permutation_list.sort()
print 'Question 6 answer:', permutation_list[100]
 
 
# Question 7
 
def powerset(sets):
    '''
    just generate a power set
    sets (a tuple): original set
    returns a set of tuples
    '''
    all_set = [()]
    for item in sets:
        for subset in all_set:
            all_set = all_set + [tuple(subset) + (item, )]
 
    return all_set
 
print 'Question 7 answer:', powerset((1, 2))
 
# Question 8
 
print '\nPrep for Question 8 follows...'
print 'when n is 0:', len(powerset(())), powerset(())
print 'when n is 1:', len(powerset((1, ))), powerset((1, ))
print 'when n is 2:', len(powerset((1, 2))), powerset((1, 2))
print 'when n is 3:', len(powerset((1, 2, 3))), powerset((1, 2, 3))
print 'when n is 4:', len(powerset((1, 2, 3, 4))), powerset((1, 2, 3, 4))
print 'when n is 5:', len(powerset((1, 2, 3, 4, 5))), '(powerset output omitted, too long)'
print 'when n is 6:', len(powerset((1, 2, 3, 4, 5, 6))), '(powerset output omitted, too long)'
print 'when n is 7:', len(powerset((1, 2, 3, 4, 5, 6, 7))), '(powerset output omitted, too long)'
print 'when n is 8:', len(powerset((1, 2, 3, 4, 5, 6, 7, 8))), '(powerset output omitted, too long)', '\n'
 
 
# Question 9
 
def comb():
    '''
    what is the probability of being dealt a five card hand where all five cards are of the same suit?
    '''
    all_five = 4.0 * math.factorial(13) / (math.factorial(13 - 5) * math.factorial(5))
    combination_total = math.factorial(52) / (math.factorial(52 - 5) * math.factorial(5))
 
    return all_five / combination_total
 
print "Question 9 answer:", comb()