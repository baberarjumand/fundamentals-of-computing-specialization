"""
Simulator for greedy boss scenario
http://www.codeskulptor.org/#user47_icpSMzu4ls_1.py
"""

import simpleplot
import math
import codeskulptor
codeskulptor.set_timeout(20)

STANDARD = True
LOGLOG = False

# constants for simulation
INITIAL_SALARY = 100
SALARY_INCREMENT = 100
INITIAL_BRIBE_COST = 1000

def func1(val):
    # y = (9.5 * d) ^ 4
    return 9.5 * (val ** 4)

def func2(val):
    # y = 95 * (d **2)
    return 95.0 * (val ** 2)

def func3(val):
    # y = exp(9.5 * d)
    return math.exp(9.5 * val)

def func4(val):
    # y = exp(0.095 * d)
    return math.exp(0.095 * val)

def build_plot(plot_size, plot_function, plot_type = STANDARD):
    """
    Build plot of the number of increments in mystery function
    """    
    plot = []
    for input_val in range(2, plot_size):        
        if plot_type == STANDARD:
            plot.append([input_val, plot_function(input_val)])
        else:
            plot.append([math.log(input_val), math.log(plot_function(input_val))])
    return plot

def greedy_boss(days_in_simulation, bribe_cost_increment, plot_type = STANDARD):
    """
    Simulation of greedy boss
    """
    
    # initialize necessary local variables
    current_salary = INITIAL_SALARY
    current_earnings = 0
    current_day = 0
    current_bribe_cost = INITIAL_BRIBE_COST
    current_savings = 0
    current_salary_increment = SALARY_INCREMENT
    
    # define  list consisting of days vs. total salary earned for analysis
    days_vs_earnings = []

    # Each iteration of this while loop simulates one bribe
    while current_day <= days_in_simulation:
        
        # update list with days vs total salary earned
        # use plot_type to control whether regular or log/log plot
        if plot_type == STANDARD:
            days_vs_earnings.append((current_day, current_earnings))
        elif plot_type == LOGLOG:
            days_vs_earnings.append((math.log(current_day), math.log(current_earnings)))
        
        # check whether we have enough money to bribe without waiting        
        if current_savings >= current_bribe_cost:
            current_savings -= current_bribe_cost
            current_salary += current_salary_increment
            current_bribe_cost += bribe_cost_increment
        
        # advance current_day to day of next bribe (DO NOT INCREMENT BY ONE DAY)
        while current_savings < current_bribe_cost:
            current_earnings += current_salary
            current_savings += current_salary
            current_day += 1

        # update state of simulation to reflect bribe
   
    return days_vs_earnings


def run_simulations():
    """
    Run simulations for several possible bribe increments
    """
    plot_type = STANDARD
#    plot_type = LOGLOG
    days = 50
    inc_0 = greedy_boss(days, 0, plot_type)
    inc_500 = greedy_boss(days, 500, plot_type)
    inc_1000 = greedy_boss(days, 1000, plot_type)
    inc_2000 = greedy_boss(days, 2000, plot_type)
    plot1 = build_plot(days, func1, plot_type)
    plot2 = build_plot(days, func2, plot_type)
    plot3 = build_plot(days, func3, plot_type)
    plot4 = build_plot(days, func4, plot_type)
#    simpleplot.plot_lines("Greedy boss", 600, 600, "days", "total earnings", 
#                          [inc_0, inc_500, inc_1000, inc_2000], False,
#                         ["Bribe increment = 0", "Bribe increment = 500",
#                          "Bribe increment = 1000", "Bribe increment = 2000"])
#    simpleplot.plot_lines("Greedy boss", 600, 600, "days", "total earnings", 
#                          [inc_0], False,
#                         ["Bribe increment = 0"])
    simpleplot.plot_lines("Greedy boss", 600, 600, "days", "total earnings", 
                          [inc_0, 
#                           plot1, 
#                           plot2, 
#                           plot3, 
                           plot4], False,
                         ["Bribe increment = 0", 
#                          "y = 9.5(d^4)", 
#                          "y = 95(d^2)", 
#                          "y=exp(9.5d)", 
                          "y=exp(0.095d)"])

run_simulations()

#print greedy_boss(35, 100)
# should print [(0, 0), (10, 1000), (16, 2200), (20, 3400), (23, 4600), (26, 6100), (29, 7900), (31, 9300), (33, 10900), (35, 12700)]

#print greedy_boss(35, 0)
# should print [(0, 0), (10, 1000), (15, 2000), (19, 3200), (21, 4000), (23, 5000), (25, 6200), (27, 7600), (28, 8400), (29, 9300), (30, 10300), (31, 11400), (32, 12600), (33, 13900), (34, 15300), (34, 15300), (35, 16900)]

#for data in greedy_boss(50, 1000, LOGLOG):
#    print data

            
            
    