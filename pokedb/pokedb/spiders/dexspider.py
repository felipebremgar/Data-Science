import scrapy

class PokedexSpider (scrapy.Spider):

    name = 'dex'
    start_urls = ['https://pokemondb.net/pokedex/all']
    allowed_domains = ['pokemondb.net']

    def parse(self, response):
        for pokemon in response.selector.xpath('//*[@id="pokedex"]/tbody//tr'):
            
            Numero = pokemon.css('span.infocard-cell-data::text').get()
            try:
                variant = pokemon.css('small.text-muted::text').get()
            except:
                variant = None
            if (variant != None):
                Nome = variant
            else:
                Nome = pokemon.css('a.ent-name::text').get()
            Types = []
            Types = pokemon.css('a.type-icon::text').getall()
            try:
                Tipo = Types [0]
                Stipo = Types [1]
            except:
                Tipo = Types [0]
                Stipo = None
            Stats = []
            Stats = pokemon.css('td.cell-num::text').getall()
            HP = Stats [0]
            Atk = Stats [1]
            Def = Stats [2]
            SPAtk = Stats [3]
            SPDef = Stats [4]
            Spd = Stats [5]
            Total = pokemon.css('td.cell-total::text').get()

            yield{
                '#': Numero,
                'Name': Nome,
                'Type 1': Tipo,
                'Type 2': Stipo,
                'HP': Stats [0],
                'Atk': Stats [1],
                'Def': Stats [2],
                'SP Atk': Stats [3],
                'SP Def': Stats [4],
                'Spd': Stats [5],
                'Total': Total,
            }
            

            