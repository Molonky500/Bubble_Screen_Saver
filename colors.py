import pygame as pg
import itertools

color = pg.color.THECOLORS
grey_scale = set([
black := 'black',
gray := 'gray',
gray0 := 'gray0',
gray1 := 'gray1',
gray2 := 'gray2',
gray3 := 'gray3',
gray4 := 'gray4',
gray5 := 'gray5',
gray6 := 'gray6',
gray7 := 'gray7',
gray8 := 'gray8',
gray9 := 'gray9',
gray10 := 'gray10',
gray11 := 'gray11',
gray12 := 'gray12',
gray13 := 'gray13',
gray14 := 'gray14',
gray15 := 'gray15',
gray16 := 'gray16',
gray17 := 'gray17',
gray18 := 'gray18',
gray19 := 'gray19',
gray20 := 'gray20',
gray21 := 'gray21',
gray22 := 'gray22',
gray23 := 'gray23',
gray24 := 'gray24',
gray25 := 'gray25',
gray26 := 'gray26',
gray27 := 'gray27',
gray28 := 'gray28',
gray29 := 'gray29',
gray30 := 'gray30',
gray31 := 'gray31',
gray32 := 'gray32',
gray33 := 'gray33',
gray34 := 'gray34',
gray35 := 'gray35',
gray36 := 'gray36',
gray37 := 'gray37',
gray38 := 'gray38',
gray39 := 'gray39',
gray40 := 'gray40',
gray41 := 'gray41',
gray42 := 'gray42',
gray43 := 'gray43',
gray44 := 'gray44',
gray45 := 'gray45',
gray46 := 'gray46',
gray47 := 'gray47',
gray48 := 'gray48',
gray49 := 'gray49',
gray50 := 'gray50',
gray51 := 'gray51',
gray52 := 'gray52',
gray53 := 'gray53',
gray54 := 'gray54',
gray55 := 'gray55',
gray56 := 'gray56',
gray57 := 'gray57',
gray58 := 'gray58',
gray59 := 'gray59',
gray60 := 'gray60',
gray61 := 'gray61',
gray62 := 'gray62',
gray63 := 'gray63',
gray64 := 'gray64',
gray65 := 'gray65',
gray66 := 'gray66',
gray67 := 'gray67',
gray68 := 'gray68',
gray69 := 'gray69',
gray70 := 'gray70',
gray71 := 'gray71',
gray72 := 'gray72',
gray73 := 'gray73',
gray74 := 'gray74',
gray75 := 'gray75',
gray76 := 'gray76',
gray77 := 'gray77',
gray78 := 'gray78',
gray79 := 'gray79',
gray80 := 'gray80',
gray81 := 'gray81',
gray82 := 'gray82',
gray83 := 'gray83',
gray84 := 'gray84',
gray85 := 'gray85',
gray86 := 'gray86',
gray87 := 'gray87',
gray88 := 'gray88',
gray89 := 'gray89',
gray90 := 'gray90',
gray91 := 'gray91',
gray92 := 'gray92',
gray93 := 'gray93',
gray94 := 'gray94',
gray95 := 'gray95',
gray96 := 'gray96',
gray97 := 'gray97',
gray98 := 'gray98',
gray99 := 'gray99',
gray100 := 'gray100',
green := 'green',
green1 := 'green1',
green2 := 'green2',
green3 := 'green3',
green4 := 'green4',
grey := 'grey',
grey0 := 'grey0',
grey1 := 'grey1',
grey2 := 'grey2',
grey3 := 'grey3',
grey4 := 'grey4',
grey5 := 'grey5',
grey6 := 'grey6',
grey7 := 'grey7',
grey8 := 'grey8',
grey9 := 'grey9',
grey10 := 'grey10',
grey11 := 'grey11',
grey12 := 'grey12',
grey13 := 'grey13',
grey14 := 'grey14',
grey15 := 'grey15',
grey16 := 'grey16',
grey17 := 'grey17',
grey18 := 'grey18',
grey19 := 'grey19',
grey20 := 'grey20',
grey21 := 'grey21',
grey22 := 'grey22',
grey23 := 'grey23',
grey24 := 'grey24',
grey25 := 'grey25',
grey26 := 'grey26',
grey27 := 'grey27',
grey28 := 'grey28',
grey29 := 'grey29',
grey30 := 'grey30',
grey31 := 'grey31',
grey32 := 'grey32',
grey33 := 'grey33',
grey34 := 'grey34',
grey35 := 'grey35',
grey36 := 'grey36',
grey37 := 'grey37',
grey38 := 'grey38',
grey39 := 'grey39',
grey40 := 'grey40',
grey41 := 'grey41',
grey42 := 'grey42',
grey43 := 'grey43',
grey44 := 'grey44',
grey45 := 'grey45',
grey46 := 'grey46',
grey47 := 'grey47',
grey48 := 'grey48',
grey49 := 'grey49',
grey50 := 'grey50',
grey51 := 'grey51',
grey52 := 'grey52',
grey53 := 'grey53',
grey54 := 'grey54',
grey55 := 'grey55',
grey56 := 'grey56',
grey57 := 'grey57',
grey58 := 'grey58',
grey59 := 'grey59',
grey60 := 'grey60',
grey61 := 'grey61',
grey62 := 'grey62',
grey63 := 'grey63',
grey64 := 'grey64',
grey65 := 'grey65',
grey66 := 'grey66',
grey67 := 'grey67',
grey68 := 'grey68',
grey69 := 'grey69',
grey70 := 'grey70',
grey71 := 'grey71',
grey72 := 'grey72',
grey73 := 'grey73',
grey74 := 'grey74',
grey75 := 'grey75',
grey76 := 'grey76',
grey77 := 'grey77',
grey78 := 'grey78',
grey79 := 'grey79',
grey80 := 'grey80',
grey81 := 'grey81',
grey82 := 'grey82',
grey83 := 'grey83',
grey84 := 'grey84',
grey85 := 'grey85',
grey86 := 'grey86',
grey87 := 'grey87',
grey88 := 'grey88',
grey89 := 'grey89',
grey90 := 'grey90',
grey91 := 'grey91',
grey92 := 'grey92',
grey93 := 'grey93',
grey94 := 'grey94',
grey95 := 'grey95',
grey96 := 'grey96',
grey97 := 'grey97',
grey98 := 'grey98',
grey99 := 'grey99',
grey100 := 'grey100',
darkgray := 'darkgray',
darkgreen := 'darkgreen',
darkgrey := 'darkgrey',
dimgray := 'dimgray',
dimgrey := 'dimgrey',
ghostwhite := 'ghostwhite',
lightgray := 'lightgray',
slategray := 'slategray',
slategray1 := 'slategray1',
slategray2 := 'slategray2',
slategray3 := 'slategray3',
slategray4 := 'slategray4',
slategrey := 'slategrey',
snow := 'snow',
snow1 := 'snow1',
snow2 := 'snow2',
snow3 := 'snow3',
snow4 := 'snow4',
antiquewhite := 'antiquewhite',
antiquewhite1 := 'antiquewhite1',
antiquewhite2 := 'antiquewhite2',
antiquewhite3 := 'antiquewhite3',
antiquewhite4 := 'antiquewhite4',
white := 'white',
whitesmoke := 'whitesmoke',
floralwhite := 'floralwhite',
navajowhite := 'navajowhite',
navajowhite1 := 'navajowhite1',
navajowhite2 := 'navajowhite2',
navajowhite3 := 'navajowhite3',
navajowhite4 := 'navajowhite4',
])
# colors---------------------------
colors = set([
aliceblue := 'aliceblue',
aqua := 'aqua',
aquamarine := 'aquamarine',
aquamarine1 := 'aquamarine1',
aquamarine2 := 'aquamarine2',
aquamarine3 := 'aquamarine3',
aquamarine4 := 'aquamarine4',
azure := 'azure',
azure1 := 'azure1',
azure2 := 'azure2',
azure3 := 'azure3',
azure4 := 'azure4',
beige := 'beige',
bisque := 'bisque',
bisque1 := 'bisque1',
bisque2 := 'bisque2',
bisque3 := 'bisque3',
bisque4 := 'bisque4',
blanchedalmond := 'blanchedalmond',
blue := 'blue',
blue1 := 'blue1',
blue2 := 'blue2',
blue3 := 'blue3',
blue4 := 'blue4',
blueviolet := 'blueviolet',
brown := 'brown',
brown1 := 'brown1',
brown2 := 'brown2',
brown3 := 'brown3',
brown4 := 'brown4',
burlywood := 'burlywood',
burlywood1 := 'burlywood1',
burlywood2 := 'burlywood2',
burlywood3 := 'burlywood3',
burlywood4 := 'burlywood4',
cadetblue := 'cadetblue',
cadetblue1 := 'cadetblue1',
cadetblue2 := 'cadetblue2',
cadetblue3 := 'cadetblue3',
cadetblue4 := 'cadetblue4',
chartreuse := 'chartreuse',
chartreuse1 := 'chartreuse1',
chartreuse2 := 'chartreuse2',
chartreuse3 := 'chartreuse3',
chartreuse4 := 'chartreuse4',
chocolate := 'chocolate',
chocolate1 := 'chocolate1',
chocolate2 := 'chocolate2',
chocolate3 := 'chocolate3',
chocolate4 := 'chocolate4',
coral := 'coral',
coral1 := 'coral1',
coral2 := 'coral2',
coral3 := 'coral3',
coral4 := 'coral4',
cornflowerblue := 'cornflowerblue',
cornsilk := 'cornsilk',
cornsilk1 := 'cornsilk1',
cornsilk2 := 'cornsilk2',
cornsilk3 := 'cornsilk3',
cornsilk4 := 'cornsilk4',
crimson := 'crimson',
cyan := 'cyan',
cyan1 := 'cyan1',
cyan2 := 'cyan2',
cyan3 := 'cyan3',
cyan4 := 'cyan4',
darkblue := 'darkblue',
darkcyan := 'darkcyan',
darkgoldenrod := 'darkgoldenrod',
darkgoldenrod1 := 'darkgoldenrod1',
darkgoldenrod2 := 'darkgoldenrod2',
darkgoldenrod3 := 'darkgoldenrod3',
darkgoldenrod4 := 'darkgoldenrod4',
darkkhaki := 'darkkhaki',
darkmagenta := 'darkmagenta',
darkolivegreen := 'darkolivegreen',
darkolivegreen1 := 'darkolivegreen1',
darkolivegreen2 := 'darkolivegreen2',
darkolivegreen3 := 'darkolivegreen3',
darkolivegreen4 := 'darkolivegreen4',
darkorange := 'darkorange',
darkorange1 := 'darkorange1',
darkorange2 := 'darkorange2',
darkorange3 := 'darkorange3',
darkorange4 := 'darkorange4',
darkorchid := 'darkorchid',
darkorchid1 := 'darkorchid1',
darkorchid2 := 'darkorchid2',
darkorchid3 := 'darkorchid3',
darkorchid4 := 'darkorchid4',
darkred := 'darkred',
darksalmon := 'darksalmon',
darkseagreen := 'darkseagreen',
darkseagreen1 := 'darkseagreen1',
darkseagreen2 := 'darkseagreen2',
darkseagreen3 := 'darkseagreen3',
darkseagreen4 := 'darkseagreen4',
darkslateblue := 'darkslateblue',
darkslategray := 'darkslategray',
darkslategray1 := 'darkslategray1',
darkslategray2 := 'darkslategray2',
darkslategray3 := 'darkslategray3',
darkslategray4 := 'darkslategray4',
darkslategrey := 'darkslategrey',
darkturquoise := 'darkturquoise',
darkviolet := 'darkviolet',
deeppink := 'deeppink',
deeppink1 := 'deeppink1',
deeppink2 := 'deeppink2',
deeppink3 := 'deeppink3',
deeppink4 := 'deeppink4',
deepskyblue := 'deepskyblue',
deepskyblue1 := 'deepskyblue1',
deepskyblue2 := 'deepskyblue2',
deepskyblue3 := 'deepskyblue3',
deepskyblue4 := 'deepskyblue4',
dodgerblue := 'dodgerblue',
dodgerblue1 := 'dodgerblue1',
dodgerblue2 := 'dodgerblue2',
dodgerblue3 := 'dodgerblue3',
dodgerblue4 := 'dodgerblue4',
firebrick := 'firebrick',
firebrick1 := 'firebrick1',
firebrick2 := 'firebrick2',
firebrick3 := 'firebrick3',
firebrick4 := 'firebrick4',
forestgreen := 'forestgreen',
fuchsia := 'fuchsia',
gainsboro := 'gainsboro',
gold := 'gold',
gold1 := 'gold1',
gold2 := 'gold2',
gold3 := 'gold3',
gold4 := 'gold4',
goldenrod := 'goldenrod',
goldenrod1 := 'goldenrod1',
goldenrod2 := 'goldenrod2',
goldenrod3 := 'goldenrod3',
goldenrod4 := 'goldenrod4',
greenyellow := 'greenyellow',
honeydew := 'honeydew',
honeydew1 := 'honeydew1',
honeydew2 := 'honeydew2',
honeydew3 := 'honeydew3',
honeydew4 := 'honeydew4',
hotpink := 'hotpink',
hotpink1 := 'hotpink1',
hotpink2 := 'hotpink2',
hotpink3 := 'hotpink3',
hotpink4 := 'hotpink4',
indianred := 'indianred',
indianred1 := 'indianred1',
indianred2 := 'indianred2',
indianred3 := 'indianred3',
indianred4 := 'indianred4',
indigo := 'indigo',
ivory := 'ivory',
ivory1 := 'ivory1',
ivory2 := 'ivory2',
ivory3 := 'ivory3',
ivory4 := 'ivory4',
khaki := 'khaki',
khaki1 := 'khaki1',
khaki2 := 'khaki2',
khaki3 := 'khaki3',
khaki4 := 'khaki4',
lavender := 'lavender',
lavenderblush := 'lavenderblush',
lavenderblush1 := 'lavenderblush1',
lavenderblush2 := 'lavenderblush2',
lavenderblush3 := 'lavenderblush3',
lavenderblush4 := 'lavenderblush4',
lawngreen := 'lawngreen',
lemonchiffon := 'lemonchiffon',
lemonchiffon1 := 'lemonchiffon1',
lemonchiffon2 := 'lemonchiffon2',
lemonchiffon3 := 'lemonchiffon3',
lemonchiffon4 := 'lemonchiffon4',
lightblue := 'lightblue',
lightblue1 := 'lightblue1',
lightblue2 := 'lightblue2',
lightblue3 := 'lightblue3',
lightblue4 := 'lightblue4',
lightcoral := 'lightcoral',
lightcyan := 'lightcyan',
lightcyan1 := 'lightcyan1',
lightcyan2 := 'lightcyan2',
lightcyan3 := 'lightcyan3',
lightcyan4 := 'lightcyan4',
lightgoldenrod := 'lightgoldenrod',
lightgoldenrod1 := 'lightgoldenrod1',
lightgoldenrod2 := 'lightgoldenrod2',
lightgoldenrod3 := 'lightgoldenrod3',
lightgoldenrod4 := 'lightgoldenrod4',
lightgoldenrodyellow := 'lightgoldenrodyellow',
lightgrey := 'lightgrey',
lightgreen := 'lightgreen',
lightpink := 'lightpink',
lightpink1 := 'lightpink1',
lightpink2 := 'lightpink2',
lightpink3 := 'lightpink3',
lightpink4 := 'lightpink4',
lightsalmon := 'lightsalmon',
lightsalmon1 := 'lightsalmon1',
lightsalmon2 := 'lightsalmon2',
lightsalmon3 := 'lightsalmon3',
lightsalmon4 := 'lightsalmon4',
lightseagreen := 'lightseagreen',
lightskyblue := 'lightskyblue',
lightskyblue1 := 'lightskyblue1',
lightskyblue2 := 'lightskyblue2',
lightskyblue3 := 'lightskyblue3',
lightskyblue4 := 'lightskyblue4',
lightslateblue := 'lightslateblue',
lightslategray := 'lightslategray',
lightslategrey := 'lightslategrey',
lightsteelblue := 'lightsteelblue',
lightsteelblue1 := 'lightsteelblue1',
lightsteelblue2 := 'lightsteelblue2',
lightsteelblue3 := 'lightsteelblue3',
lightsteelblue4 := 'lightsteelblue4',
lightyellow := 'lightyellow',
lightyellow1 := 'lightyellow1',
lightyellow2 := 'lightyellow2',
lightyellow3 := 'lightyellow3',
lightyellow4 := 'lightyellow4',
lime := 'lime',
limegreen := 'limegreen',
linen := 'linen',
magenta := 'magenta',
magenta1 := 'magenta1',
magenta2 := 'magenta2',
magenta3 := 'magenta3',
magenta4 := 'magenta4',
maroon := 'maroon',
maroon1 := 'maroon1',
maroon2 := 'maroon2',
maroon3 := 'maroon3',
maroon4 := 'maroon4',
mediumaquamarine := 'mediumaquamarine',
mediumblue := 'mediumblue',
mediumorchid := 'mediumorchid',
mediumorchid1 := 'mediumorchid1',
mediumorchid2 := 'mediumorchid2',
mediumorchid3 := 'mediumorchid3',
mediumorchid4 := 'mediumorchid4',
mediumpurple := 'mediumpurple',
mediumpurple1 := 'mediumpurple1',
mediumpurple2 := 'mediumpurple2',
mediumpurple3 := 'mediumpurple3',
mediumpurple4 := 'mediumpurple4',
mediumseagreen := 'mediumseagreen',
mediumslateblue := 'mediumslateblue',
mediumspringgreen := 'mediumspringgreen',
mediumturquoise := 'mediumturquoise',
mediumvioletred := 'mediumvioletred',
midnightblue := 'midnightblue',
mintcream := 'mintcream',
mistyrose := 'mistyrose',
mistyrose1 := 'mistyrose1',
mistyrose2 := 'mistyrose2',
mistyrose3 := 'mistyrose3',
mistyrose4 := 'mistyrose4',
moccasin := 'moccasin',
navy := 'navy',
navyblue := 'navyblue',
oldlace := 'oldlace',
olive := 'olive',
olivedrab := 'olivedrab',
olivedrab1 := 'olivedrab1',
olivedrab2 := 'olivedrab2',
olivedrab3 := 'olivedrab3',
olivedrab4 := 'olivedrab4',
orange := 'orange',
orange1 := 'orange1',
orange2 := 'orange2',
orange3 := 'orange3',
orange4 := 'orange4',
orangered := 'orangered',
orangered1 := 'orangered1',
orangered2 := 'orangered2',
orangered3 := 'orangered3',
orangered4 := 'orangered4',
orchid := 'orchid',
orchid1 := 'orchid1',
orchid2 := 'orchid2',
orchid3 := 'orchid3',
orchid4 := 'orchid4',
palegoldenrod := 'palegoldenrod',
palegreen := 'palegreen',
palegreen1 := 'palegreen1',
palegreen2 := 'palegreen2',
palegreen3 := 'palegreen3',
palegreen4 := 'palegreen4',
paleturquoise := 'paleturquoise',
paleturquoise1 := 'paleturquoise1',
paleturquoise2 := 'paleturquoise2',
paleturquoise3 := 'paleturquoise3',
paleturquoise4 := 'paleturquoise4',
palevioletred := 'palevioletred',
palevioletred1 := 'palevioletred1',
palevioletred2 := 'palevioletred2',
palevioletred3 := 'palevioletred3',
palevioletred4 := 'palevioletred4',
papayawhip := 'papayawhip',
peachpuff := 'peachpuff',
peachpuff1 := 'peachpuff1',
peachpuff2 := 'peachpuff2',
peachpuff3 := 'peachpuff3',
peachpuff4 := 'peachpuff4',
peru := 'peru',
pink := 'pink',
pink1 := 'pink1',
pink2 := 'pink2',
pink3 := 'pink3',
pink4 := 'pink4',
plum := 'plum',
plum1 := 'plum1',
plum2 := 'plum2',
plum3 := 'plum3',
plum4 := 'plum4',
powderblue := 'powderblue',
purple := 'purple',
purple1 := 'purple1',
purple2 := 'purple2',
purple3 := 'purple3',
purple4 := 'purple4',
red := 'red',
red1 := 'red1',
red2 := 'red2',
red3 := 'red3',
red4 := 'red4',
rosybrown := 'rosybrown',
rosybrown1 := 'rosybrown1',
rosybrown2 := 'rosybrown2',
rosybrown3 := 'rosybrown3',
rosybrown4 := 'rosybrown4',
royalblue := 'royalblue',
royalblue1 := 'royalblue1',
royalblue2 := 'royalblue2',
royalblue3 := 'royalblue3',
royalblue4 := 'royalblue4',
saddlebrown := 'saddlebrown',
salmon := 'salmon',
salmon1 := 'salmon1',
salmon2 := 'salmon2',
salmon3 := 'salmon3',
salmon4 := 'salmon4',
sandybrown := 'sandybrown',
seagreen := 'seagreen',
seagreen1 := 'seagreen1',
seagreen2 := 'seagreen2',
seagreen3 := 'seagreen3',
seagreen4 := 'seagreen4',
seashell := 'seashell',
seashell1 := 'seashell1',
seashell2 := 'seashell2',
seashell3 := 'seashell3',
seashell4 := 'seashell4',
sienna := 'sienna',
sienna1 := 'sienna1',
sienna2 := 'sienna2',
sienna3 := 'sienna3',
sienna4 := 'sienna4',
silver := 'silver',
skyblue := 'skyblue',
skyblue1 := 'skyblue1',
skyblue2 := 'skyblue2',
skyblue3 := 'skyblue3',
skyblue4 := 'skyblue4',
slateblue := 'slateblue',
slateblue1 := 'slateblue1',
slateblue2 := 'slateblue2',
slateblue3 := 'slateblue3',
slateblue4 := 'slateblue4',
springgreen := 'springgreen',
springgreen1 := 'springgreen1',
springgreen2 := 'springgreen2',
springgreen3 := 'springgreen3',
springgreen4 := 'springgreen4',
steelblue := 'steelblue',
steelblue1 := 'steelblue1',
steelblue2 := 'steelblue2',
steelblue3 := 'steelblue3',
steelblue4 := 'steelblue4',
tan := 'tan',
tan1 := 'tan1',
tan2 := 'tan2',
tan3 := 'tan3',
tan4 := 'tan4',
teal := 'teal',
thistle := 'thistle',
thistle1 := 'thistle1',
thistle2 := 'thistle2',
thistle3 := 'thistle3',
thistle4 := 'thistle4',
tomato := 'tomato',
tomato1 := 'tomato1',
tomato2 := 'tomato2',
tomato3 := 'tomato3',
tomato4 := 'tomato4',
turquoise := 'turquoise',
turquoise1 := 'turquoise1',
turquoise2 := 'turquoise2',
turquoise3 := 'turquoise3',
turquoise4 := 'turquoise4',
violet := 'violet',
violetred := 'violetred',
violetred1 := 'violetred1',
violetred2 := 'violetred2',
violetred3 := 'violetred3',
violetred4 := 'violetred4',
wheat := 'wheat',
wheat1 := 'wheat1',
wheat2 := 'wheat2',
wheat3 := 'wheat3',
wheat4 := 'wheat4',
yellow := 'yellow',
yellow1 := 'yellow1',
yellow2 := 'yellow2',
yellow3 := 'yellow3',
yellow4 := 'yellow4',
yellowgreen := 'yellowgreen',
])
colors_hex = {
'aliceblue': '#F0F8FF',
'antiquewhite': '#FAEBD7',
'aqua': '#00FFFF',
'aquamarine': '#7FFFD4',
'azure': '#F0FFFF',
'beige': '#F5F5DC',
'bisque': '#FFE4C4',
'black': '#000000',
'blanchedalmond': '#FFEBCD',
'blue': '#0000FF',
'blueviolet': '#8A2BE2',
'brown': '#A52A2A',
'burlywood': '#DEB887',
'cadetblue': '#5F9EA0',
'chartreuse': '#7FFF00',
'chocolate': '#D2691E',
'coral': '#FF7F50',
'cornflowerblue': '#6495ED',
'cornsilk': '#FFF8DC',
'crimson': '#DC143C',
'cyan': '#00FFFF',
'darkblue': '#00008B',
'darkcyan': '#008B8B',
'darkgoldenrod': '#B8860B',
'darkgray': '#A9A9A9',
'darkgreen': '#006400',
'darkkhaki': '#BDB76B',
'darkmagenta': '#8B008B',
'darkolivegreen': '#556B2F',
'darkorange': '#FF8C00',
'darkorchid': '#9932CC',
'darkred': '#8B0000',
'darksalmon': '#E9967A',
'darkseagreen': '#8FBC8F',
'darkslateblue': '#483D8B',
'darkslategray': '#2F4F4F',
'darkturquoise': '#00CED1',
'darkviolet': '#9400D3',
'deeppink': '#FF1493',
'deepskyblue': '#00BFFF',
'dimgray': '#696969',
'dodgerblue': '#1E90FF',
'firebrick': '#B22222',
'floralwhite': '#FFFAF0',
'forestgreen': '#228B22',
'fuchsia': '#FF00FF',
'gainsboro': '#DCDCDC',
'ghostwhite': '#F8F8FF',
'gold': '#FFD700',
'goldenrod': '#DAA520',
'gray': '#808080',
'green': '#008000',
'greenyellow': '#ADFF2F',
'honeydew': '#F0FFF0',
'hotpink': '#FF69B4',
'indianred': '#CD5C5C',
'indigo': '#4B0082',
'ivory': '#FFFFF0',
'khaki': '#F0E68C',
'lavender': '#E6E6FA',
'lavenderblush': '#FFF0F5',
'lawngreen': '#7CFC00',
'lemonchiffon': '#FFFACD',
'lightblue': '#ADD8E6',
'lightcoral': '#F08080',
'lightcyan': '#E0FFFF',
'lightgoldenrodyellow': '#FAFAD2',
'lightgrey': '#D3D3D3',
'lightgreen': '#90EE90',
'lightpink': '#FFB6C1',
'lightsalmon': '#FFA07A',
'lightseagreen': '#20B2AA',
'lightskyblue': '#87CEFA',
'lightslategray': '#778899',
'lightsteelblue': '#B0C4DE',
'lightyellow': '#FFFFE0',
'lime': '#00FF00',
'limegreen': '#32CD32',
'linen': '#FAF0E6',
'magenta': '#FF00FF',
'maroon': '#800000',
'mediumaquamarine': '#66CDAA',
'mediumblue': '#0000CD',
'mediumorchid': '#BA55D3',
'mediumpurple': '#9370D8',
'mediumseagreen': '#3CB371',
'mediumslateblue': '#7B68EE',
'mediumspringgreen': '#00FA9A',
'mediumturquoise': '#48D1CC',
'mediumvioletred': '#C71585',
'midnightblue': '#191970',
'mintcream': '#F5FFFA',
'mistyrose': '#FFE4E1',
'moccasin': '#FFE4B5',
'navajowhite': '#FFDEAD',
'navy': '#000080',
'oldlace': '#FDF5E6',
'olive': '#808000',
'olivedrab': '#6B8E23',
'orange': '#FFA500',
'orangered': '#FF4500',
'orchid': '#DA70D6',
'palegoldenrod': '#EEE8AA',
'palegreen': '#98FB98',
'paleturquoise': '#AFEEEE',
'palevioletred': '#D87093',
'papayawhip': '#FFEFD5',
'peachpuff': '#FFDAB9',
'peru': '#CD853F',
'pink': '#FFC0CB',
'plum': '#DDA0DD',
'powderblue': '#B0E0E6',
'purple': '#800080',
'red': '#FF0000',
'rosybrown': '#BC8F8F',
'royalblue': '#4169E1',
'saddlebrown': '#8B4513',
'salmon': '#FA8072',
'sandybrown': '#F4A460',
'seagreen': '#2E8B57',
'seashell': '#FFF5EE',
'sienna': '#A0522D',
'silver': '#C0C0C0',
'skyblue': '#87CEEB',
'slateblue': '#6A5ACD',
'slategray': '#708090',
'snow': '#FFFAFA',
'springgreen': '#00FF7F',
'steelblue': '#4682B4',
'tan': '#D2B48C',
'teal': '#008080',
'thistle': '#D8BFD8',
'tomato': '#FF6347',
'turquoise': '#40E0D0',
'violet': '#EE82EE',
'wheat': '#F5DEB3',
'white': '#FFFFFF',
'whitesmoke': '#F5F5F5',
'yellow': '#FFFF00',
'yellowgreen': '#9ACD32',
}
colors = list(colors)
colors.sort()
cycle = itertools.cycle(colors).__next__



# colors---------------------------