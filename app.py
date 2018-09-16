# coding=UTF-8

from bottle import route, run, template, request, error, static_file

frett_1_listi = ["Kreml reynir að þvo tilræðismennina af Pútín",
               "Yfirvöld í Kreml fullyrða að tveir menn sem bresk stjórnvöld saka um að hafa reynt að myrða rússneskan fyrrverandi njósnara í mars hafi ekkert með Vladímír Pútín forseta eða ríkisstjórnina að gera. Breska ríkisstjórnin hefur sagt að Pútín hafi sjálfur gefið skipun um tilræðið og að mennirnir tveir vinni fyrir rússnesku herleyniþjónustuna GRU. Mennirnir tveir sem bresk yfirvöld hafa ákært fyrir að hafa eitrað fyrir Sergei Skrípal og dóttur hans Júlíu með taugaeitrinu Novichok í bænum Salisbury á Englandi í mars eru sagðir heita Alexander Petrov og Ruslan Bosjirov. Talsmaður ríkisstjórnar Pútín sagði Interfax-fréttastofunni að hvorugur mannanna tengdist Pútín eða Kreml á nokkurn hátt í dag. Rússnesk stjórnvöld hafa alfarið hafnað því að hafa komið nálægt tilræðinu. Pútín sagði sjálfur að mennirnir tveir væru óbreyttir borgarar í síðustu viku. Tvímenningarnir veittu RT-sjónvarpsstöðinni sem rússneska ríkið styrkir viðtal í vikunni. Þar sögðust þeir vera saklausir ferðamenn sem hafi heimsótt Salisbury til að skemmta sér og að sjá dómkirkjuna þar. Bresk yfirvöld segja hins vegar að leifar af taugaeitrinu hafi fundist á hótelherbergi mannanna í London.",
               "/lidur_b/frett/1/static/frett_1.jpg",
               "Kjartan Kjartansson"]
frett_2_listi = ["Handtóku mann á brókinni",
               "Lögreglan á höfuðborgarsvæðinu hafði í nótt afskipti af ofurölvi manni við Löngulínu. Hann var einungis klæddur í nærbuxur þegar hann handtekinn og samkvæmt dagbók lögreglu vissi hann ekki hvar hann var og gat ekki gefið upp nafn né kennitölu. Hann var vistaður í fangageymslu á meðan ástand hans lagast. Annar maður í annarlegu ástandi var handtekinn í Kringlunni snemma í gærkvöldi. Sá hafði ráðist á öryggisvörð. Þá var þriðji maðurinn í annarlegu ástandi handtekinn í Kópavogi á ellefta tímanum í gær. Sá mun hafa verið ofurölvi og er hann einnig grunaður um hótanir og brot á vopnalögum. Lögreglan handtók einnig tvo menn sem grunaðir eru um að hafa framið rán í fyrirtæki við Reykjavíkurveg. Þá voru nokkrir ökumenn stöðvaðir sem grunaðir eru um akstur undir áhrifum áfengis og/eða fíkniefna. Minnst einn þeirra hafði áður verið sviptur ökuréttindum.",
               "/lidur_b/frett/2/static/frett_2.jpg",
               "Samúel Karl Ólason"]
frett_3_listi = ["Rændi Teslu með snjallsímanum einum saman",
               "21 árs gamall karlmaður í Minnesota í Bandaríkjunum hefur verið handtekinn grunaður um þjófnað á Tesla Model 3 bíl sem var til sýnis í Mall of America verslunarmiðstöðinni í Minneapolis. Fox 9 Minneapolis greinir frá því að maðurinn hafi eingöngu notað snjallsíma sinn til að fremja verknaðinn. Maðurinn var handtekinn þremur dögum síðar í Texas. Lögregla segir líklegast að maðurinn hafi fengið þjónustuver Tesla til að tengja bílinn við Tesla aðgang hans en hann hafði áður tekið sama bíl á leigu hjá bílaleigunni Trevls. John Marino, eigandi Trevsl, segir í samtali við Fox að maðurinn hafi leigt bíla hjá fyrirtækinu í þónokkur skipti. Enn fremur segir Marino að þegar að bílinn hvarf hafi starfsmenn grunað hinn handtekna umsvifalaust vegna þess hve oft hann gortaði sig af vitneskju sinni um öryggisbúnað bílanna. Maðurinn náði að keyra brott á bílnum og slökkti á GPS sendi bílsins. Það var þó ekki nóg því í hver skipti sem maðurinn setti bílinn í hleðslu barst tilkynning um staðsetningu. Marino segir Tesla ekki vera réttu bílana til að ræna vegna þess mikla magns af gögnum sem bílarnir safna.",
               "/lidur_b/frett/3/static/frett_3.jpg",
               "Andri Eysteinsson"]

frettir = [frett_1_listi, frett_2_listi, frett_3_listi]

@route("/")
def index():
    return '''<a href="/lidur_a">Liður A</a><br><a href="/lidur_b">Liður B</a>'''

@route("/lidur_a")
def lidura():
        nofn = {'Nonni': '0104037843', 'Pétur': '0504027812', "Grímur": '4401046544', 'Lalli': '4403021234', 'Doddi': '8705028542',
                'Nína': '0643021276', 'Ásdís': '0401082480', 'Gunna': '3212768989', 'Þóra': '0212072365', 'Þorgerður': '0205125423'}
        return template("links.tpl", nofn)

@route('/lidur_a/kennitala')
def display_forum():
    kenni = request.query.ken
    summa = 0
    for x in kenni:
        summa += int(x)
    return template("thversumma.tpl", kenni = kenni, summa = summa)

@route("/lidur_b")
def lidurb():
    return '''<a href="/lidur_b/frett/1">Frétt 1</a><br><a href="/lidur_b/frett/2">Frétt 2</a><br><a href="/lidur_b/frett/3">Frétt 2</a>'''

@route("/lidur_b/frett/<sida>")
def fre(sida=1):
    return template("frett.tpl", titill = frettir[int(sida)-1][0], meginmal = frettir[int(sida)-1][1], hofundur = frettir[int(sida)-1][3], mynd = frettir[int(sida)-1][2])


@route('/lidur_b/frett/<sida>/static/<skra>')
def static_skrar(skra, sida=1):
    return static_file(skra, root='./public/')

@error(404)
def error404(error):
    return 'Nothing here, sorry'

if __name__ == "__main__":
    run(debug=True)
