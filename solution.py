class Solution:
    def canPermutePalindrome(self, s:str) -> bool:
        odd_characters = set()
        for char in s:
            if char not in odd_characters:
                odd_characters.add(char)
            else:
                odd_characters.remove(char)
        return len(odd_characters) < 2

if __name__ == '__main__':
    solution = Solution()
    print(solution.canPermutePalindrome('code'))
    print(solution.canPermutePalindrome('aab'))
    print(solution.canPermutePalindrome('carerac'))