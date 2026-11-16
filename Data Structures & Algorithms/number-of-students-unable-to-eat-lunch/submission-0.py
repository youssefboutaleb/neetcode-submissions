class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_sandwich_one = sum(students)
        student_sandwich_zero = len(students) - student_sandwich_one

        while students!=[]: 
            if students[0]==sandwiches[0]:
                if students.pop(0) :
                    student_sandwich_one-=1
                else :
                    student_sandwich_zero-=1
                sandwiches.pop(0)
            else :
                students = students[1:] + [students[0]]
                if sandwiches[0] and student_sandwich_one==0 :
                    break
                if sandwiches[0]==0 and student_sandwich_zero==0 :
                    break
        return len(sandwiches)
