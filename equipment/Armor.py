from equipment.ArmorInfo import Armor


# Cloth Armor Set
class clothLegArmor(Armor):
    def __init__(self):
        super().__init__("Leg Armor (Cloth)", armor=3, magResist=10)


class clothChestArmor(Armor):
    def __init__(self):
        super().__init__("Chest Armor (Cloth)", armor=3, magResist=10)


class clothGloves(Armor):
    def __init__(self):
        super().__init__("Gloves (Cloth)", armor=3, magResist=10)


class clothShoes(Armor):
    def __init__(self):
        super().__init__("Shoes (Cloth)", armor=3, magResist=10)


# Leather Armor Set
class leatherLegArmor(Armor):
    def __init__(self):
        super().__init__("Leg Armor (Leather)", armor=5, magResist=5)


class leatherChestArmor(Armor):
    def __init__(self):
        super().__init__("Chest Armor (Leather)", armor=5, magResist=5)


class leatherGloves(Armor):
    def __init__(self):
        super().__init__("Gloves (Leather)", armor=5, magResist=5)


class leatherShoes(Armor):
    def __init__(self):
        super().__init__("Shoes (Leather)", armor=5, magResist=5)


# Chainmail armor
class chainmailLegArmor(Armor):
    def __init__(self):
        super().__init__("Leg Armor (Chainmail)", armor=7, magResist=7)

class chainmailChestArmor(Armor):
    def __init__(self):
        super().__init__("Chest Armor (Chainmail)", armor=7, magResist=7)

class chainmailGloves(Armor):
    def __init__(self):
        super().__init__("Gloves (Chainmail)", armor=7, magResist=7)

class chainmailShoes(Armor):
    def __init__(self):
        super().__init__("Shoes (Chainmail)", armor=7, magResist=7)


# Plate Armor Set
class plateLegArmor(Armor):
    def __init__(self):
        super().__init__("Leg Armor (Plate)", armor=10, magResist=3)


class plateChestArmor(Armor):
    def __init__(self):
        super().__init__("Chest Armor (Plate)", armor=10, magResist=3)


class plateGloves(Armor):
    def __init__(self):
        super().__init__("Gloves (Plate)", armor=10, magResist=3)


class plateShoes(Armor):
    def __init__(self):
        super().__init__("Shoes (Plate)", armor=10, magResist=3)
