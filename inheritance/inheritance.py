#l'ereditarietà avviene quando una classe
#oltre ai suoi attributi ne eredita altri da altre classi
from chef import Chef
from chinese_chef import Chinese_chef


my_chef = Chef()
second_chef = Chinese_chef()
my_chef.make_chicken()
second_chef.make_chicken()

