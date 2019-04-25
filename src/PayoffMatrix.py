class PayoffMatrix:
    def __init__(self):
        self.matrix = dict()
        self.options = list()

    # Calcuates
    def getEquilibrium(self):
        p1_list = set()
        p2_list = set()

        def better_option

        # Go over each pair of options
        for p1_choice in self.options:
            for p2_choice in self.options:
                # Get the outcome given the current choices
                outcome = self.getOutcome(p1_choice, p2_choice)


                # Check if score improves by changing choice when knowing

        return


    def getOutcome(self, p1_choice, p2_choice):
        return self.matrix[(p1_choice, p2_choice)]

    def __str__(self):
        pass


    def readMatrix(self):
        pass