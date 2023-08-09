# For loop execudes a block of code repetedly until the condition in the for statement is no longer valid.

# Looping through an iterable: 
# for a in iterable:
#     print(a)

companies = ['Tesla', 'Apple', 'Google', 'Microsoft', 'Amazon']
for company in companies:
   print(company)
   
# index of items, enumerate(iterable)
for index, company in enumerate(companies):
    print(index, company)

# loop through a String    
for i in "Hi there":
    print(i)       
    
# range(start, end, step) -> [start, end)
for i in range(5):
    print(i)     
    