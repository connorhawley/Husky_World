from Level import *
from Enemy import Enemy
class Level00(Level):
    def __init__(self):
        super().__init__()
        self.enemies.add(Enemy(100, 250))
        self.enemies.add(Enemy(200,300))

        self.level = [
            "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "P         PPPPPPPPPPP                      P",
            "P                                          P",
            "P                                          P",
            "P                          PPPPPPP         P",
            "P                 PPPPPP                   P",
            "P                                          P",
            "P      PPPPPPPPPP                          P",
            "P                                          P",
            "P                     PPPPPP               P",
            "P                                          P",
            "P   PPPPPPPPPPP                            P",
            "P                           E              P",
            "P                 PPPPPPPPPPP              P",
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "P        P                                 P",
            "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]



