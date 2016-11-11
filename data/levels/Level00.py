from Level import *
from Enemy import Enemy
class Level00(Level):
    def __init__(self):
        super().__init__()
        self.enemies.add(Enemy(100, 550))
        self.enemies.add(Enemy(200, 700))

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
<<<<<<< HEAD
            "P        JPJ       J                       P",
=======
<<<<<<< HEAD
            "P        JPJ                               P",
=======
            "P        JPJ       J                       P",
>>>>>>> refs/remotes/origin/Updated_Level
>>>>>>> master
            "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]


