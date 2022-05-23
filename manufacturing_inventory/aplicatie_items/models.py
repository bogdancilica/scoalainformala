from django.db import models

category_choices = (
("Fittings", "fittings"), ("Adaptors", "adaptors"), ("Ball Valves", "b_valves"), ("Check Valves", "c_valves"),
("Relief Valves", "r_valves"), ("Pressure Indicators", "p_indicators"), ("Temperature Indicators", "t_indicators"))
auto_po_choices = (("n/a", "n_a"), ("5", "5"), ("10", "10"), ("15", "15"), ("20", "20"))


class Items(models.Model):
    category = models.CharField(max_length=100, choices=category_choices)
    item_no = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    auto_po = models.BooleanField(default=1)
    auto_po_qty = models.CharField(max_length=100, choices=auto_po_choices)
    status = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.item_no}_{self.category}"
