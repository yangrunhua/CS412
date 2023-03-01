# Submit this file to Gradescope
from typing import List
import sys
import math


# you may use other Python standard libraries, but not data
# science libraries, such as numpy, scikit-learn, etc.
def euclidean_dist(point1, point2):
  return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

class Solution:
    def hclus_single_link(self, X: List[List[float]], K: int) -> List[int]:
        """Single link hierarchical clustering
    Args:
      - X: 2D input data
      - K: the number of output clusters
    Returns:
      A list of integers that represent class labels.
      The number does not matter as long as the clusters are correct.
      For example: [0, 0, 1] is treated the same as [1, 1, 0]"""
        n = len(X)
        cs = [[i] for i in range(n)]
        while len(cs) > K:
            min_dist = float("inf")
            closest_cs = None
            for i in range(len(cs)):
                for j in range(i + 1, len(cs)):
                    dist = min([euclidean_dist(X[p1], X[p2]) for p1 in cs[i] for p2 in cs[j]])
                    if dist < min_dist:
                        min_dist = dist
                        closest_cs = (i, j)

            merged = cs[closest_cs[0]] + cs[closest_cs[1]]
            del cs[closest_cs[1]]
            del cs[closest_cs[0]]

            cs.append(merged)

        labels = [-1] * n
        for i in range(len(cs)):
            for j in range(len(cs[i])):
                point_index = cs[i][j]
                labels[point_index] = i
        return labels

    def hclus_average_link(self, X: List[List[float]], K: int) -> List[int]:
        """Average link hierarchical clustering"""
        n = len(X)
        cs = [[i] for i in range(n)]
        while len(cs) > K:
          min_dist = float("inf")
          closest_cs = None
          for i in range(len(cs)):
            for j in range(i + 1, len(cs)):
              dist = sum([euclidean_dist(X[p1], X[p2]) for p1 in cs[i] for p2 in cs[j]]) / (len(cs[i]) * len(cs[j]))
              if dist < min_dist:
                min_dist = dist
                closest_cs = (i, j)

          merged = cs[closest_cs[0]] + cs[closest_cs[1]]
          del cs[closest_cs[1]]
          del cs[closest_cs[0]]

          cs.append(merged)

        labels = [-1] * n
        for i in range(len(cs)):
          for j in range(len(cs[i])):
            point_index = cs[i][j]
            labels[point_index] = i
        return labels

    def hclus_complete_link(self, X: List[List[float]], K: int) -> List[int]:
        """Complete link hierarchical clustering"""
        n = len(X)
        cs = [[i] for i in range(n)]
        while len(cs) > K:
          min_dist = float("inf")
          closest_cs = None
          for i in range(len(cs)):
            for j in range(i + 1, len(cs)):
              dist = max([euclidean_dist(X[p1], X[p2]) for p1 in cs[i] for p2 in cs[j]])
              if dist < min_dist:
                min_dist = dist
                closest_cs = (i, j)

          merged = cs[closest_cs[0]] + cs[closest_cs[1]]
          del cs[closest_cs[1]]
          del cs[closest_cs[0]]

          cs.append(merged)

        labels = [-1] * n
        for i in range(len(cs)):
          for j in range(len(cs[i])):
            point_index = cs[i][j]
            labels[point_index] = i
        return labels


# clusters_raw = []
# N, K, M = sys.stdin.readline().strip().split(' ')
# N, K, M = int(N), int(K), int(M)
# for cluster in sys.stdin.readlines():
#     string_list = cluster.strip().split(' ')
#     c = [float(s) for s in string_list]
#     clusters_raw.append(c)
# 
# s = Solution()
# if M == 0:
#     print(s.hclus_single_link(X=clusters_raw, K=K))
# elif M == 1:
#     print(s.hclus_complete_link(X=clusters_raw, K=K))
# elif M == 2:
#     print(s.hclus_average_link(X=clusters_raw, K=K))
# 