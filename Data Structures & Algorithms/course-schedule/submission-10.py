class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses_prereqs = {}

        for course, prereq in prerequisites:
            if course not in courses_prereqs:
                courses_prereqs[course] = [prereq]
            else:
                courses_prereqs[course].append(prereq)

        # visited = set()
        def dfs(course, visited):
            if course in visited:
                return False

            visited.add(course)
            if course in courses_prereqs:
                prereqs = courses_prereqs[course]

                for prereq in prereqs:
                    found = dfs(prereq, visited)
                    if not found:
                        return False

            visited.remove(course)
            courses_prereqs[course] = []

            return True

        for course in range(numCourses):
            is_possible = dfs(course, set())
            if not is_possible:
                return False

        return True
