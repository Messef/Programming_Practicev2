text_file = open('Python_Programs/__pycache__/file.txt','r')
line_list = text_file.readlines()

def searchInsert(word) -> bool:
        l=0
        r=len(line_list)
        while l < r:
            mid=(l+r) // 2
            print(l, r, mid, line_list[mid])
            if line_list[mid].lower()<word: 
                  l=mid+1
            else: 
                  r=mid
            if line_list[mid][0:5].lower() == word:
                print('h')
                return True


        return False
print(searchInsert("apple"))