import time
start_time = time.time()
def strStr(haystack: str, needle: str) -> int:
      
      return haystack.find(needle)
print(strStr("sadbutsad", "bu"))
print("--- %s seconds ---" % (time.time() - start_time))