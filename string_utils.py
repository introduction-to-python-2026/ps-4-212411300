def split_before_each_uppercases(formula):
     start = 0
     end = 1
     split_formula = []

     if not formula:
       return formula
         
     while end < len(formula):
      if formula[end].isupper():
         split_formula.append(formula[start:end])
         start=end
      end +=1
      split_formula.append(formula[start:])
      
     return split_formula



def split_at_first_digit(formula):
    for i, char in enumerate(formula):
        if char.isdigit():
            return formula[:i], formula[i:]
    return formula, "1"  



