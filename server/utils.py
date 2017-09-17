# -*- coding: utf-8 -*-

def get_request_params_for_search(request):
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    radius = request.args.get('radius')
    count = request.args.get('count')
    if not lat or not lng or not radius or not count:
        raise Exception('Required parameters not present')
    if lat > 90 or lat < -90 or lng > 180 or lng < -180:
        raise Exception('Illegal coordinates')

    if 'tags' in request:
        tags = request.args.get('tags').split(',')

    return {
        lat: lat,
        lng: lng,
        radius: radius,
        count: count,
        tags: tags if tags else None
    };
