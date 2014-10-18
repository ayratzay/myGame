__author__ = 'Freeman'

import random

class City():
    def __init__(self):
        self.communities = {}

    def add_migrants(self):
        rand_pop = random.randrange(0, 5)
        if rand_pop == 0:
            print "no one desired to come to your shithole city!"
        else:
            keys = self.communities.keys()
            if len(keys) != 0:
                key = max(keys) +1
            else:
                key = 0
            self.communities.update({key : Nomad_community(rand_pop)})
            print "new %d dirty immigrants came to your city" % (rand_pop)

    def alter_epoch(self):

        for community in self.communities.itervalues():   # UPGRADE COMMUNITIES
            community.upgrade_community()

        for community in self.communities.itervalues():   #KILL ALL EMPTY COMMUNITIES
            community.check_population_()

        self.add_migrants() #RANDOMLY GENERATE MIGRANTS


    def __str__(self):
        return "city with %d communities" % (len(self.communities))



class Community():
    def __init__(self, population, level, type):
        self.population = population
        self.level = level
        self.type = type

    def upgrade_community(self):
        self.upgrade_()


    def downgrade_community_(self):
        self.level =- 1

    def check_population_(self):
        if self.population == 0:
            self.__class__ = Dead_community
            self.type = "Dead community"

    def __str__(self):
        return "community %s has %d people in it, level %d" % (self.type, self.population,self.level)



class Nomad_community(Community):
    def __init__(self, population = 1):
        Community.__init__(self, population, 0, "nomad")

    def upgrade_(self):
        self.__class__ = Household_community
        self.type = "household"
        self.level = 1
        print "nomad community has grown to household community"


class Household_community(Community):
    def __init__(self, population, level = 1):
        Community.__init__(self, population, level, "household")

    def upgrade_(self):
        self.level = self.level + 1
        self.type = self.type + "+"
        print "community %s upgraded to level %d" % (self.type, self.level)

class Dead_community(Community):
    def __init__(self):
        self.type = "Dead community"
    def upgrade_(self):
        print "someone farted inside a grave"

def alter_epoch((city, epoch)):   #
    city.alter_epoch()
    epoch =+ 1
    print "for city epoch changed to %d" % (epoch)
    return (city, epoch)
