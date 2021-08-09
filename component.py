class Component:
    def __init__(self):
        self.input = []
        self.output = []
    
    def clear_input(self, input_data):
        #make list
        if type(input_data) != list:
            input_data = [input_data]
        #delete non boolean
        input_data = [x for x in input_data if isinstance(x, bool)]

        #add missing as false or remove last if to many list entrys
        if(len(input_data)>self.INPUT_LENGTH):
            input_data = input_data[:len(input_data)-(len(input_data)-self.INPUT_LENGTH)]
            print("del length")
        elif(len(input_data)<self.INPUT_LENGTH):
            for i in range(len(input_data), self.INPUT_LENGTH):
                input_data.append(False)
        self.input = input_data