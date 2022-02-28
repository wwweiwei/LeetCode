class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = collections.defaultdict(set)
        pres = collections.defaultdict(set)
        for course, pre in prerequisites:
            courses[course].add(pre)
            pres[pre].add(course)
        no_pre_courses = [n for n in range(numCourses) if not courses[n]]
        count = 0
        while no_pre_courses:
            no_pre = no_pre_courses.pop()
            count+=1
            for course in pres[no_pre]:
                courses[course].remove(no_pre)
                if not courses[course]:
                    no_pre_courses.append(course)
        return count == numCourses