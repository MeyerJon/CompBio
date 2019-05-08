class PayoffMatrix:
    def __init__(self, options1, options2, matrix):
        self.options1 = options1
        self.options2 = options2
        self.matrix = matrix

    # Calcuates
    def getNashEquilibrium(self):
        equilibria = list()

        def best_option(choice1, choice2, vertical):
            # check if given choice is best in the
            outcome = self.getOutcome(p1_choice, p2_choice)



            if vertical:
                options = self.options1[:]
                options.remove(choice1)
            else:
                options = self.options2[:]
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
        for p1_choice in self.options1:
            for p2_choice in self.options2:

                # Check if current options are best for player 1 and player 2 respectively
                if best_option(p1_choice, p2_choice, True) and best_option(p1_choice, p2_choice, False):
                    equilibria.append((p1_choice, p2_choice))

        return equilibria

    def getESS(self):
        stable_strategy = list()

        def best_option(choice1, choice2):
            # check if given choice is best in the
            outcome = self.getOutcome(p1_choice, p2_choice)

            options = self.options1[:]

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
        options1 = ['R1', 'P1', 'S1']
        options2 = ['R2', 'P2', 'S2']

        matrix[('R1', 'R2')] = (0, 0)
        matrix[('R1', 'P2')] = (-1, 1)
        matrix[('R1', 'S2')] = (1, -1)
        matrix[('P1', 'R2')] = (1, -1)
        matrix[('P1', 'P2')] = (0, 0)
        matrix[('P1', 'S2')] = (-1, 1)
        matrix[('S1', 'R2')] = (-1, 1)
        matrix[('S1', 'P2')] = (1, -1)
        matrix[('S1', 'S2')] = (0, 0)

        pm = PayoffMatrix(options1, options2, matrix)

        print('Test RPS: Equilibrium = ', pm.getNashEquilibrium())
        print('Expected: \t\t\t\t', [])

    def test_Hunt():
        matrix = dict()
        options1 = ['Hunt stag1', 'Hunt rabbit1']
        options2 = ['Hunt stag2', 'Hunt rabbit2']

        matrix[('Hunt stag1', 'Hunt stag2')] = (2, 2)
        matrix[('Hunt stag1', 'Hunt rabbit2')] = (0, 1)
        matrix[('Hunt rabbit1', 'Hunt stag2')] = (1, 0)
        matrix[('Hunt rabbit1', 'Hunt rabbit2')] = (1, 1)

        pm = PayoffMatrix(options1, options2, matrix)

        print('Test Hunt: Equilibrium =', pm.getNashEquilibrium())
        print('Expected: \t\t\t\t', [('Hunt stag1', 'Hunt stag2'), ('Hunt rabbit1', 'Hunt rabbit2')])

    def test_ESS():
        matrix = dict()
        options1 = ['A1', 'B1']
        options2 = ['A2', 'B2']

        matrix[('A1', 'A2')] = (2, 2)
        matrix[('A1', 'B2')] = (1, 2)
        matrix[('B1', 'A2')] = (2, 1)
        matrix[('B1', 'B2')] = (2, 2)

        pm = PayoffMatrix(options1, options2, matrix)

        print('Test ESS: Equilibrium = ', pm.getESS())
        print('Expected: \t\t\t\t', ['B1'])

    test_RPS()
    test_Hunt()
    test_ESS()


if __name__ == '__main__':
    testEquilibrium()
