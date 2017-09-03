import json
from pygal.maps.world import World
from json_data.country_codes import get_country_code
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

year = input('Enter the Year (1961-2010) : ')
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == year:
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}

for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 100000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.title = 'World Population by Country, '+year
wm.add('Upto 10m', cc_pops_1)
wm.add('10m to 1b', cc_pops_2)
wm.add('1b or more', cc_pops_3)


wm.render_to_file('world_population.svg')

