from datetime import datetime

subtotal = 1
while subtotal != 0:
    subtotal = float(input('\nPlease enter the subtotal(enter 0 to exit): '))
    date = datetime.now()
    day = date.weekday()

#See if day is Tues or Wed

    if subtotal == 0:
        print('Thanks for shopping with us!')
    elif subtotal >= 50 and day in (1,2):
        discount = subtotal/100*10
        subtotal = subtotal - discount   
        tax =  subtotal/100*6
        print(f'Discount amount: {discount:.2f}')
        print(f'Sales tax amount: {tax:.2f} ')
        print(f'Total: {subtotal + tax:.2f} ')
    elif subtotal <50 and day in(1,2):
        amount_needed = 50-subtotal
        print(f'You need {amount_needed} more to receive the 10% discount!')
        discount = 0
        subtotal = subtotal - discount   
        tax =  subtotal/100*6
        print(f'Sales tax amount: {tax:.2f} ')
        print(f'Total: {subtotal + tax:.2f} ')
    else:
        discount = 0
        subtotal = subtotal - discount   
        tax =  subtotal/100*6
        print(f'Sales tax amount: {tax:.2f} ')
        print(f'Total: {subtotal + tax:.2f} ')  