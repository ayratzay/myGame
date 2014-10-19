__author__ = 'Freeman'

import random
from handlers import *

class Population():
    def __init__(self, pid, size, specialization, good_production, goods_consumption):
        self.group_size = size
        self.specialization = specialization
        self.good_production = good_production
        self.goods_consumption = goods_consumption
        self.pid = pid


class Nomads(Population):
    def __init__(self, pid, size, specialization = "none",good_production = 0, goods_consumption = 1):
        Population.__init__(self, pid, size, specialization, good_production, goods_consumption)

    def develop_(self, cid, city):   # nomad can or join to other community or form new community # balance here!
        variants = city.communities.keys()
        choice = random.choice(variants)
        if choice != 0:
            self.join(city, choice)
        else:
            self.upgrade(city)  # create new community

    def upgrade(self, city):
        self.__class__ = Peasants     #create function that converts self to a Peasant
        self.good_production = 1
        self.specialization = "none"
        city.communities[0].groups.pop(self.pid)
        new_community_cid = city.add_community()
        city.communities[new_community_cid].add_group(self)
        print "nomad community has developed and formed a new community"

    def join(self, city, community_key):
        city.communities[0].groups.pop(self.pid)
        city.communities[community_key].add_group(self)
        print "nomads assimilated into community %d" % (community_key)

class Peasants(Population):
    def __init__(self, size = 1, specialization = "none",good_production = 1, goods_consumption = 1):
        Population.__init__(self, size, specialization, good_production, goods_consumption)

    def develop_(self, cid, city):
        new_group_type = random.choice([Bourgeoisie, Military])
        self.__class__ = new_group_type

class Bourgeoisie(Population):
    def __init__(self, size = 1, specialization = "merchandise",good_production = 4, goods_consumption = 2):
        Population.__init__(self, size, specialization, good_production, goods_consumption)

class Military(Population):
    def __init__(self, size = 1, specialization = "army",good_production = 1, goods_consumption = 1):
        Population.__init__(self, size, specialization, good_production, goods_consumption)
