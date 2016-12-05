from Level import *
from Enemy import Enemy

class Level00(Level):
    def __init__(self):
        super().__init__()

        self.player = Player(96, 112)


        self.level =[
            "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP           ",
            "P                                                P",
            "P                                                P",
            "P                                                P",
            "P                                                P",
            "PPPPPPP                                          P",
            "P     P                                          P",
            "P     PPP                                        P",
            "P       P                                        P",
            "P       PPPP                                     PPPPPPPPPPPP",
            "P          P                                     P          P",
            "P          PPP                       E           P          P",
            "P            P      K   C   K  I  C     I    C   P          P",
            "P            PPP    RRRRRRRRR   RRRRRRRR   RRRRRRP          P",
            "P                   UUUUUUUUU                               P",
            "P                                                           P",
            "P                                                           P",
            "P                                                           P",
            "P                                                           P",
            "P                                                           P",
            "R      E     E    JRJ Z          Z  J    J              X   R",
            "RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR", ]

    

