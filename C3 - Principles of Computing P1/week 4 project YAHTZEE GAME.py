"""
http://www.codeskulptor.org/#user47_WAmUZrzQ4t_7.py
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
#import poc_simpletest as tsuite

codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
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

# testing gen_all_sequences()
#for outcome in gen_all_sequences([1,2,3], 2):
#    print outcome

def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand    

    Returns an integer score 
    """
    
    occurrences_of_die = {}
    max_score = 0
    
    for die in hand:
        if occurrences_of_die.has_key(die):
            occurrences_of_die[die] += 1
        else:
            occurrences_of_die[die] = 1
            
    for key, value in occurrences_of_die.items():
        if (key * value) > max_score:
            max_score = key * value
    
    return max_score

# testing score()
#Tests = tsuite.TestSuite()
#
#input = (6,4,1,4,6)
#expected = 12
#Tests.run_test(score(input), expected, 'Testing score()')
#
#input = (1,1,1,4,6)
#expected = 6
#Tests.run_test(score(input), expected, 'Testing score()')
#
#input = (1,1,1,1,2)
#expected = 4
#Tests.run_test(score(input), expected, 'Testing score()')
#
#input = (1,1,1,1,1)
#expected = 5
#Tests.run_test(score(input), expected, 'Testing score()')
#
#Tests.report_results()

def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    sum_score = 0.0
    
    possible_hands_of_free_dice = gen_all_sequences(range(1, (num_die_sides + 1)), num_free_dice)

    for possible_hand in possible_hands_of_free_dice:
        sum_score += score(list(held_dice) + list(possible_hand))
        
    return sum_score / float(len(possible_hands_of_free_dice))    
    

#print expected_value((2,2), 6, 2)
# testing expected_value()
#Tests = tsuite.TestSuite()
#
#input = ((1,), 2, 1)
#expected = 2.0
#Tests.run_test(expected_value(input[0], input[1], input[2]), expected, 'Testing expected_value()')
#
#input = ((2,), 2, 1)
#expected = 3.0
#Tests.run_test(expected_value(input[0], input[1], input[2]), expected, 'Testing expected_value()')
#
#input = ((2,2), 6, 2)
#expected = 5.8333333333333
#Tests.run_test(expected_value(input[0], input[1], input[2]), expected, 'Testing expected_value()')
#
#Tests.report_results()

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    possible_holds = [()]
    for die in hand:
        for subset in possible_holds:
            possible_holds = possible_holds + [tuple(subset) + (die,)]
    return set(possible_holds)

# testing gen_all_holds()
#Tests = tsuite.TestSuite()
#
#input = (1,3)
#expected = set([(), (1,), (3,), (1, 3)])
#Tests.run_test(gen_all_holds(input), expected, 'Testing score()')
#
#input = (1,)
#expected = set([(), (1,)])
#Tests.run_test(gen_all_holds(input), expected, 'Testing score()')
#
#Tests.report_results()

def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    result = (0.0, ())
    current_score = 0.0
    
    for choice in gen_all_holds(hand):
        expected_score = expected_value(choice, num_die_sides, len(hand) - len(choice))
        if expected_score > current_score:
            current_score = expected_score
            result = (current_score, choice)
  
    return result

# testing strategy()
#Tests = tsuite.TestSuite()
#
#input = [(1, 1, 1, 5, 6), 6]
#expected = (21.5, (5,6))
#Tests.run_test(strategy(input[0], input[1]), expected, 'Testing strategy()')
#
#Tests.report_results()

def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
#run_example()

#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
    
    
    



