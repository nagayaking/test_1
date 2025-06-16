class Aparell:
    def __init__(self,id,name,price,purchase_price):
        self.id = id
        self.name = name
        self.price = price
        self.purchase_price = purchase_price

    def cost_rate(self):
        ct_rate = self.purchase_price / self.price * 100
        return(ct_rate)
    
aparell_1 = Aparell("A0001","半袖クールTシャツ",5000,2250)

aparell_1_cost_rate = aparell_1.cost_rate()
print(aparell_1_cost_rate)

aparell_1.price = 6000
aparell_1_cost_rate = aparell_1.cost_rate()
print(aparell_1_cost_rate)