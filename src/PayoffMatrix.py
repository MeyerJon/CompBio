class PayoffMatrix:
    def __init__(self, options, matrix):
        self.options = options
        self.matrix = matrix

    # Calcuates
    def getNashEquilibrium(self):
        equilibria = list()

        def best_option(choice1, choice2, vertical):
            # check if given choice is best in the
            outcome = self.getOutcome(p1_choice, p2_choice)

            options = self.options[:]

            if vertical:
                options.remove(choice1)
            else:
                options.remove(choice2)

            for option in options:
                if vertical:
                    if not (outcome[0] > self.getOutcome(option, choice2)[0]):
                        return False
                else:
                    if not (outcome[1] > self.getOutcome(choice1, option)[1]):
                        return False

            return True

        # Go over each pair of options
        for p1_choice in self.options:
            for p2_choice in self.options:

                # Check if current options are best for player 1 and player 2 respectively
                if best_option(p1_choice, p2_choice, True) and best_option(p1_choice, p2_choice, False):
                    equilibria.append((p1_choice, p2_choice))

        return equilibria

    def getESS(self):
        stable_strategy = list()

        def best_option(choice1, choice2):
            # check if given choice is best in the
            outcome = self.getOutcome(p1_choice, p2_choice)

            options = self.options[:]

            options.remove(choice1)

            for option in options:
                if not (outcome[0] > self.getOutcome(option, choice2)[0]) or (
                        (outcome[0] == self.getOutcome(option, choice2)[0]) and (
                        self.getOutcome(choice2, option)[0] > self.getOutcome(option, option)[0])):
                    return False

            return True

        # Go over each pair of options
        for p1_choice, p2_choice in self.getNashEquilibrium():
            # Check if current options are best for player 1 and player 2 respectively
            if best_option(p1_choice, p2_choice):
                stable_strategy.append(p1_choice)

        return stable_strategy

    def getOutcome(self, p1_choice, p2_choice):
        return self.matrix[(p1_choice, p2_choice)]

    def __str__(self):
        pass

    def readMatrix(self):
        pass


def testEquilibrium():
    def test_RPS():
        matrix = dict()
        options = ['R', 'P', 'S']

        matrix[('R', 'R')] = (0, 0)
        matrix[('R', 'P')] = (-1, 1)
        matrix[('R', 'S')] = (1, -1)
        matrix[('P', 'R')] = (1, -1)
        matrix[('P', 'P')] = (0, 0)
        matrix[('P', 'S')] = (-1, 1)
        matrix[('S', 'R')] = (-1, 1)
        matrix[('S', 'P')] = (1, -1)
        matrix[('S', 'S')] = (0, 0)

        pm = PayoffMatrix(options, matrix)

        print('Test RPS: Equilibrium = ', pm.getNashEquilibrium())
        print('Expected: \t\t\t\t', [])

    def test_Hunt():
        matrix = dict()
        options = ['Hunt stag', 'Hunt rabbit']

        matrix[('Hunt stag', 'Hunt stag')] = (2, 2)
        matrix[('Hunt stag', 'Hunt rabbit')] = (0, 1)
        matrix[('Hunt rabbit', 'Hunt stag')] = (1, 0)
        matrix[('Hunt rabbit', 'Hunt rabbit')] = (1, 1)

        pm = PayoffMatrix(options, matrix)

        print('Test Hunt: Equilibrium =', pm.getNashEquilibrium())
        print('Expected: \t\t\t\t', [('Hunt stag', 'Hunt stag'), ('Hunt rabbit', 'Hunt rabbit')])

    def test_ESS():
        matrix = dict()
        options = ['A', 'B']

        matrix[('A', 'A')] = (2, 2)
        matrix[('A', 'B')] = (1, 2)
        matrix[('B', 'A')] = (2, 1)
        matrix[('B', 'B')] = (2, 2)

        pm = PayoffMatrix(options, matrix)

        print('Test ESS: Equilibrium = ', pm.getESS())
        print('Expected: \t\t\t\t', ['B'])

    test_RPS()
    test_Hunt()
    test_ESS()


if __name__ == '__main__':
    testEquilibrium()
