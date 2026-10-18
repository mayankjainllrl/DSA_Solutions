

class Invoice:
    
    platform_fee_percent = 10
    invoice_count = 0
    usd_exchange_rate = 95.3
    
    def __init__(self, client_name, hours_worked, hourly_rate):
        self.client_name = client_name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.gross_amount = self.hourly_rate * self.hours_worked
        Invoice.invoice_count += 1
        
    def calc_net_amount(self):
        net_fee = self.gross_amount * self.platform_fee_percent/100
        return self.gross_amount - net_fee
    
    @classmethod
    def from_string(cls, formatted_string):
        client_name, hours_worked, hourly_rate = formatted_string.split("-")
        return cls(client_name, int(hours_worked), int(hourly_rate))
    
    @staticmethod
    def usd_to_inr_converter(usd_amount):
        return usd_amount * Invoice.usd_exchange_rate
    
class RecurringInvoice(Invoice):
    def __init__(self, client_name, hours_worked, hourly_rate, months):
        super().__init__(client_name, hours_worked, hourly_rate)
        self.months = months
        
    def calc_net_amount(self):
        return super().calc_net_amount() * self.months
    
    
    
inv1 = Invoice("Jagdish", 4, 25)
inv3 = Invoice("Hari", 5, 21)
inv2 = Invoice.from_string("AcmeCorp-12-25")
print(Invoice.invoice_count)
rec_inv = RecurringInvoice("Mona", 10, 20, 6)
print(Invoice.invoice_count)
print(rec_inv.calc_net_amount())

print(inv1.calc_net_amount())
print(inv2.calc_net_amount())
Invoice.platform_fee_percent = 8
print(inv1.calc_net_amount())
print(Invoice.usd_to_inr_converter(inv1.calc_net_amount()))
Invoice.usd_exchange_rate = 100
print(Invoice.usd_to_inr_converter(inv1.calc_net_amount()))
