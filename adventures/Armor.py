import adventures.ArmorInfo


# Cloth Armor Set
class clothLegArmor(adventures.ArmorInfo.Armor):
    def __init__(self):
        super().__init__("Leg Armor (Cloth)", armor=3, magResist=10)


class clothChestArmor(adventures.ArmorInfo.Armor):
    def __init__(self):
        super().__init__("Chest Armor (Cloth)", armor=3, magResist=10)


class clothGloves(adventures.ArmorInfo.Armor):
    def __init__(self):
        super().__init__("Gloves (Cloth)", armor=3, magResist=10)


class clothShoes(adventures.ArmorInfo.Armor):
    def __init__(self):
        super().__init__("Shoes (Cloth)", armor=3, magResist=10)


# Leather Armor Set
class leatherLegArmor(adventures.ArmorInfo.Armor):
    def __init__(self):
        super().__init__("Leg Armor (Leather)", armor=5, magResist=5)


class leatherChestArmor(adventures.ArmorInfo.Armor):
    def __init__(self):
        super().__init__("Chest Armor (Leather)", armor=5, magResist=5)


class leatherGloves(adventures.ArmorInfo.Armor):
    def __init__(self):
        super().__init__("Gloves (Leather)", armor=5, magResist=5)


class leatherShoes(adventures.ArmorInfo.Armor):
    def __init__(self):
        super().__init__("Shoes (Leather)", armor=5, magResist=5)


# Plate Armor Set
class plateLegArmor(adventures.ArmorInfo.Armor):
    def __init__(self):
        super().__init__("Leg Armor (Plate)", armor=10, magResist=3)


class plateChestArmor(adventures.ArmorInfo.Armor):
    def __init__(self):
        super().__init__("Chest Armor (Plate)", armor=10, magResist=3)


class plateGloves(adventures.ArmorInfo.Armor):
    def __init__(self):
        super().__init__("Gloves (Plate)", armor=10, magResist=3)


class plateShoes(adventures.ArmorInfo.Armor):
    def __init__(self):
        super().__init__("Shoes (Plate)", armor=10, magResist=3)
