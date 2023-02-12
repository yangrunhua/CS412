import math
import random

K = 3

places = []
with open('places.txt', 'r') as f:
    for idx, latlong in enumerate(f):
        lat, long = latlong.strip().split(',')
        lat, long = float(lat), float(long)
        places.append((lat, long))

def euclidean_dist(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)


for iter in range(100):
    centroids = [places[random.randint(0, len(places) - 1)] for i in range(K)]
    clusters_last = [[] for i in range(K)]
    while True:
        clusters = [[] for i in range(K)]
        for idx, (lat, long) in enumerate(places):
            distance = [euclidean_dist(centroids[i], (lat, long)) for i in range(K)]
            clusters[distance.index(min(distance))].append(idx)
        if any([len(i) == 0 for i in clusters]):
            break
        for i in range(K):
            sum_lat, sum_long = float(0), float(0)
            for p in clusters[i]:
                sum_lat += places[p][0]
                sum_long += places[p][1]
            mean_lat, mean_long = sum_lat/len(clusters[i]), sum_long/len(clusters[i])
            centroids[i] = (mean_lat, mean_long)

        if all([a == b for a, b in zip(clusters_last, clusters)]):
            break

        clusters_last = clusters.copy()
    with open('clusters.txt', 'w') as f:
        for c in range(K):
            for j in clusters[c]:
                f.write('{} {}\n'.format(j, c))
    print('This iteration: {} {} {}'.format(*[len(i) for i in clusters]))
