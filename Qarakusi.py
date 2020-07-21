import random
class rec:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

    def pr(self):
        print(self.l, self.w)

    def matric(self):
        m = []
        for i in range(self.l):
            m.append([])
            for j in range(self.w):
                m[i].append("*")

        for i in range(self.l):
            for j in range(self.w):
                print(m[i][j], end=" ")
            print()
        print()


# mec matrici sarqum
def big_mat(q):
    mat = []
    for i in range(q):
        mat.append([])
        for j in range(q):
            mat[i].append(0)
    return mat


# erkchap matrici print
def pr_arr(ar):
    for i in range(len(ar)):
        for j in range(len(ar)):
            print(ar[i][j], end=" ")
        print()
    print()


# tokosi hashvum
def percent(mato):
    o = 0
    for i in range(len(mato)):
        for j in range(len(mato)):
            if mato[i][j] == 1:
                o = o + 1

    return (o * 100) / (len(mato) * len(mato))


# random matricneri zangvac
arr = []
for i in range(260):
    d = rec(random.randint(1, 5), random.randint(1, 5))

    arr.append(d)

arr = sorted(arr, reverse=True, key=lambda arr: arr.l)

## mec matricneri zangvac

# # mec matric
sevak = big_mat(50)

for i in range(len(karen)):
    for j in range(len(karen)):
        if karen[i][j] == 0:
            l1 = len(karen) - i
            w1 = len(karen) - j
            l_arr = len(arr)
            t = 0
            while t < l_arr:

                if arr[t].l <= l1 and arr[t].w <= w1:
                    # chpcnelu proces

                    for q in range(arr[t].l):
                        for q1 in range(arr[t].w):
                            karen[i + q][j + q1] = 1

                    del arr[t]
                    l_arr = l_arr - 1
                    break

                else:
                    t = t + 1

pr_arr(sevak)
print(percent(sevak), "%")
print(l_arr)