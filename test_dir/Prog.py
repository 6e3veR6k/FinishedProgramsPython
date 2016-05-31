gen_list = []
for x in range(10):
    gen_list.append(x)
    y = reduce(lambda x, y: x if x==y else y, gen_list)
    z = reduce(lambda x, y: (x+1)*y, gen_list )
    print(gen_list)
    print '{0} - it\'s y allways, {1} - its a value'.format(y,z)