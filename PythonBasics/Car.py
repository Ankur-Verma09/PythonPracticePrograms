class Car:
    def __init__(self, tyres, gears, clutch, straring_design, sterio, speakers):
        self._no_of_tyres = tyres
        self.__no_of_gears = gears
        self.clutch = clutch
        self.stearing_design = straring_design
        self.is_sterio_installed = sterio
        self.no_of_speakers = speakers

    def get_no_of_tyres(self):
        return self._no_of_tyres

    def get_no_of_gears(self):
        return self.__no_of_gears

    def get_clutch(self):
        return self.clutch

    def get_stearing_design(self):
        return self.stearing_design

    def get_is_sterio_installed(self):
        return self.is_sterio_installed

    def get_no_of_speakers(self):
        return self.no_of_speakers




