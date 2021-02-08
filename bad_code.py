cities = ['Berlin:52.520:13.404', 'Melbourne:37.840:144.946', ]


def find(cities, lat, lon, d):
    from math import sqrt
    found = []
    for city in cities:
        cname, clat, clon = city.split(':')
        clat, clon = float(clat), float(clon)
        deuc = sqrt((clat - lat) ** 2 + (clon - lon) ** 2)
        if deuc < d:
            found.append(cname)
    return found


# --------------------------------------------------------

def dist(city, lat, lon):
    from math import sqrt
    cname, clat, clon = city.split(':')
    clat, clon = float(clat), float(clon)
    return sqrt((clat - lat) ** 2 + (clon - lon) ** 2)


def find(cities, lat, lon, d):
    return [c.split(':')[0] for c in cities if dist(c, lat, lon) < d]


# --------------------------------------------------------

def convert(city):
    name, lat, lon = city.split(':')
    return name, float(lat), float(lon)


def dist(city, lat, lon):
    from math import sqrt
    cname, clat, clon = city
    return sqrt((clat - lat) ** 2 + (clon - lon) ** 2)


def find(cities, lat, lon, d):
    cities = map(convert, cities)
    return [c[0] for c in cities if dist(c, lat, lon) < d]
    # return {c[0] for c in cities if dist(c, lat, lon) < d}
    # return (c[0] for c in cities if dist(c, lat, lon) < d)


# --------------------------------------------------------

def find(cities, lat, lon, d):
    cdists = [(c, dist(c, lat, lon)) for c in map(convert, cities)]
    return [(c[0], dist) for c, dist in cdists if dist < d]
    # {c[0]: dist for c, dist in cdists if dist < d}
    # sum(dist for c, dist in cdists if dist < d)


def find(cities, lat, lon, d):
    cdists = [(c, dist(c, lat, lon)) for c in map(convert, cities)]
    by_dist = lambda cdist: cdist[0]
    return sorted([(c, dist) for c, dist in cdists if dist < d], key=by_dist)


