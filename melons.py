"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """calculate cost and shipping status for domestic and international melon orders."""

    def __init__(self, species, qty, tax = None, country_code = None):
        """ """
        self.species = species
        self.qty = qty
        self.shipped = False
        if tax:
            self.tax = tax
        if country_code:
            self.country_code = country_code

    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total   

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order, where tax is 0.08."""

    tax = 0.08
    order_type = "domestic"
    country_code = "USA"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order, where tax is 0.17."""

    tax = 0.17    
    order_type = "international"
    # country_code = None

    def get_country_code(self, country_code):
        """Return the country code."""

        self.country_code = country_code

        return self.country_code
