'''tabulation.py tabulates the optimal combinations for a given lenght and a given value table (refered to as 'assortment'). It uses a custom class 'PlankType' to 
store the data about each category in a compact way. Returns a table.'''
from planktype import PlankType


def split_assortment(assortment):
    q1,q2,q3 = [],[],[]

    for item in assortment:                             # Split the assortment by quality. Turn into objects.
        if item[0] == 1:
            q1.append(PlankType(item[1],item[2],item[3]))
        if item[0] == 2:
            q2.append(PlankType(item[1],item[2],item[3]))
        if item[0] == 3:
            q3.append(PlankType(item[1],item[2],item[3]))
    assortment_list = []
    if len(q1):
        assortment_list.append(q1)
    if len(q2):
        assortment_list.append(q2)
    if len(q3):
        assortment_list.append(q3)
    # assortment_list = [q1,q2,q3]
    return assortment_list


def tabulate(assortment, n = 70):
    n += 1                                                          # just to avoid having range(n+1)
    quality = assortment[0].quality
    values = [None for x in range(n)]
    values[0] = 0
    cuts = [[] for x in range(n)]
    offcuts = [0 for x in range(n)]
    table = []

    for cm in range(n):

        if values[cm] is not None:                                  # if a cut can be made
            offcut = 0
            
            for item in assortment:                                 # for types in the assortment
                next = cm + item.length

                if (next < n):                                      # if not out of bound
                    new_val = values[cm] + item.value
                    if (not values[next] or values[next] < new_val):        # if the next spot is empty OR if the tabulated value is inferior to current one

                        values[next] = new_val                      # update the lists (tables)
                        combi = [*cuts[cm], [item.name, item.length]]
                        cuts[next] = [*combi]
    
        else: 
            offcut += 1 
            values[cm] = values[cm-1]        # same as previous
            cuts[cm] = [*cuts[cm-1]]
            offcuts[cm] += offcut            # but offcuts is updated

    for cm in range(n):
        if (cm < (n-1)):
            if values[cm + 1] < values[cm]:        # if next value is lower than prev: update
                values[cm +1 ] = values[cm]
                cuts[cm + 1] = cuts[cm]
                offcuts[cm + 1] = offcuts[cm] + 1  # add 1 rests 
        
        entry = []                                 # combine the classified cuts with the offcuts
        if cuts[cm]:
            for cut in cuts[cm]:
                entry.append(cut)
        if offcuts[cm] != 0:
            entry.append([quality+1,offcuts[cm]])  # quality of the offcut goes up (lower quality)
        new_entry = []
        new_entry.append(entry)
        new_entry.append(values[cm])
        table.append(new_entry)


    return table

def get_table(assortment, n):
    table = []

    for quality in split_assortment(assortment):
        table.append(tabulate(quality, n))

    return table

