def split_before_each_uppercases(formula):
     start = 0
     end = 1
     split_formula = []

     if not formula:
        return split_formula
         
     while end < len(formula):
       if formula[end].isupper():
         split_formula.append(formula[start:end])
         start=end
       end +=1
     split_formula.append(formula[start:])
      
     return split_formula

def split_at_first_digit(formula):
    digit_index = -1
    for i, char in enumerate(formula):
        if char.isdigit():
            digit_index = i
            break
    if digit_index == -1:  
        return formula, 1
    else:
        prefix = formula[:digit_index]
        numeric_part = int(formula[digit_index:])
        return prefix, numeric_part



