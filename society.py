__author__ = 'Freeman'

import random
from population import *
from handlers import *


class City():
    def __init__(self):
        self.communities = {0: NomadCommunity()}
        self.goods_stock = 10

    def add_community(self):        #can not add empty community
        community_cid = generate_key_(self.communities)
        self.communities.update({community_cid: HouseholdCommunity()})
        return community_cid

    def alter_epoch(self):

        for cid, community in self.communities.items():  # UPGRADE COMMUNITIES
            community.upgrade_community()

        for key, community in self.communities.iteritems():  # KILL ALL EMPTY COMMUNITIES
            if community.check_population_():
                self.communities.pop(key)
                #
        self.communities[0].add_group()  # RANDOMLY GENERATE MIGRANTS IN Nomad community

    #
    # city_goods_bal = 0
    #     for community in self.communities.itervalues():   #PRODUCE and CONSUME goods
    #         city_goods_bal = city_goods_bal - community.consume_goods()
    #         if community.__class__ == HouseholdCommunity:
    #             city_goods_bal = city_goods_bal + community.produce_goods()
    #     self.goods_stock = self.goods_stock + city_goods_bal
    #     print "city goods stock changed to %d" % (self.goods_stock)
    #
    #     city_population = 0
    #     for community in self.communities.itervalues():   #POPULATION GROWTH
    #         community.community_growth()
    #         city_population = city_population + community.population
    #     print "your city became home for %d habitats" % (city_population)

    def __str__(self):
        return "city with %d communities" % (len(self.communities))


class Community():
    def __init__(self, level, type, cid=0,):
        self.cid = cid
        self.level = level
        self.type = type
        self.groups = {}
        self.population = 0

    def upgrade_community(self):
        self.upgrade_()

    def downgrade_community(self):
        self.downgrade_()

    def develop_groups(self, city):
        for key, group in self.groups.items():
            group.develop_(self.cid, city)

    def check_population_(self):
        if self.population == 0 and self.__class__ != NomadCommunity:  # Nomad community will never die
            return True

    def get_population(self):  # create get_iterate function
        ppl = 0
        for group in self.groups.itervalues():
            ppl = ppl + group.group_size
        self.population = ppl

    def consume_goods(self):
        return (self.population * 1)

    def community_growth(self):
        old_pop = self.population
        new_pop = int(self.population * random.uniform(0.95, 1.35))  # balance variable
        if old_pop != new_pop:
            self.population = new_pop
            print "community %s has changed by %d" % (self.type, (new_pop - old_pop))

    def __str__(self):
        return "community %s has %d people in it, level %d" % (self.type, self.population, self.level)


class NomadCommunity(Community):
    def __init__(self):
        Community.__init__(self, 0, "nomad")


    def add_group(self):
        rand_pop = random.randrange(0, 5)
        if rand_pop == 0:
            print "no one desired to come to your shithole city!"
        else:
            key = generate_key_(self.groups)
            self.groups.update({key: Nomads(key, rand_pop)})  # create get_iterate function
            print "new %d dirty immigrants came to your city. %d" % (rand_pop, key)


    def upgrade_(self):
        print "horse in stable farted"


class HouseholdCommunity(Community):
    def __init__(self, level=1):
        Community.__init__(self, level, "household")

    def upgrade_(self):
        self.level = self.level + 1
        self.type = self.type + "+"
        print "community %s upgraded to level %d" % (self.type, self.level)

    def add_group(self, group):
        key = generate_key_(self.groups)
        self.groups.update({key: group})
        print "%d dirty immigrants established new house in your city. %d" % (group.group_size, key)

    def produce_goods(self):
        return self.population * 2  # balance variable





