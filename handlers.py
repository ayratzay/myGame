__author__ = 'Freeman'

def generate_key_(obj):
    keys = obj.keys()
    if len(keys) != 0:
        return max(keys) + 1
    else:
        return 0

def alter_epoch((city, epoch)):  #
    city.alter_epoch()
    epoch = epoch + 1
    print "for city epoch changed to %d" % (epoch)
    return (city, epoch)