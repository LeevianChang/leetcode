
import collections

class Solution:

    def is_overlap(self,node1,node2):
        if node1[0]<=node2[0] and  node1[1]>=node2[0]:
            return True
        if node2[0]<=node1[0] and  node2[1]>=node1[0]:
            return True

        return False

    # 建立邻接表
    def build_graph(self,intervals):
        graph = {}
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if self.is_overlap(intervals[i],intervals[j]):
                    if graph.get(i) is None:
                        graph[i] = []
                    if i!=j:
                        graph[i].append(j)

        return graph
                    

    def build_resList(self,intervals,graph):
        resList = []
        isVisited = set()
        for i in range(len(graph)):
            if i in isVisited:
                continue
            if len(graph[i])==0:
                isVisited.add(i)
                resList.append(intervals[i])
                # print(resList)
                continue
            stack = [[i]]
            leftMin = intervals[i][0]
            rightMax = intervals[i][1]
            while len(stack)>0:
                top = stack.pop()

                for j in range(len(top)):
                    if top[j] in isVisited:
                        continue
                    leftMin = min(leftMin,intervals[top[j]][0])
                    rightMax = max(rightMax,intervals[top[j]][1])
                    isVisited.add(top[j])
                    stack.append(graph[top[j]])

            resList.append([leftMin,rightMax])
        resList.sort()
        return resList
                

        

    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        graph = self.build_graph(intervals)
        
        return self.build_resList(intervals,graph)



    def insert2(self, intervals, newInterval):
        resList = []
        if len(intervals)==0:
            return [newInterval]
        used = False
        for i in range(len(intervals)):
            if intervals[i][0]>newInterval[0]:
                used = True
                intervals = intervals[:i]+[newInterval]+intervals[i:]
                break

        if used == False:
            intervals.append(newInterval)

        minLeft = intervals[0][0]
        maxRight = intervals[0][1]
        for i in range(len(intervals)):
            
        
            if  intervals[i][0]<=maxRight:
                minLeft = min(minLeft,intervals[i][0])
                maxRight = max(maxRight,intervals[i][1])
            else:
                resList.append([minLeft,maxRight])
                minLeft = intervals[i][0]
                maxRight = intervals[i][1]
       
    
        resList.append([minLeft,maxRight])
        
        return resList


        
s = Solution()
f = s.insert2([[1,3],[6,9]],[7,10])
print(f)
