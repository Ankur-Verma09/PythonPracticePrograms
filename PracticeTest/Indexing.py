import numpy as np

def indexing():
    a = np.array(['m','o','n','t','y',' ','p','y','t','h','o','n'])
    # print(a[0:5])
    print(a[2:9])


def indexingOf2DArray():
    a = np.array([[1,2,3],[4,5,6],[7,8,9]])
    # print(a[0]) # extract the 1st row element
    # print(a[:1,1:]) # extract the 1st row  2nd and 3rd element
    # print(a[:2,1:]) # extract the 1st two row's  2nd and 3rd element
    print(a[1:, 1:]) # extract the 2nd two row's  2nd and 3rd element


# indexing()
indexingOf2DArray()