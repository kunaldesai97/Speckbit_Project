class Product:
    """Class for Product"""
    def __init__(self, price, prod_id, quantity,all):
        self.price = price
        self.prod_id = prod_id
        self.quantity = quantity
        all[prod_id] = self #Store prod_id (key) and product object (value) in the dictionary

class Inventory:
    """ Class for Inventory """
    all = {}

    def remove_prod(self,prod_id):
        """To remove the product based on the product id"""
        if prod_id in self.all.keys():
            del self.all[prod_id]
            print('Product with ID %d is deleted' % prod_id)
        else:
            print('Product with ID %d is not found' % prod_id)

    def total(self):
        """To return the total value of all the products"""
        sum = 0
        for key in self.all.keys():
            sum += self.all[key].price
        return sum


inventory = Inventory() #Creation of inventory object

while(True):
    c  = int(input('1.Add product\n2.Delete Product\n3.Display Total\n4.Exit\nEnter option\n'))
    if c==1: #To add new product
        n = int(input('Enter no.of products\n'))
        for i in range(n):
            price = int(input('Enter Price of product %d\n' % (i+1)))
            prod_id = int(input('Enter Product_ID of product %d\n' % (i+1)))
            quantity = int(input('Enter Quantity of product %d\n' % (i+1)))
            if prod_id in inventory.all.keys():
                print('Product with ID %d already exists' % prod_id)
            else:
                Product(price,prod_id,quantity,inventory.all)
            print('\n')

    elif c==2: #To delete an existing product
        del_prod = int(input('Enter Prod_ID of product to be deleted\n'))
        inventory.remove_prod(del_prod)
        print('\n')

    elif c==3: #To display the total value of all products
        print('Total value of all the products:', inventory.total())
        print('\n')

    elif c==4: #To exit
        break;

    else:
        print('Invalid Choice')
