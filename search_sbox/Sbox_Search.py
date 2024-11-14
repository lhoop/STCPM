from DDTLAT import boolean_function_linearity_from_number, algebraic_degree, differential_uniformity
import multiprocessing
N = 5
permDict = {}
MAX_LINEARITY = 16
MAX_DIFF = 6
truthTableMap = {}
Truthtable = []
TruthtableTotal = []

def computeNAND3str0(N):
    res = []
    for i in range(N):
        for j in range(N):
            for k in range(N):
                TT = 0
                for num in range(2 ** N):
                    TT+=((int(1^(((num>>i)&1) & ((num>>j)&1) & ((num>>k)&1)))) << num)
                if TT not in res:
                    res.append(TT)
    return res

def computeNAND3str1(N):
    res = []
    for i in range(N):
        for j in range(N):
            for k in range(N):
                TT = 0
                for num in range(2 ** N):
                    TT+=((int(1^((1^((num>>i)&1)) & ((num>>j)&1) & ((num>>k)&1)))) << num)
                if TT not in res:
                    res.append(TT)
    return res

def computeNAND3str2(N):
    res = []
    for i in range(N):
        for j in range(N):
            for k in range(N):
                TT = 0
                for num in range(2 ** N):
                    TT+=((int(1^((1^((num>>i)&1)) & (1^((num>>j)&1)) & ((num>>k)&1)))) << num)
                if TT not in res:
                    res.append(TT)
    return res

def computeNAND3str3(N):
    res = []
    for i in range(N):
        for j in range(N):
            for k in range(N):
                TT = 0
                for num in range(2 ** N):
                    TT+=((int(1^((1^((num>>i)&1)) & (1^((num>>j)&1)) & (1^((num>>k)&1))))) << num)
                if TT not in res:
                    res.append(TT)
    return res

M5 = list(set([0x55555555, 
    0x33333333, 
    0x66666666, 
    0x0f0f0f0f, 
    0x5a5a5a5a, 
    0x3c3c3c3c, 
    0x69696969, 
    0x00ff00ff, 
    0x55aa55aa, 
    0x33cc33cc, 
    0x66996699, 
    0x0ff00ff0, 
    0x5aa55aa5, 
    0x3cc33cc3, 
    0x69966996, 
    0x0000ffff, 
    0x5555aaaa, 
    0x3333cccc, 
    0x66669999, 
    0x0f0ff0f0, 
    0x5a5aa5a5, 
    0x3c3cc3c3, 
    0x69699696, 
    0x00ffff00, 
    0x55aaaa55, 
    0x33cccc33, 
    0x66999966, 
    0x0ff0f00f, 
    0x5aa5a55a, 
    0x3cc3c33c, 
    0x69969669, 
    0xffffffff, 
    0xaaaaaaaa, 
    0xcccccccc, 
    0x99999999, 
    0xf0f0f0f0, 
    0xa5a5a5a5, 
    0xc3c3c3c3, 
    0x96969696, 
    0xff00ff00, 
    0xaa55aa55, 
    0xcc33cc33, 
    0x99669966, 
    0xf00ff00f, 
    0xa55aa55a, 
    0xc33cc33c, 
    0x96699669, 
    0xffff0000, 
    0xaaaa5555, 
    0xcccc3333, 
    0x99996666, 
    0xf0f00f0f, 
    0xa5a55a5a, 
    0xc3c33c3c, 
    0x96966969, 
    0xff0000ff, 
    0xaa5555aa, 
    0xcc3333cc, 
    0x99666699, 
    0xf00f0ff0, 
    0xa55a5aa5, 
    0xc33c3cc3, 
    0x96696996, 
    0xffffffff, 
    0xaaaaaaaa, 
    0xcccccccc, 
    0x99999999, 
    0xf0f0f0f0, 
    0xa5a5a5a5, 
    0xc3c3c3c3, 
    0x96969696, 
    0xff00ff00, 
    0xaa55aa55, 
    0xcc33cc33, 
    0x99669966, 
    0xf00ff00f, 
    0xa55aa55a, 
    0xc33cc33c, 
    0x96699669, 
    0xffff0000, 
    0xaaaa5555, 
    0xcccc3333, 
    0x99996666, 
    0xf0f00f0f, 
    0xa5a55a5a, 
    0xc3c33c3c, 
    0x96966969, 
    0xff0000ff, 
    0xaa5555aa, 
    0xcc3333cc, 
    0x99666699, 
    0xf00f0ff0, 
    0xa55a5aa5, 
    0xc33c3cc3, 
    0x96696996, 
    0x00000000, 
    0x55555555, 
    0x33333333, 
    0x66666666, 
    0x0f0f0f0f, 
    0x5a5a5a5a, 
    0x3c3c3c3c, 
    0x69696969, 
    0x00ff00ff, 
    0x55aa55aa, 
    0x33cc33cc, 
    0x66996699, 
    0x0ff00ff0, 
    0x5aa55aa5, 
    0x3cc33cc3, 
    0x69966996, 
    0x0000ffff, 
    0x5555aaaa, 
    0x3333cccc, 
    0x66669999, 
    0x0f0ff0f0, 
    0x5a5aa5a5, 
    0x3c3cc3c3, 
    0x69699696, 
    0x00ffff00, 
    0x55aaaa55, 
    0x33cccc33, 
    0x66999966, 
    0x0ff0f00f, 
    0x5aa5a55a, 
    0x3cc3c33c, 
    0x69969669, 
    0xffffffff, 
    0xaaaaaaaa, 
    0xcccccccc, 
    0x99999999, 
    0xf0f0f0f0, 
    0xa5a5a5a5, 
    0xc3c3c3c3, 
    0x96969696, 
    0xff00ff00, 
    0xaa55aa55, 
    0xcc33cc33, 
    0x99669966, 
    0xf00ff00f, 
    0xa55aa55a, 
    0xc33cc33c, 
    0x96699669, 
    0xffff0000, 
    0xaaaa5555, 
    0xcccc3333, 
    0x99996666, 
    0xf0f00f0f, 
    0xa5a55a5a, 
    0xc3c33c3c, 
    0x96966969, 
    0xff0000ff, 
    0xaa5555aa, 
    0xcc3333cc, 
    0x99666699, 
    0xf00f0ff0, 
    0xa55a5aa5, 
    0xc33c3cc3, 
    0x96696996, 
    0x00000000, 
    0x55555555, 
    0x33333333, 
    0x66666666, 
    0x0f0f0f0f, 
    0x5a5a5a5a, 
    0x3c3c3c3c, 
    0x69696969, 
    0x00ff00ff, 
    0x55aa55aa, 
    0x33cc33cc, 
    0x66996699, 
    0x0ff00ff0, 
    0x5aa55aa5, 
    0x3cc33cc3, 
    0x69966996, 
    0x0000ffff, 
    0x5555aaaa, 
    0x3333cccc, 
    0x66669999, 
    0x0f0ff0f0, 
    0x5a5aa5a5, 
    0x3c3cc3c3, 
    0x69699696, 
    0x00ffff00, 
    0x55aaaa55, 
    0x33cccc33, 
    0x66999966, 
    0x0ff0f00f, 
    0x5aa5a55a, 
    0x3cc3c33c, 
    0x69969669, 
    0x00000000, 
    0x55555555, 
    0x33333333, 
    0x66666666, 
    0x0f0f0f0f, 
    0x5a5a5a5a, 
    0x3c3c3c3c, 
    0x69696969, 
    0x00ff00ff, 
    0x55aa55aa, 
    0x33cc33cc, 
    0x66996699, 
    0x0ff00ff0, 
    0x5aa55aa5, 
    0x3cc33cc3, 
    0x69966996, 
    0x0000ffff, 
    0x5555aaaa, 
    0x3333cccc, 
    0x66669999, 
    0x0f0ff0f0, 
    0x5a5aa5a5, 
    0x3c3cc3c3, 
    0x69699696, 
    0x00ffff00, 
    0x55aaaa55, 
    0x33cccc33, 
    0x66999966, 
    0x0ff0f00f, 
    0x5aa5a55a, 
    0x3cc3c33c, 
    0x69969669, 
    0xffffffff, 
    0xaaaaaaaa, 
    0xcccccccc, 
    0x99999999, 
    0xf0f0f0f0, 
    0xa5a5a5a5, 
    0xc3c3c3c3, 
    0x96969696, 
    0xff00ff00, 
    0xaa55aa55, 
    0xcc33cc33, 
    0x99669966, 
    0xf00ff00f, 
    0xa55aa55a, 
    0xc33cc33c, 
    0x96699669, 
    0xffff0000, 
    0xaaaa5555, 
    0xcccc3333, 
    0x99996666, 
    0xf0f00f0f, 
    0xa5a55a5a, 
    0xc3c33c3c, 
    0x96966969, 
    0xff0000ff, 
    0xaa5555aa, 
    0xcc3333cc, 
    0x99666699, 
    0xf00f0ff0, 
    0xa55a5aa5, 
    0xc33c3cc3, 
    0x96696996]))


def bitCount(tt) -> int:
    return bin(tt).count("1")

def judge(tt) -> bool:
    if bitCount(tt) != 16:
        return False
    maxLinearity = 0
    for i in M5:
        num_of_1 = bitCount(tt ^ i)
        t = abs(2 * num_of_1 - 32)
        if t > maxLinearity:
            maxLinearity = t
    if maxLinearity <= MAX_LINEARITY:
        return True
    return False

def build():
    F1_dagger = []
    c0 = 0
    c1 = 0
    for i0 in range(len(Truthtable)):
        tt0 = Truthtable[i0]
        F1_dagger.clear()

        print("has done: %d || total: %d" % (i0, len(Truthtable)))
        for i1 in range(i0, len(Truthtable)):
            tt1 = Truthtable[i1]
            if judge(tt0 ^ tt1):
                #print(judgeList(tt0 ^ tt1))
                F1_dagger.append(tt1)
        #print(len(F1_dagger))
        for i1 in range(len(F1_dagger)):
            #print(i1)
            tt1 = F1_dagger[i1]
            F2_dagger = []
            for i2 in range(i1, len(F1_dagger)):
                tt2 = F1_dagger[i2]
                #c0 += int(judge(tt1 ^ tt2))
                #c1 += int(judge(tt0 ^ tt1 ^ tt2))
                #print(c0, c1)
                #print(judge(tt1 ^ tt2), judge(tt0 ^ tt1 ^ tt2))
                if judge(tt1 ^ tt2) and judge(tt0 ^ tt1 ^ tt2):
                    F2_dagger.append(tt2)
            #print(len(F2_dagger))
            for i2 in range(len(F2_dagger)):
                tt2 = F2_dagger[i2]
                F3_dagger = []
                for i3 in range(i2, len(F2_dagger)):
                    tt3 = F2_dagger[i3]
                    if judge(tt2 ^ tt3) and judge(tt1 ^ tt2 ^ tt3) and \
                        judge(tt0 ^ tt2 ^ tt3) and judge(tt0 ^ tt1 ^ tt2 ^ tt3):
                        F3_dagger.append(tt3)
                
                for i3 in range(len(F3_dagger)):
                    tt3 = F3_dagger[i3]
                    F4_dagger = []
                    for i4 in range(i3, len(F3_dagger)):
                        tt4 = F3_dagger[i4]
                        if judge(tt3 ^ tt4) and judge(tt2 ^ tt3 ^ tt4) and \
                            judge(tt1 ^ tt3 ^ tt4) and judge(tt0 ^ tt3 ^ tt4) and \
                            judge(tt1 ^ tt2 ^ tt3 ^ tt4) and judge(tt0 ^ tt2 ^ tt3 ^ tt4) and \
                            judge(tt0 ^ tt1 ^ tt3 ^ tt4) and judge(tt0 ^ tt1 ^ tt2 ^ tt3 ^ tt4):
                            F4_dagger.append(tt4)
                            sbox = [0 for _ in range(32)]
                            #print(f"{("0"*32+bin(tt0)[2:])[-32:]}\n{("0"*32+bin(tt1)[2:])[-32:]}\n{("0"*32+bin(tt2)[2:])[-32:]}\n{("0"*32+bin(tt3)[2:])[-32:]}\n{("0"*32+bin(tt4)[2:])[-32:]}\n")
                            ttt0 = ("0"*32+bin(tt0)[2:])[-32:]
                            ttt1 = ("0"*32+bin(tt1)[2:])[-32:]
                            ttt2 = ("0"*32+bin(tt2)[2:])[-32:]
                            ttt3 = ("0"*32+bin(tt3)[2:])[-32:]
                            ttt4 = ("0"*32+bin(tt4)[2:])[-32:]
                            for i in range(32):
                                sbox[i] = int(ttt0[i]+ttt1[i]+ttt2[i]+ttt3[i]+ttt4[i], 2)
                                #print(f"{(((tt0 >> (32 - i)) & 1) << 4)}, {(((tt1 >> (32 - i)) & 1) << 3)}, {(((tt2 >> (32 - i)) & 1) << 2)}, {(((tt3 >> (32 - i)) & 1) << 1)}, {((tt4 >> (32 - i)) & 1)}")
                            diff = differential_uniformity(sbox)
                            if diff[0] <= MAX_DIFF:
                                #print(f"{bin(tt0)}, \n{bin(tt1)}, \n{bin(tt2)}, \n{bin(tt3)}, \n{bin(tt4)}")
                                
                                print(f"find a sbox: {sbox}")
                                input()



if __name__ == '__main__':
    N = 5
    res0 = computeNAND3str0(N)
    res1 = computeNAND3str1(N)
    res2 = computeNAND3str2(N)
    res3 = computeNAND3str3(N)
    #print(res0, res1, res2, res3)
    print(len(res0), len(res1), len(res2), len(res3))
    num1 = 2**(N-1)
    num2 = (2**(2**N) - 1)
    res = set([])

    for x0 in range(len(res0)):
        # res = list(set(res))
        for x1 in range(len(res1)):
            tmp0 = res0[x0] & res1[x1]
            for x2 in range(len(res2)):
                tmp1 = tmp0 & res2[x2]
                tmp = bin(tmp1)
                if tmp.count('1') == num1:
                    res.add(tmp1)

    print(len(res))
    resLin16 = []
    cnt = []
    for x in res:
        lin = boolean_function_linearity_from_number(x, N)
        alg = algebraic_degree(x, N)
        if lin <= MAX_LINEARITY and alg > 3:
            cnt.append(lin)
            resLin16.append(x)
            Truthtable.append(x)
    print(len(resLin16), cnt.count(8), cnt.count(10), cnt.count(12), cnt.count(14), cnt.count(16))
    build()