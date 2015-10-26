# Books cost $20 each.  For every 10 ordered the 11th is free.
# Delivery is $10 for the first book and $2 for each additional book.
# What is the total cost cost for 80 books?

bookCost = 20
numBooks = 80

bookCost = (numBooks*bookCost) - int(numBooks/11)*bookCost
deliveryCost = 10 + 2*(numBooks-1)

totalCost = bookCost + deliveryCost

print("$" + str(totalCost))