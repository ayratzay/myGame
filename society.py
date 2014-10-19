__author__ = 'Freeman'

import random
from population import *
from handlers import *


class City():
    def __init__(self):
        self.communities = {0: NomadCommunity()}
        self.goods_stock = 10
        self.population = 0

    def add_community(self):        #can not add empty community
        community_cid = generate_key_(self.communities)
        self.communities.update({community_cid: HouseholdCommunity()})
        return community_cid

    def delete_community(self, cid):
        self.communities.pop(cid)

    def alter_epoch(self):

        for cid, community in self.communities.items():     # UPGRADE COMMUNITIES
            if community.__class__ == HouseholdCommunity:
                community.upgrade_community()

        self.communities[0].add_group()                     # RANDOMLY GENERATE MIGRANTS IN Nomad community

        cpop = 0
        for key, community in self.communities.iteritems():  # KILL ALL EMPTY COMMUNITIES and Recount pop
            if community.check_population_():
                self.delete_community.pop(key)
            else:
                cpop = cpop + community.population
        self.population = cpop

        for cid, community in self.communities.items():     # develop COMMUNITIES
            community.develop_groups(self)


    def __str__(self):
        return "city with %d communities" % (len(self.communities))


class Community():
    def __init__(self, level, type, cid=0,):
        self.cid = cid
        self.level = level
        self.type = type
        self.groups = {}
        self.population = 0

    def develop_groups(self, city):
        for key, group in self.groups.items():
            group.develop_(self.cid, city)

    def check_population_(self):

        pop = 0
        old_pop = self.population
        for community in self.groups.itervalues():
            pop = pop + community.group_size
        self.population = pop
        if old_pop != pop:
            print "community population increased by %d" % (pop - old_pop)
        if self.population == 0 and self.__class__ != NomadCommunity:  # Nomad community will never die
            return True

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


class HouseholdCommunity(Community):
    def __init__(self, level=1):
        Community.__init__(self, level, "household")

    def upgrade_community(self):
        self.level = self.level + 1
        self.type = self.type + "+"
        print "community %s upgraded to level %d" % (self.type, self.level)

    def add_group(self, group):
        key = generate_key_(self.groups)
        self.groups.update({key: group})
        print "%d dirty immigrants established new house in your city. %d" % (group.group_size, key)




