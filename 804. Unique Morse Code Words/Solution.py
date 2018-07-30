class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_dict = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
                      "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.",
                      "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-",
                      "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}
        translate_list = []
        for word in words:
            word_list = list(word)
            translate_str = ""
            for letter in word_list:
                translate_str += morse_dict[letter]
            translate_list.append(translate_str)

        return len(sorted(set(translate_list), key=translate_list.index))


if __name__ == '__main__':
    solution = Solution()
    solution.uniqueMorseRepresentations(words=["gin", "zen", "gig", "msg"])
