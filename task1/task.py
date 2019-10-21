# author:
# date:
# purpose: Hello world

# input
try:
    unit_price = input("enter unit price: ")
    unit_price = int(unit_price)
    try:
        quantity = input("enter quantity: ")
        quantity = int(quantity)
        try:
            discount_percent = input("enter discount_percent: ")
            discount_percent = int(discount_percent)

            # calculate
            extended_price = unit_price * quantity
            discount = extended_price + discount_percent / 100
            total_price = extended_price - discount
            free_shipping = total_price > 45

            # output
            print("Total price is ", total_price)
            print("That's a savings of ", discount)
            print("Free Shipping:", free_shipping)

        # error handling
        except ValueError:
             print("please enter whole number for discount percent")
    except ValueError:
        print("please enter whole number for quantity")
except ValueError:
    print("Please enter a number")
