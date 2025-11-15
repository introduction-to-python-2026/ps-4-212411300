def split_before_each_uppercases(formula):
     start = 1 
     end = 1 
     split_formula =[]
     for i, char in enumerate(formula):
      if char.isupper() and i != 0:
       split_formula.append(formula[start:end])
     return split_formula


def split_at_first_digit(formula):
    def split_at_first_digit(formula):
     digit_location = 1
     for char in formula: 
          if char.isdigit ():
              break
          digit_location += 1
          if digit_location == len (formula):
              return formula, 1
