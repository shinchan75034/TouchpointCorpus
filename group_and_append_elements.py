def list2tuple(mylist):
     tuple_holder = []
     for element in mylist:
         h = element.split(',')
         tuple_holder.append(tuple(h))
     return tuple_holder

def iterate_through_field(sel, n, collapse=False):
    holder = []
    for user_activity in sel:
        holder.append(user_activity[int(n)])
    if collapse is True:
        holder = list(set(holder)) # in case I want unique and not sequence with duplicate values
    return holder

def group_and_append(list_of_tuples):
    import itertools
    import operator
    it = itertools.groupby(list_of_tuples, operator.itemgetter(0)) # group input list by userid in field 0.
    groups = []
    uniquekeys = []
    sequence_holder = []
    response_holder = []
    for key, subiter in it:
        user_activity = list(subiter)
        groups.append(user_activity)
        uniquekeys.append(key)
        h = iterate_through_field(user_activity, 2, False)
        sequence_holder.append(h)

        r = iterate_through_field(user_activity, 8, True)
        response_holder.append(r)
    return uniquekeys, sequence_holder, response_holder

if __name__ == "__main__":
    import sys
    fib(sys.argv[1])
