import csv

def data_file_path(filename):
    from server.app import config
    return app.config.DATA_PATH + '/' + filename

class ProductRepository:
    def __init__(self):
        self.shops = dict()
        self._load_shops(data_file_path('shops.csv'))
        self._load_tags(data_file_path('tags.csv'), data_file_path('taggings.csv'))
        self._load_products(data_file_path('products.csv'))
        self._order_products()

    def _load_shops(self, filename):
        with open(filename, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            assert next(reader) == ['id', 'name', 'lat', 'lng']
            for row in reader:
                self.shops[row[0]] = Shop(row[1], row[2],row[3])

    def _load_products(self, filename):
        with open(filename, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            assert next(reader) == ['id', 'shop_id', 'title', 'popularity', 'quantity']
            for row in reader:
                self.shops[row[1]].add_product(Product(row[2], row[3], row[4]))

    def _order_products(self):
        for shop in self.shops:
            shop.order_products()

    def _load_tags(self, tags_file, taggings_file):
        tags_dict = dict()
        with open(tags_file, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            assert next(reader) == ['id', 'tag']
            for row in reader:
                tags_dict[row[0]] = row[1]

        with open(taggings_file, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            assert next(reader) == ['id', 'shop_id', 'tag_id']
            for row in reader:
                self.shops[row[1]].add_tag(tags_dict[row[2]])

class Shop(object):
    __slots__ = 'id', 'name', 'lat', 'lng', '_tags', '_products'

    def __init__(self, name, lat, lng):
        self.name = name
        self.lat = float(lat)
        self.lng = float(lng)
        self._tags = set()
        self.products = list()

    @property
    def tags(self):
        return self._tags

    def add_tag(self, tag):
        self._tags.add(tag)

    @property
    def products(self):
        return self._products
    
    def add_product(self, product):
        self._products.add(product)

    def order_products(self):
        self._products = sorted(self._products, key=lambda x:x[1], reverse=True)

class Product(object):
    __slots__ = 'title', 'popularity', 'quantity'

    def __init__(self, title, popularity, quantity):
        self.title = title
        self.popularity = popularity
        self.quantity = quantity
