import csv, os

class ProductRepository:
    __slots__ = '_products'

    def __init__(self, data_path):
        def data_file_path(filename):
            return os.path.join(data_path, filename)
        self._products = dict()
        shops = self._load_shops(data_file_path('shops.csv'))
        self._tag_shops(data_file_path('tags.csv'), data_file_path('taggings.csv'), shops)
        self._products = self._load_products(data_file_path('products.csv'), shops)

    def _load_shops(self, filename):
        with open(filename, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            assert next(reader) == ['id', 'name', 'lat', 'lng']
            shops_list_to_return = dict()
            for row in reader:
                shops_list_to_return[row[0]] = Shop(row[1], row[2],row[3])
            return shops_list_to_return

    def _tag_shops(self, tags_file, taggings_file, shops):
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
                shops[row[1]].add_tag(tags_dict[row[2]])

    def _load_products(self, filename, shops):
        product_list_to_return = list()
        with open(filename, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            assert next(reader) == ['id', 'shop_id', 'title', 'popularity', 'quantity']
            for row in reader:
                shop_data = shops[row[1]]
                product_list_to_return.append(Product(row[2], row[3], row[4], shop_data))
        return sorted(product_list_to_return, key=lambda x:x.popularity, reverse=True)

    def get_filtered_products(self, lat, lng, radius, tags, count):
        from utils import contains_tags, get_distance_m
        products_list = list()
        for cur_product in self._products:
            #if is_acceptable_shop(cur_product.shop, lat, lng, radius, tags):
            if not contains_tags(tags, cur_product.shop.tags):
                continue
            if get_distance_m(lat,lng,cur_product.shop.lat, cur_product.shop.lng) > radius:
                continue        
            products_list.append(cur_product)
            if (len(products_list) >= count):
                break
        return products_list    

class Shop(object):
    __slots__ = 'name', 'lat', 'lng', '_tags'

    def __init__(self, name, lat, lng):
        self.name = name
        self.lat = float(lat)
        self.lng = float(lng)
        self._tags = set()

    @property
    def tags(self):
        return self._tags

    def add_tag(self, tag):
        self._tags.add(tag)

    def serialize(self): 
        return {           
            'name' : self.name, 
            'lat': self.lat, 
            'lng': self.lng, 
            'tags': [tag for tag in self.tags]
        }

class Product(object):
    __slots__ = 'title', 'popularity', 'quantity', '_shop'

    def __init__(self, title, popularity, quantity, shop):
        self.title = title
        self.popularity = popularity
        self.quantity = quantity
        self._shop = shop

    @property
    def shop(self):
        return self._shop

    def serialize(self): 
        return {           
            'title': self.title, 
            'quantity': self.quantity,
            'popularity': self.popularity,
            'shop': self.shop.serialize()
        }
