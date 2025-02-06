# for (i = 0; i < P.size()-1; ++i)

#   if ccw(p, P[i], P[i+1])

#     sum += angle(P[i], p, P[i+1])

#   else sum -= angle(P[i], p, P[i+1])

# return fabs(sum) > PI ? 1 : -1; // 1/-1 = in/out

# bool ccw(pair<int, int> a, pair<int, int> b, pair<int, int> c) {
#     int z = (b.first - a.first) * (c.second - a.second) 
#           - (b.second - a.second) * (c.first - a.first);
#     return z > 0; // True if c is on the left
# }

# import math

print(math.degrees(1.78))
print(math.radians(1.78))

# https://visualgo.net/en/polygon