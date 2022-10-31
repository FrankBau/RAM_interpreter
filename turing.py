# https://python-course.eu/applications-python/turing-machine.php
 
class Tape(object):
    
    blank_symbol = "_"
    
    def __init__(self, tape_string = ""):
        self.__tape = dict((enumerate(tape_string)))
        
    def __str__(self):
        min_used_index = min(self.__tape.keys()) 
        max_used_index = max(self.__tape.keys())
        s = ""
        for i in range(min_used_index, max_used_index+1):
            s += self.__tape[i]
        return s.strip(Tape.blank_symbol)
   
    def __getitem__(self,index):
        if index in self.__tape:
            return self.__tape[index]
        else:
            return Tape.blank_symbol

    def __setitem__(self, pos, char):
        self.__tape[pos] = char 

        
class TuringMachine(object):
    
    def __init__(self, 
                 tape = "", 
                 blank_symbol = " ",
                 initial_state = "",
                 final_states = None,
                 transition_function = None):
        self.__tape = Tape(tape)
        self.__head_position = 0
        self.__current_state = initial_state
        if transition_function == None:
            self.__transition_function = {}
        else:
            self.__transition_function = transition_function
        if final_states == None:
            self.__final_states = set()
        else:
            self.__final_states = set(final_states)
        
    def get_tape(self): 
        return str(self.__tape)
    
    def step(self):
        char_under_head = self.__tape[self.__head_position]
        x = (self.__current_state, char_under_head)
        if x in self.__transition_function:
            y = self.__transition_function[x]
            self.__tape[self.__head_position] = y[1]
            if y[2] == "R":
                self.__head_position += 1
            elif y[2] == "L":
                self.__head_position -= 1
            elif y[2] == "N":
                pass
            self.__current_state = y[0]

    def final(self):
        if self.__current_state in self.__final_states:
            return True
        else:
            return False


if __name__ == "__main__":

    transition_function = {
        ("init","0"):("init", "1", "R"),
        ("init","1"):("init", "0", "R"),
        ("init","_"):("halt", "_", "N"),
    }

    t = TuringMachine(
        "011", 
        initial_state = "init",
        final_states = {"halt"},
        transition_function=transition_function
    )

    print("Input on Tape:\n" + t.get_tape())

    while not t.final():
        t.step()

    print("Result of the Turing machine calculation:")    
    print(t.get_tape())
