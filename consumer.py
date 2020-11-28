import json
from kafka import KafkaConsumer
from pymongo import MongoClient


# configuração do kafka
brokers = ['localhost:9092']
topic = 'producs-to-update'
consumer = KafkaConsumer(topic, group_id='group1', bootstrap_servers=brokers)

# MongoDB
db_client = MongoClient(host='localhost', port=27017, username="root", password="tigaru", authMechanism='SCRAM-SHA-1', authSource='admin',)
compraz_db = db_client.compraz

# geração da nuvem de palavras em tempo real
frases = ''
for messagem in consumer:
    product = json.loads(messagem.value.decode('utf-8'))
    if product.get('codGetin') != 'SEM GTIN':
        print('products', compraz_db.products.update_one(
            {'gtin': product.get('codGetin')},
            {
                '$set': {
                    'gtin': product.get('codGetin'),
                    'name': product.get('dscProduto'),
                    'ncm': product.get('codNcm'),
                }
            },
            upsert=True
        ).raw_result)
        print('company', compraz_db.company.update_one(
            {'identity': product.get('numCNPJ')},
            {
                '$set': {
                    'identity': product.get('numCNPJ'),
                    'social_name': product.get('nomRazaoSocial'),
                    'fantasy_name': product.get('nomFantasia'),
                    'city': product.get('nomMunicipio'),
                    'zipcode': product.get('numCep'),
                    'street': product.get('nomLogradouro'),
                    'street_number': product.get('numImovel'),
                    'neighborhood': product.get('nomBairro'),
                    'location': {
                        'type': "Point",
                        'coordinates': [product.get('numLatitude'), product.get('numLongitude')]
                    }
                }
            },
            upsert=True,
        ).raw_result)
        print('company_products', compraz_db.company_products.update_one(
            {'identity': product.get('numCNPJ'), 'gtin': product.get('codGetin')},
            {
                '$set': {
                    'gtin': product.get('codGetin'),
                    'identity': product.get('numCNPJ'),
                    'price': float(product.get('valUnitarioUltimaVenda')),
                    'last_buy_date': product.get('dthEmissaoUltimaVenda'),
                }
            },
            upsert=True
        ).raw_result)

        # print(compraz_db.dados.insert(product))
        # print(product.get('codGetin'), product.get('dscProduto'), product.get('valUnitarioUltimaVenda'), '\n')
    # for product in products:
    #     print(product)
