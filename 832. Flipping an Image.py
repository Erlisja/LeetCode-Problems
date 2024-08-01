"""
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
To flip an image horizontally means that each row of the image is reversed.
For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
For example, inverting [0,1,1] results in [1,0,0].
"""
# Method 1
def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
    # reverse the rows
    for row in image:
        row.reverse()
    # invert the image
    for i, element in enumerate(row):
        if element == 1:
            row[i] = 0
        else:
            row[i] = 1

# Method 2
def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
    # reverse the rows
    def reverse(row):
        i = 0
        j = len(row)-1
        while i<j:
            temp = row[i]
            row[i] = row[j]
            row[j] = temp
            i += 1  
            j -= 1
       
    # invert the elements
    def invert(row):
        for i in range (len(row)):
            if row[i] == 1:
                row [i] = 0
            else:   
                row[i] = 1
    for row in image:
        reverse(row)
        invert(row)
    return image
    
                
