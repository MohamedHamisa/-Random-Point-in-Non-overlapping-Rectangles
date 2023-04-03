class Solution:
    def __init__(self, rects):
        w = [(x2-x1+1)*(y2-y1+1) for x1,y1,x2,y2 in rects]
        self.weights = [i/sum(w) for i in accumulate(w)]
        self.rects = rects

    def pick(self):
        n_rect = bisect.bisect(self.weights, random.random())
        x1, y1, x2, y2 = self.rects[n_rect] 
        return [random.randint(x1, x2),random.randint(y1, y2)]

    '''
    Complexity: Time and space complexity of __init__ is O(n), where n is number of rectangles. Time complexity of pick is O(log n), 
    Space complexity of pick is O(1)
    '''
