import math #sqrt karekök almak için mat kütüphanesini kullandım.

# Noktaların Tanımlanması
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Öklid Mesafesi İçin Bir Fonksiyon Yazma:
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Mesafelerin hesaplanması:
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

# Minimum mesafenin bulunması:
min_distance = min(distances)

print("Minimum mesafe:", min_distance)