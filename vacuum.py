def init(self):
         
         self.locationCondition = {'A': '0', 'B': '0' = random.randint(0, 1)     self.locationCondition['B'] = random.randint(0, 1)


class SimpleReflexVacuumAgent(Environment):
     def init(self, Environment):
         print(Environment.locationCondition)
         Score = 0
         if vacuumLocation == 0:
             print("Vacuum is randomly placed at Location A.")
             if Environment.locationCondition['A'] == 1:
                 print("Location A is Dirty.")
                 
                 Environment.locationCondition['A'] = 0;
                 Score += 1
                 print("Location A has been Cleaned.")
                 
                 print("Moving to Location B…")
                 Score -= 1
                 if Environment.locationCondition['B'] == 1:
                     print("Location B is Dirty.")
                
                     Environment.locationCondition['B'] = 0;
                     Score += 1
                     print("Location B has been Cleaned.")
             else:
                 
                 Score -= 1
                 print("Moving to Location B…")
                 
                 if Environment.locationCondition['B'] == 1:
                     print("Location B is Dirty.")
                     
                     Environment.locationCondition['B'] = 0;
                     Score += 1
                     print("Location B has been Cleaned."
