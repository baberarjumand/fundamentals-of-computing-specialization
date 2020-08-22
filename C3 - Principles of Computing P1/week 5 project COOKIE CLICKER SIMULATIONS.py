"""
Cookie Clicker Simulator
# http://www.codeskulptor.org/#user47_WprWrq3FBA_5.py
"""

import simpleplot
import math

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(30)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0
#SIM_TIME = 30.0
INITIAL_CPS = 1.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._total_cookies = 0.0
        self._current_cookies = 0.0
        self._current_time = 0.0
        self._current_cps = INITIAL_CPS
        self._history = [(self._current_time,
                          None,
                          0.0,
                          self._total_cookies)]
        
    def __str__(self):
        """
        Return human readable state
        """
        return_str = ''
#        for item in self._history:
#            return_str += str(item)
#            return_str += '\n'        
#        # append end state to list for testing purposes
#        return_str += 'End State: '
#        return_str += str((self._current_time, None, None, self._total_cookies))
#        return_str += '\n'
        
#    	return_str = '\nState -\n'
#        return_str += 'Time           : ' + str(self._current_time) + '\n'
#        return_str += 'Current Cookies: ' + str(self._current_cookies) + '\n'
#        return_str += 'Current CPS    : ' + str(self._current_cps) + '\n'
#        return_str += 'Total Cookies  : ' + str(self._total_cookies) + '\n'
        
        return_str += 'Time: ' + str(self._current_time)
        return_str += ' Cookies: ' + str(self._current_cookies)
        return_str += ' Cps: ' + str(self._current_cps)
        return_str += ' Total: ' + str(self._total_cookies)
        
        return return_str
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._current_cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return self._history

    def time_until(self, target_cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        wait_time = (target_cookies - self._current_cookies) / self._current_cps
        wait_time = float(math.ceil(wait_time))
        if wait_time > 0.0:
            return wait_time
        return 0.0
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
#        if time > 0.0:
#            for dummy_idx in range(int(time)):
#                self._current_time += 1.0
#                self._total_cookies += self._current_cps
#                self._current_cookies += self._current_cps
        if time > 0.0:            
                self._current_time += time
                self._total_cookies += (time * self._current_cps)
                self._current_cookies += (time * self._current_cps)
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if self._current_cookies >= cost:
            self._current_cookies -= cost
            self._current_cps += additional_cps
            self._history.append((self._current_time,
                                  item_name,
                                  cost,
                                  self._total_cookies))
   
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """

    # Replace with your code
    game_obj = ClickerState()
    clone = build_info.clone()
    
    while game_obj.get_time() < duration:
        next_upgrade = strategy(game_obj.get_cookies(),
                               game_obj.get_cps(),
                               game_obj.get_history(),
                               duration - game_obj.get_time(),
                               clone)
        if next_upgrade == None:
            game_obj.wait(duration - game_obj.get_time())
        else:
            upgrade_cost = clone.get_cost(next_upgrade)
            if game_obj.get_time() + game_obj.time_until(upgrade_cost) <= duration:
                game_obj.wait(game_obj.time_until(upgrade_cost))
                game_obj.buy_item(next_upgrade,
                              upgrade_cost,
                              clone.get_cps(next_upgrade))
                clone.update_item(next_upgrade)
            else:
                game_obj.wait(duration - game_obj.get_time())
    while game_obj.get_time() == duration:
        next_upgrade = strategy(game_obj.get_cookies(),
                               game_obj.get_cps(),
                               game_obj.get_history(),
                               0.0,
                               clone)
        if next_upgrade == None:
            break
        else:
            if clone.get_cost(next_upgrade) <= game_obj.get_cookies():
                game_obj.buy_item(next_upgrade,
                              clone.get_cost(next_upgrade),
                              clone.get_cps(next_upgrade))
                clone.update_item(next_upgrade)
            else:
                break

    return game_obj


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    price_list = {}
    for item in build_info.build_items():
        price_list[build_info.get_cost(item)] = item
    if build_info.get_cost(price_list[min(price_list)]) <= cookies + cps * time_left:
        return price_list[min(price_list)]
    else:
        return None

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    price_list = {}
    fund = cookies + cps * time_left
    for item in build_info.build_items():
        if build_info.get_cost(item) <= fund:
            price_list[build_info.get_cost(item)] = item
    if len(price_list) > 0:
        return price_list[max(price_list)]
    else:
        return None

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    price_list = {}
    cps_list = {}
    for item in build_info.build_items():
        price_list[build_info.get_cost(item)] = item
        cps_list[build_info.get_cps(item) / build_info.get_cost(item)] = item
    if build_info.get_cost(price_list[min(price_list)]) <= cookies + cps * time_left:
        # at the starting 1.5% and ending 30% of simulation, purchase cheapest upgrade
        # at other times, purchase most expensive
        if time_left > SIM_TIME * 0.985 or time_left < SIM_TIME * 0.30:
            return price_list[min(price_list)]
        else:
            return cps_list[max(cps_list)]
    else:
        return None
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    run_strategy("Cheap", SIM_TIME, strategy_cheap)
    run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)
    
run()
    

