class Finite_Automata:
    def __init__(self, input_file):
        self.states = []
        self.alphabet = []
        self.initial = None
        self.final = None
        self.transition = {}

        with open(input_file, 'r') as file:
            for line in file:
                parts = line.split()
                if len(parts) > 1:
                    list_name = parts[0]
                    list_data = parts[1:]

                    if list_name == 'states':
                        self.states = list_data
                    elif list_name == 'alphabet':
                        self.alphabet = list_data
                    elif list_name == 'initial':
                        self.initial = list_data[0]
                    elif list_name == 'final':
                        self.final = list_data[0]
                    elif list_name != 'transition':
                        self.transition[(parts[0], parts[1])] = parts[2]

    def check_validity(self, input_string):
        state = self.initial

        for symbol in input_string:
            if self.transition.get((state, symbol)) is not None:
                state = self.transition[(state, symbol)]
            else:
                return False

        if state == self.final:
            return True
        else:
            return False

    def display_elements(self):
        print('States:', self.states)
        print('Alphabet:', self.alphabet)
        print('Initial:', self.initial)
        print('Final:', self.final)
        print('Transition:', self.transition)

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Display elements")
            print("2. Validate string")
            print("3. Quit")

            choice = input("Select an option: ")

            if choice == '1':
                self.display_elements()
            elif choice == '2':
                input_string = input("Input a string for validation: ")
                print(self.check_validity(input_string))
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please select a valid option (1/2/3).")

