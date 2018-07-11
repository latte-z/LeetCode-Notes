# reference
# https://segmentfault.com/a/1190000006140476


class Codec:
    ltos = {}
    stol = {}
    COUNTER = 1
    elements = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        shortUrl = self.base10ToBase62(self.COUNTER)
        self.ltos[longUrl] = self.COUNTER
        self.stol[self.COUNTER] = longUrl
        self.COUNTER += 1
        return "http://tinyurl.com/" + shortUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        url = shortUrl[len("http://tinyurl.com/"):len(shortUrl)]
        n = self.base62ToBase10(url)
        return self.stol.get(n)

    def convert(self, ch):
        if '0' <= ch <= '9':
            return ord(ch) - ord('0')
        if 'a' <= ch <= 'z':
            return ord(ch) - ord('a') + 10
        if 'A' <= ch <= 'Z':
            return ord(ch) - ord('A') + 36
        return -1

    def base10ToBase62(self, n):
        sb = ""
        while n != 0:
            sb = self.selectPosInsert(sb, 0, self.elements[n % 62])
            # python3 中的地板除是 //
            n //= 62
        while len(sb) != 6:
            sb = self.selectPosInsert(sb, 0, '0')
        return sb

    def base62ToBase10(self, s):
        n = 0
        for i in range(0, len(s)):
            n = n * 62 + self.convert(s[i])
        return n

    def selectPosInsert(self, nStr, nPos, insertStr):
        str_list = list(nStr)
        str_list.insert(nPos, insertStr)
        return "".join(str_list)


codec = Codec()
codec.decode(codec.encode('https://leetcode.com/problems/design-tinyurl'))
