C="""0 0 1
0 0 3
0 1 5
0 1 7
0 2 8
0 2 10
0 2 12
0 3 14
0 3 16
0 4 18
0 4 20
0 5 22
0 5 24
0 5 26
0 6 28
0 6 30
0 7 32
0 7 34
0 7 35
0 8 37
0 8 39
0 9 41
0 9 43
0 9 45
0 10 47
0 10 49
0 11 51
0 11 53
0 12 55
0 12 57
0 12 59
0 13 61
0 13 62
0 14 64
0 14 66
0 14 68
0 15 70
0 15 72
0 16 74
0 16 76
0 16 78
0 17 80
0 17 82
0 18 84
0 18 86
0 19 88
0 19 89
0 19 91
0 20 93
0 20 95
0 21 97
0 21 99
0 21 101
0 22 103
0 22 105
0 23 107
0 23 109
0 23 111
0 24 113
0 24 114
0 25 116
0 25 118
0 26 120
0 26 122
0 27 124
0 27 126
0 28 128
0 29 130
0 30 132
0 31 134
0 32 137
0 33 139
0 34 141
0 35 143
0 36 145
0 37 147
0 38 149
0 39 151
0 40 153
0 41 155
0 42 157
0 43 159
0 44 161
0 45 163
0 46 165
0 47 167
0 48 169
0 49 172
0 49 174
0 50 176
0 51 178
0 52 180
0 53 182
0 54 184
0 55 186
0 56 188
0 57 190
0 58 192
0 59 194
0 60 196
0 61 198
0 62 200
0 63 202
0 64 205
0 65 207
0 66 209
0 67 211
0 68 213
0 69 215
0 70 217
0 71 219
0 72 221
0 72 223
0 73 225
0 74 227
0 75 229
0 76 231
0 77 233
0 78 235
0 79 237
0 80 240
0 81 242
0 82 244
0 83 246
0 84 248
0 85 250
0 86 252
0 87 254
0 89 255
1 91 255
2 94 255
3 97 255
4 99 255
5 102 255
6 104 255
7 107 255
8 110 255
9 112 255
10 115 255
11 118 255
12 120 255
13 123 255
14 125 255
15 128 255
16 131 255
17 133 255
17 136 255
18 139 255
19 141 255
20 144 255
21 147 255
22 149 255
23 152 255
24 154 255
25 157 255
26 160 255
27 162 255
28 165 255
29 168 255
30 170 255
31 173 255
32 175 255
33 178 255
34 181 255
35 183 255
35 186 255
36 189 255
37 191 255
38 194 255
39 196 255
40 199 255
41 202 255
42 204 255
43 207 255
44 210 255
45 212 255
46 215 255
47 218 255
48 220 255
49 223 255
50 225 255
51 228 255
52 231 255
52 233 255
53 236 255
54 239 255
55 241 255
56 244 255
57 246 255
58 249 255
59 252 255
60 254 255
63 255 255
66 255 255
69 255 255
72 255 255
75 255 255
78 255 255
81 255 255
84 255 255
87 255 255
90 255 255
93 255 255
96 255 255
99 255 255
102 255 255
105 255 255
108 255 255
111 255 255
114 255 255
118 255 255
121 255 255
124 255 255
127 255 255
130 255 255
133 255 255
136 255 255
139 255 255
142 255 255
145 255 255
148 255 255
151 255 255
154 255 255
157 255 255
160 255 255
163 255 255
166 255 255
169 255 255
173 255 255
176 255 255
179 255 255
182 255 255
185 255 255
188 255 255
191 255 255
194 255 255
197 255 255
200 255 255
203 255 255
206 255 255
209 255 255
212 255 255
215 255 255
218 255 255
221 255 255
224 255 255
228 255 255
231 255 255
234 255 255
237 255 255
240 255 255
243 255 255
246 255 255
249 255 255
252 255 255
255 255 255"""

import matplotlib as mpl
import numpy as np
from io import StringIO
cm = mpl.colors.ListedColormap(np.genfromtxt(StringIO(C))/255)