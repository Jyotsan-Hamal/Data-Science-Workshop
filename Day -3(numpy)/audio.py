import numpy as np

lis = [-0.7215829 ,-0.20872921 ,-0.40040636, 0.5086889 ,0.14813483 ,-0.24972256 ,-0.21195062, 0.24284983, -0.4665012 ,0.119106926, 0.04314452, 0.17545168, 0.45289978 ,0.13064241 ,0.052069373, -0.036229886 ,-0.76075935 ,0.08742495, -0.2646325, 0.3123021 ,-0.07795048, 0.26772347 ,0.23201081 ,0.013759514, -0.17616989, -0.20985517, -0.12189485, 0.36188006, -0.71317255, -0.050885163, 0.022278491, 0.52083445, -0.073716536 ,0.04530371 ,-0.4277926 ,0.09389298, -0.059243903 ,-0.34590557, -0.16679177, 0.35343242 ,-0.19463915, -0.23271796, 0.23429853, 0.24371889 ,0.58038646, 0.072765104, 0.14763927 ,0.3194871 ,0.32862258 ,-0.038927615, -0.39316875, 0.046659425, -0.703753 ,-0.26784858, 0.2928321 ,0.41384524, -0.31739438 ,-0.16376996, 0.4229099, -0.3233577, -0.13685387 ,-0.443179, -0.116844565, -0.5420643]

lis2 = [-0.43380904, -0.18027155 ,-0.4420077 ,0.6854097 ,0.1897811 ,-0.2504444 ,-0.19869864 ,0.040655825, -0.52910095 ,-0.09537441, -0.10779398 ,0.23636222 ,0.46280527, 0.0543282 ,-0.043862414 ,-0.069240324, -0.38500845 ,0.11125735, -0.13074742, 0.24163054, -0.4525045 ,0.18209842, 0.23122832 ,0.23375514 ,-0.08606696, -0.26553768, -0.11394193 ,0.31116828 ,-0.59251404 ,0.12012606, 0.050306793 ,0.488976 ,0.061253764 ,-0.03340602 ,-0.2889217, 0.20324206, 0.12101625, -0.08333123 ,-0.11914992, 0.22186242, -0.23232472, -0.21586353, 0.33795026, 0.13430575 ,0.47954124 ,0.16900884 ,0.06310188, 0.0373701, 0.11605419, 0.024240024, -0.37388134, 0.0722963 ,-0.27443996 ,-0.33750123, 0.3278707, 0.5895889, 0.15566596, -0.43209362, 0.008194398, 0.12684694 ,-0.007840578, -0.42433313 ,0.10325709 ,-0.47277182]

vector1 = np.array(lis)
vector2 = np.array(lis2)

# Calculate Euclidean distance
distance = np.linalg.norm(vector1 - vector2)

print("Euclidean Distance:", distance)