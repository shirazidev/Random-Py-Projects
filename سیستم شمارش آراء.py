from collections import OrderedDict

n = int(input())


vote_counts = {}


for _ in range(n):
    country = input().strip()
    vote_counts[country] = vote_counts.get(country, 0) + 1


sorted_votes = OrderedDict(sorted(vote_counts.items()))

for country, count in sorted_votes.items():
    print(country, count)
