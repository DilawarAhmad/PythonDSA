class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for [a,b] in prerequisites:
            graph[b].append(a)
            indegree[a] +=1
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        taken = 0
        while queue:
            course =queue.popleft()
            taken+=1
            for nei in graph[course]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    queue.append(nei)
        return taken == numCourses
