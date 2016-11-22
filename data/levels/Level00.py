from Level import *
from Enemy import Enemy

class Level00(Level):
    def __init__(self):
        super().__init__()
        # self.enemies.add(Enemy(100, 550))
        # self.enemies.add(Enemy(200, 700))

        self.player = Player(320,448)

        self.level = [
            "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "P             C                            P",
            "P         RRRRRRRRRRR                      P",
            "P                                          P",
            "P                              Z           P",
            "P                   C      RRRRRRR         P",
            "P                 RRRRRR                   P",
            "P                                          P",
            "P      RRRRRRRRRR                          P",
            "P                                          P",
            "P                     RRRRRR               P",
            "P                                          P",
            "P   RRRRRRRRRRR                            P",
            "P                     E                    P",
            "P                 RRRRRRRRRRR              P",
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "R    E   JRJ       J          Z           XR",
            "RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",]


