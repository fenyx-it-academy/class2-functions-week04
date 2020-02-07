def alphabetical_order():
    items = [n for n in input().split('-')]
    #print(items)
    items.sort()
    print('-'.join(items))

alphabetical_order()