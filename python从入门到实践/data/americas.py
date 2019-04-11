from pygal_maps_world.maps import World

wm = World()
wm.title = 'Populations of Countries in North America'

wm.add('North America', {'ca': 34126000, 'mx': 309349000, 'us': 1113452000})
# wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')
