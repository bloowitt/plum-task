# -*- coding: utf-8 -*-

def get_request_params_for_search(args):
    lat = float(args.get('lat'))
    lng = float(args.get('lng'))
    radius = args.get('radius')
    count = args.get('count')
    if not lat or not lng or not radius or not count:
        raise Exception('Required parameters not present')
    if lat > 90 or lat < -90 or lng > 180 or lng < -180:
        raise Exception('Illegal coordinates')

    tags = None
    if 'tags' in args:
        tags = args.get('tags').split(',')

    return {
        lat: lat,
        lng: lng,
        radius: radius,
        count: count,
        tags: tags
    };
