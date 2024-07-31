from Car import Car

class Tata:
    def __init__(self, model, tyres, gears, clutch, straring_design, sterio, speakers, logo, insurance, warrenty):
        Car.__init__(self, tyres, gears, clutch, straring_design, sterio, speakers)
        self.company_logo = logo
        self.insurance_amount = insurance
        self.warrenty_duration = warrenty
        self.car_model = model

    def get_logo(self):
        return self.company_logo

    def get_insurance(self):
        return self.insurance_amount

    def get_warrenty(self):
        return self.warrenty_duration

    def get_model(self):
        return self.car_model


brand = Tata('Tiago', 5, 6, 1, 'diamond', 'Harmon sterio', 4, 'Tata', '27500', 5)
brand1 = Tata('Nexon', 5, 7, 1, 'round', 'Harmon sterio', 5, 'Tata', '57000', 5)