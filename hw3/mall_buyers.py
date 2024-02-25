from BootcampPythonRepo.hw3.frac import Frac
import random
# Maverick Espinosa
# mespin11

# Task 2
# write a class called Node corresponding to each of the buildings.
class Node:
    """ class corresponding to each of the buildings"""
    def __init__(self,build_id,connected_nodes,minimum_price,fractional_price):
        
        """
        Parameters
        ----------
        build_id : id of store
        outgoing_edges : list of outgoing nodes
        minimum_price : Frac object defining minimum price threshold
        fractional_price : Frac object defining fraction of buyer remaining budget that buyer has to pay

        Returns
        -------
        None.
        """
        
        self.build_id = build_id
        self.connected_nodes = connected_nodes
        self.minimum_price = minimum_price
        self.fractional_price = fractional_price
        self.revenue = Frac(0,1)
        return

# Task 3
# write a Buyer class
class Buyer:
    """ class corresponding a buyer"""
    def __init__(self,current_node_id,remaining_budget):
        self.current_node_id = current_node_id
        self.remaining_budget = remaining_budget
        return

# Task 4
# write a function called
# run_simulation that takes as input (i) a filename for the connectivities, (ii)
# a filename for the building pricing schemes, and (iii) a filename for the Buyer
# budgets, in that order

def assignNode(outgoing_nodes):
    random_key = random.choice(list(outgoing_nodes.keys()))
    return random_key

def run_simulation (connectivities,pricing_schemes,buyer_budgets):
    

    # create graph (dictionary of nodes)
    
    graph = {}
    outgoing_nodes = {}
    
    # reading from connectiivites (from node, to node)

    outgoing_edges_file = open(connectivities, 'r', encoding='utf-8-sig')
    outgoing_edges_lines = outgoing_edges_file.readlines()

    for line in outgoing_edges_lines:
        
        from_node, to_node = line.strip().split()

        if from_node not in outgoing_nodes:
            outgoing_nodes[from_node] = []

        outgoing_nodes[from_node].append(to_node)
        
    # reading from pricing_schemes file (buildingid, numerator + denominator of building min price
     # , numerator + denominator of fractional price) and populating each node
    
    pricing_info_file = open(pricing_schemes, 'r', encoding='utf-8-sig')
    pricing_info_lines = pricing_info_file.readlines()

    for line in pricing_info_lines:
        building_id, min_numerator, min_denominator, fract_numerator, fract_denominator = line.strip().split()
        # print("Converted values:", building_id, min_numerator, min_denominator, fract_numerator, fract_denominator)
        # Create Node and add to graph
        graph[building_id] = Node(building_id, outgoing_nodes.get(building_id, []),
                                 Frac(int(min_numerator), int(min_denominator)),
                                 Frac(int(fract_numerator), int(fract_denominator)))  
        
    # create a list of Buyer objects with budgets as specified by the budget input file
        # reading from buyer_budgets (1st buyer budget, 2nd, ...) file
    
    buyers = []

    buyer_budgets_file = open(buyer_budgets, 'r', encoding='utf-8-sig')
    buyer_budgets_lines = buyer_budgets_file.readlines()
    
    for line in buyer_budgets_lines:
        buyer_budget = line.strip().split()
        
        for budget_value in buyer_budget:
            
            # buyers choose building to visit at random
            
            buyers.append(Buyer(assignNode(outgoing_nodes), Frac(int(budget_value), 1)))     

    # simulate movement and purchasing on the graph  
    
    total_revenue = Frac(0,1)
    
    # while there are still buyers in the list of buyer objects, run simulation for each buyer
    
    while buyers:
        for index,buyer in enumerate(buyers):
            
            if buyer.remaining_budget <= graph[buyer.current_node_id].minimum_price:
                buyers.pop(index)
                continue
            node_revenue = graph[buyer.current_node_id].fractional_price * buyer.remaining_budget
            
            # buyer makes purchase
            
            buyer.remaining_budget -= node_revenue
            
            # node/store makes revenue 
            
            graph[buyer.current_node_id].revenue += node_revenue
            
            # keep track of total revenue
            
            total_revenue += node_revenue
            
            # update current_node_id after each purchase
            buyer.current_node_id = assignNode(outgoing_nodes)

    # return total revenue of all buildings and dictionary with Node ids as keys
     # and fraction of total revenue that building earned as values

    building_fract_revenue = {}
    for build_id,node in graph.items():
        building_fract_revenue[build_id] = graph[build_id].revenue/total_revenue
        
    # create a tuple of total revenue and dictionary
    return total_revenue, building_fract_revenue
        
        

# # Run the simulation with sample files
# result = run_simulation("connectivities.txt", "pricing_schemes.txt", "buyer_budgets.txt")

# # Print the result
# print("Total Revenue:", result[0])
# print("Building Fractional Revenue:")
# for build_id, fraction in result[1].items():
#     print(f"Building {build_id}: {fraction}")


