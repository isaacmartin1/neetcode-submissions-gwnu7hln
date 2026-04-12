class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {i: [] for i in range(numCourses)}

        for c, p in prerequisites:
            courses[c].append(p)
        

        res = []
        visited = set()
        cycle = set()

        def dfs(course):
            if course in cycle:
                return False

            if course in visited:
                return True
            

            cycle.add(course)
            for p in courses[course]:
                if not dfs(p):
                    return False

            cycle.remove(course)
            visited.add(course)
            res.append(course)

            return True
        

        for course_idx in range(numCourses):
            if not dfs(course_idx):
                return []
        return res

        

