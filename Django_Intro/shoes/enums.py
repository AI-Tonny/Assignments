from enum import Enum

class ShoeGender(Enum):
    MALE = 'men'
    FEMALE = 'woman'
    UNISEX = 'unisex'

class ShoeType(Enum):
    SNEAKERS = 'sneakers'
    BOOTS = 'boots'
    FLIP_FLOPS = 'flip-flops'
    SANDALS = 'sandals'
    HEELS = 'heels'
    SLIPPERS = 'slippers'
    SPORT_SHOES = 'sport shoes'
    CASUAL = 'casual'

class ShoeColor(Enum):
    WHITE = 'white'
    BLACK = 'black'
    RED = 'red'
    BLUE = 'blue'
    GREEN = 'green'
    YELLOW = 'yellow'
    BROWN = 'brown'
    GREY = 'grey'
    PINK = 'pink'
    ORANGE = 'orange'
    PURPLE = 'purple'
    BEIGE = 'beige'
    NAVY = 'navy'
    SILVER = 'silver'
    GOLD = 'gold'
    MULTICOLOR = 'multicolor'

class ShoeSize(Enum):
    EXTRA_SMALL = 'XS'
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    EXTRA_LARGE = 'XL'
    DOUBLE_EXTRA_LARGE = 'XXL'
