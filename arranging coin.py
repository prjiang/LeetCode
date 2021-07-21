def arrangecoins(n):
    r = 0   # 1 ~ k 層塞滿總共要多少硬幣
    k = 1   # 目前要塞的是第幾層
    while True:
        r += k
        if r > n:
            return k - 1
        k += 1

class solution:
    def arrangecoins(self, n: int) -> int:
        return arrangecoins(n)