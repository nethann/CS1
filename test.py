# class Solution(object):
#     def twoSum(self, nums, target):
#         self.nums = nums 
#         self.target = target

#         print(self.nums, self.target)

#         for elements in self.nums:
#             print(elements)

#             if elements == self.target: 
#                 print("already contains") 

            
            




# person = Solution()
# person.twoSum([5,15,20],5)


class myOwnClass():
    def __init__(self,values):
        self.values = values

        print(type(self.values))

    def rm(self,indexOf): 
         if type(self.values) is list:
            self.values.pop(indexOf)
            return self.values
        
                
    def ad(self, value): 
        if type(self.values) is list: 
            self.values.append(value)
            return self.values
        
        if type(self.values) is set: 
            self.values.add(value)
            return self.values


Person = myOwnClass({1,2,3})
print(Person.ad(50))