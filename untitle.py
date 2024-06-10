available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['olives', 'pepperoni']

#Customer list of toppings that they available in the restaurant.
customer_toppings = []

#check each topping whether it exist in available toppings.
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
        customer_toppings.append(requested_topping)
    else:
        print(f"Sorry, we don't have {requested_topping}.")

if len(customer_toppings) == 1:     #whether customer list have one topping print "is"
    print(f"\nSummary toppings you want is:\n- {customer_toppings}")    
elif len(customer_toppings) > 1:    #whether customer list have more than one topping print "are"
    print("Summary toppings you want are:")
    for customer_topping in customer_toppings:
        print(f"- {customer_topping}")
else:
    print("\nAre you sure you want a plain pizza?")
