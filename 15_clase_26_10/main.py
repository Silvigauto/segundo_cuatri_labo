#import modulos.config as config
from modulos.config import Config
from modulos.game import Game


game = Game((800,800), 60)

game.set_caption('POO game')

game.init()