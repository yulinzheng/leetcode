import image as code

def test_imageSmoother_661():
    img = [[1,1,1],[1,0,1],[1,1,1]]
    assert code.imageSmoother_661(img) == [[0,0,0],[0,0,0],[0,0,0]]
    img = [[100,200,100],[200,50,200],[100,200,100]]
    assert code.imageSmoother_661(img) == [[137,141,137],[141,138,141],[137,141,137]]
    img = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
    assert code.imageSmoother_661(img) == [[4,4,5],[5,6,6],[8,9,9],[11,12,12],[13,13,14]]
