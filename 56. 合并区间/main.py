
import collections

class Solution:

    def is_overlap(self,left,right):
        if left[0]<=right[0] and left[1]>=right[0]:
            return True
        if right[0]<=left[0] and right[1]>=left[0]:
            return True
        return False

    def build_graph(self,intervals):
        graph = {}
        for i in range(len(intervals)):
            for j in range(i,len(intervals)):
                if self.is_overlap(intervals[i],intervals[j]) and i !=j:
                    if graph.get(i) is None:
                        graph[i] = []
                    if graph.get(j) is None:
                        graph[j] = []
                         
                    graph[i].append(j)
                    graph[j].append(i)
                else:
                    if graph.get(i) is None:
                        graph[i] = []
        return graph


    def merge_graph(self,intervals,graph):
        visted = set()
        resList = []
        print(graph)
        for i in graph:
            if i not in visted:
                curList = [intervals[i][0],intervals[i][1]]
                if len(graph[i])>0:
                    for k in range (len(graph[i])):
                        
                        stack = [graph[i][k]]
                        while len(stack)>0:
                            top = stack.pop()
                            visted.add(top)
                            curList[0] = min(curList[0],intervals[top][0])
                            curList[1] = max(curList[1],intervals[top][1])
                            
                            
                            for z in range(len(graph[top])):
                                if graph[top][z] not in visted:
                                    stack.append(graph[top][z])
                if curList not in resList:
                    resList.append(curList)

                
    

        return resList


    def merge(self, intervals):
        graph =  self.build_graph(intervals)
        return self.merge_graph(intervals,graph)



    def merge2(self, intervals):
        if len(intervals)==0:
            return []
        intervals.sort()
        resList = []
        minLeft = intervals[0][0]
        maxRight = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][1]<=maxRight or intervals[i][0]<=maxRight:
                minLeft = min(minLeft,intervals[i][0])
                maxRight = max(maxRight,intervals[i][1])
                print(minLeft,maxRight)
            else:
                resList.append([minLeft,maxRight])

                minLeft = intervals[i][0]
                maxRight = intervals[i][1]
        resList.append([minLeft,maxRight])
        return resList

        
s = Solution()
f = s.merge2([])
print(f)
