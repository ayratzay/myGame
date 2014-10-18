__author__ = 'Freeman'

import random

class City():
    def __init__(self):
        self.communities = {}

    def add_migrants(self):
        keys = self.communities.keys()
        if len(keys) != 0:
            key = max(keys) +1
        else:
            key = 0
        rand_pop = random.randrange(0, 5)
        self.communities.update({key : Nomad_community(rand_pop)})
        print "new %d dirty immigrants came to your city" % (rand_pop)

    def alter_epoch(self):    #RANDOMLY GENERATE MIGRANTS #KILL ALL EMPTY COMMUNITIES # UPGRADE COMMUNITIES
        pass

    def __str__(self):
        return "city with %d communities" % (len(self.communities))



class Community():
    def __init__(self, population, level, type):
        self.population = population
        self.level = level
        self.type = type

    def upgrade_community_(self):
        self.level =+ 1
        print "community %s upgraded to level %d" % (self.type, self.level)

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

    def upgrade_to_household(self):
        self.__class__ = Household_community
        self.type = "household"
        self.upgrade_community_()
        print "nomad community has grown to household community"



class Household_community(Community):
    def __init__(self, population, level = 1):
        Community.__init__(self, population, level, "household")


class Dead_community(Community):
    def __init__(self):
        self.type = "Dead community"

def alter_epoch((city, epoch)):   #
    city.alter_epoch()
    epoch =+ 1
    print "for city epoch changed to %d" % (epoch)
    return (city, epoch)
