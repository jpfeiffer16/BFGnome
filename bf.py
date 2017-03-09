class bf():

  def __init__(self, code, programInput):
    self.__code = ""
    self.__input = ""
    self.__code_pointer = 0
    self.__input_pointer = 0
    self.__stack_pointer = 0
    self.output = ""
    self.done = False
    self.stack = [0 for i in range(300)]
    # for i in range(0, 299):
    #   self.stack[i] = 0
    self.__code = code
    self.__input = programInput
  
  def __interpret(self, char):
    #TODO: Do stuff with the char here
    if (char == "<"):
      self.__stack_pointer -= 1
      self.__code_pointer += 1
    if (char == ">"):
      self.__stack_pointer += 1
      self.__code_pointer += 1
    if (char == ","):
      if (self.__input_pointer >= len(self.__input)):
        self.stack[self.__stack_pointer] = 0
      else:
        self.stack[self.__stack_pointer] = ord(self.__input[self.__input_pointer])
      self.__code_pointer += 1
      self.__input_pointer += 1
    if (char == "."):
      self.output = self.output + chr(self.stack[self.__stack_pointer])
      self.__code_pointer += 1
    if (char == "+"):
      self.stack[self.__stack_pointer] += 1
      self.__code_pointer += 1
    if (char == "-"):
      self.stack[self.__stack_pointer] -= 1
      self.__code_pointer += 1
    if (char == "["):
      self.__code_pointer += 1
    if (char == "]"):
      if (self.stack[self.__stack_pointer] == 0):
        self.__code_pointer += 1
      else:
        while self.__code[self.__code_pointer] != "[":
          self.__code_pointer -= 1

    if (self.__code_pointer > len(self.__code) - 1):
      self.done = True

  def step(self):
    self.__interpret(self.__code[self.__code_pointer])
  
  def run(self):
    while not(self.done):
      self.step()
    return self.output