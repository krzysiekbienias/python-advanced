from functools import lru_cache

@lru_cache(maxsize=None)
def is_palindrome(word: str) -> bool:
    
    def wrapper(left:int, right:int):
        if left>=right:
            return True
        if word[left]!=word[right]:
            return False
        return wrapper(left+1,right-1)
    
    return wrapper(0,len(word)-1)
