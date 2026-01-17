letter = '''  
Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 
print(letter.replace("<|Name|>" , "Amit").replace("<|Date|>" , "31 December 2025"))