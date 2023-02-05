class Table:
    def __init__(self, table_form, seats, orders: list):
        self.__table_form = table_form
        self.__seats = seats
        self.__orders = orders

    def get_table_form(self):
        return self.__table_form

    def get_seats(self):
        return self.__seats

    def get_orders(self):
        return self.__orders

    def set_table_form(self, new_form):
        self.__table_form = new_form

    def set_seats(self, new_seats):
        self.__seats = new_seats

    def add_order(self, order):
        self.__orders.append(order)

    def edit_order(self, order):
        if order in self.__orders:
            pass

    def remove_order(self, order):
        if order in self.__orders:
            self.__orders.remove(order)

    @property
    def opened_order(self):
        if len(self.__orders > 0):
            return self.__orders[-1]

