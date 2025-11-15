def split_before_each_uppercases(formula):
     start = 0
     end = 1
     split_formula = []

     if len(formula) == 0:
       return formula
         
     while end < len(formula):
      if formula [end].isupper():
        split_formula.append(formula[start:end])
        start=end
      end +=1
      split_formula.append(formula[start:])
      
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
