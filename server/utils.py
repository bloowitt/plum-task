# -*- coding: utf-8 -*-

def get_request_params_for_search(args):
    if not args.get('lat') or not args.get('lng') or not args.get('radius') or not args.get('count'):
        raise Exception('Required parameters not present')
    lat = float(args.get('lat'))
    lng = float(args.get('lng'))
    radius = int(args.get('radius'))
    count = int(args.get('count'))
    if lat > 90 or lat < -90 or lng > 180 or lng < -180:
        raise Exception('Illegal coordinates')

    tags = None
    if 'tags' in args:
        tags = args.get('tags').split(',')

    return {
        'lat': lat,
        'lng': lng,
        'radius': radius,
        'count': count,
        'tags': tags
    };
