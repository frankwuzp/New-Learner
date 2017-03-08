drinks = {
	'martini':{'vodka','vermouth'},
	'black russian':{'cream','kahlua'},
	'white russian':{'cream','kahlua','vodka'},
	'mahattan':{'rye','vermouth','bitters'},
	'screwdriver':{'orange juice','vodka'}
}
for name,contents in drinks.items():
    if 'vodka' in contents:
        print(name)
        