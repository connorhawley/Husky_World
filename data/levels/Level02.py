from Level import Level
from Enemy import Enemy
class Level02(Level):
    def __init__(self):
        super().__init__()
        self.enemies.add(Enemy(100, 400))
        self.enemies.add(Enemy(64, 64))

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
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "P                                          P",
            "P        P                                 P",
            "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP", ]


