from django.db import models

class GiftCard(models.Model):
    card_number = models.CharField(max_length=50, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def add_balance(self, amount):
        if self.is_active:
            self.balance += amount
            return True
        else:
            return False  # Card is not active

    def deduct_balance(self, amount):
        if self.is_active and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False  # Insufficient balance or card is not active
