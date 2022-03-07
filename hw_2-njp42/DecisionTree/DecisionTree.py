class Node:
    """ base (master) class for nodes """
    def __init__(self, name, cost, utility):
        """
        :param name: name of this node
        :param cost: cost of visiting this node
        """

        self.name = name
        self.cost = cost
        self.utility = utility

    def get_expected_cost(self):
        """ abstract method to be overridden in derived classes
        :returns expected cost of this node """

    def get_expected_utility(self):
        """ abstract method to be overridden in derived classes
        :returns expected utility of this node """


class ChanceNode(Node):

    def __init__(self, name, cost, future_nodes, probs, utility):
        """
        :param name: name of this node
        :param cost: cost of visiting this node
        :param future_nodes: (list) future nodes connected to this node
        :param probs: (list) probability of future nodes
        :param utility: utility of future nodes
        """

        Node.__init__(self, name, cost, utility)
        self.futureNodes = future_nodes
        self.probs = probs

    def get_expected_cost(self):
        """
        :return: expected cost of this chance node
        E[cost] = (cost of visiting this node)
                  + sum_{i}(probability of future node i)*(E[cost of future node i])
        """

        # expected cost initialized with the cost of visiting the current node
        exp_cost = self.cost

        # go over all future nodes
        i = 0
        for node in self.futureNodes:
            # increment expected cost by
            # (probability of visiting this future node) * (expected cost of this future node)
            exp_cost += self.probs[i]*node.get_expected_cost()
            i += 1

        return exp_cost

    def get_expected_utility(self):
        # expected utility initialized with the utility of visiting the current node
        exp_utility = self.utility

        # go over all future nodes
        i = 0
        for node in self.futureNodes:
            # increment expected utility by
            # (probability of visiting this future node) * (expected utility of this future node)
            exp_utility += self.probs[i] * node.get_expected_utility()
            i += 1

        return exp_utility


class TerminalNode(Node):

    def __init__(self, name, cost, utility):
        """
        :param name: name of this node
        :param cost: cost of visiting this node
        :param utility: health utility of visiting this node
        """

        Node.__init__(self, name, cost, utility)

    def get_expected_cost(self):
        """
        :return: cost of this visiting this terminal node
        """
        return self.cost

    def get_expected_utility(self):
        """
        :return: utility of this visiting this terminal node
         """
        return self.utility


class DecisionNode(Node):

    def __init__(self, name, cost, probs, future_nodes, utility):
        """
        :param name: name of this node
        :param cost: cost of visiting this node
        :param future_nodes: (list) future nodes connected to this node
        (assumes that future nodes can only be chance or terminal nodes)
        """

        Node.__init__(self, name, cost, utility)
        self.futureNode = future_nodes
        self.probs = probs

    def get_expected_costs(self):
        """ returns the expected costs of future nodes
        :return: a dictionary of expected costs of future nodes with node names as dictionary keys
        """

        # a dictionary to store the expected cost of future nodes
        exp_costs = dict()
        # go over all future nodes
        for node in self.futureNode:
            # add the expected cost of this future node to the dictionary
            exp_costs[node.name] = self.cost + node.get_expected_cost()

        return exp_costs

    def get_expected_utility(self):
        # a dictionary to store the expected utility of future nodes
        exp_utility = dict()

        for node in self.futureNode:
            # add the expected cost of this future node to the dictionary
            exp_utility[node.name] = self.utility + node.get_expected_utility()

        return exp_utility



#######################
# See figure DT3.png (from the project menu) for the structure of this decision tree
########################

# create the terminal nodes
T1 = TerminalNode('T1', 10, 0.5)
T2 = TerminalNode('T2', 20, 0.6)
T3 = TerminalNode('T3', 30, 0.7)
T4 = TerminalNode('T4', 40, 0.8)
T5 = TerminalNode('T5', 50, 0.9)

# create C2
C2 = ChanceNode('C2', 35, [T1, T2], [0.7, 0.3], 0.0)
# create C1
C1 = ChanceNode('C1', 25, [C2, T3], [0.2, 0.8], 0.0)
# create C3
C3 = ChanceNode('C3', 45, [T4, T5], [0.1, 0.9], 0.0)


# create D1
D1 = DecisionNode('D1', 0, [C1, C3], [C1, C3], 0)

# print the expect cost of C1
print("Expected Costs: " + str(D1.get_expected_costs()))
print("Expected Utilities: " + str(D1.get_expected_utility()))

cost = D1.get_expected_costs()
utility = D1.get_expected_utility()
ICER = (cost['C3'] - cost['C1'])/(utility['C3'] - utility['C1'])
print("ICER = " + str(ICER))
