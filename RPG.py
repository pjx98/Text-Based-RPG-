import random
from libdw import sm as sm



class Maze(sm.SM):
    
    def __init__(self, key = 0, durability = 10):
        self.start_state = 0
        self.key = key
        if self.key > 3:
            self.key = 3
        self.durability = durability
        
    def soldier(self):
        print("\nEncountered Enemy Soldier \n"
              "Prepare to attack.. \n")
        attack = input("Press a to attack")
        if attack == "a":
            if self.soldier_defeat() == True:
                print("Enenmy Soldier : Ughhhhhhh... \n"
                      "You have defeated the enemy soldier\n"
                      "Please continue on your path... \n")
            else:
                self.durability -= 1
                self.AmourDurability()
                print("\nYou have died \n"
                      "You will be revived at your current location \n"
                      "Your armour durability will drop by 1 \n"
                      "You left {} armour durability \n".format(self.durability))
                if self.durability  == 0:
                    return True
                else:
                    return self.soldier()
        else:
            return self.soldier()
        
    def Died(self):
        next_state = 1
        output = "y"
        
        
    
    def AmourDurability(self):
        if self.durability == 0:
            print("You have died \n"
                  "Unfortunately, your durability has reached 0 \n"
                  "You wil not be able to continue on this path \n"
                  "you will be revived at the start of the maze with full durability \n")   
            self.Died = True
            return self.Died
        else:
            pass
        
    
    def getKeys(self):
        return self.key
    
    def soldier_defeat(self):
        x = random.randint(0, 10)
        if x > 3:
            return True
        else:
            return False
    
    def Boss_defeat(self):
        x = random.randint(0, 10)
        if x > 4:
            return True
        else:
            return False
    
    def FinalBoss_defeat(self):
        x = random.randint(0, 10)
        if x > 5:
            return True
        else:
            return False
    
    
    def step(self, inp):
        (x, output) = self.getNextValues(self.state, inp)
        self.state = x
        if output == "F" and x == 99:
            return print("\nThanks for playing! \nHope you had a great time! \nExiting Game...")
        else:         
            return self.step(output) # recursive, ensures that the state machine loops infinitely by itself
    
    def interlude(self): # makes the code cleaner
        print("\nwalking... walking \n"
                      "Hmm, where should I go now?")
    
    def getNextValues(self, state, inp ):
    
        if state == 0:
            
            print("Story: \n \n"
      "You are a knight in the kingdom of Mario. One day, the evil Dark King kidnapped the princess \n"
      "of your kingdom. The King of Mario has ordered you to save the princess from the Dark Lord's \n"
      "clutches and bring her back safely. However, in order to find the Dark King, you need to \n" 
      "find 3 keys from each of his 3 generals which will unlock the door to his personal room where\n"
      "you can defeat him and bring back the princess.\n")
            output = input("Press y to continue...")
            next_state = 0.5
            
            return next_state, output
        
        elif state == 0.5:
            
            if inp == "y":
                print("\nYou have reached the gates of the Dark Lord's castle \n"
                      "You are on your own now \n"
                      "Are you READY?")
                output = input('Press y to continue...')
                next_state = 1
                
            else:
                next_state = 0.5
                output = input("Press y to continue... \n")

            
            return next_state, output
        
        elif state == 1:
            
            if inp == 'y':
                print("\nAs you pushed open the gates, you realise that this is a maze\n"
                      "Navigate through the maze \n"
                      "\nWhere should I move?")
                output = input("Press N to go North")
                next_state = 2
            
            else:
                next_state = 1
                output = input("Press y to continue...")
            
            return next_state, output
    
        elif state == 2:
            
            if inp == 'N':
                self.interlude()
                output = input("Press E to move East")
                next_state = 3 
            
            else:
                next_state = 1
                output = "y"
            
            return next_state, output
        
        elif state == 3:           
            
            if inp == 'E':
                self.interlude()
                output = input("Checkpoint Reached! \n"
                              "Press N to move North \n"
                              "Press S to move South \n"
                              "Press W to move West ")            
                next_state = 3.5 # indicate a crossroad
            
            else:
                next_state = 2
                output = 'N'
                
            return next_state, output
        
        elif state == 3.5:           
            
            if inp == 'N':
                self.interlude()
                self.soldier()
                if self.AmourDurability() == True:
                    next_state = 1 
                    output = "y"
                
                else:
                    next_state = 7       
                    output = input("Press W to move West \n"
                                   "Press S to move South")
          
            elif inp == 'S':
                self.interlude()
                self.soldier()
                if self.AmourDurability() == True:
                    next_state = 1 
                    output = "y"
                    
                else:
                    next_state = 4
                    output = input("Press W to move West \n"
                                   "Press N to move North")
                    
                       
            elif inp == 'W':
               output = 'N'
               next_state = 2
            
            else:
                next_state = 3
                output = 'E'
            
            return next_state, output
        
        elif state == 4:          
            
            if inp == 'W':
                self.interlude()
                next_state = 5
                output = input('Press N to go North \n'
                               'Press E to go East')
            elif inp == 'N':
                next_state = 3
                output ='E'
           
            else:
                next_state = 3.5
                output = 'S'
            
            return next_state, output
        
        elif state == 5:                        
            
            if inp == 'N' or inp == "R" or inp == "r":
                self.interlude()
                next_state = 6
                output = input("Encountered Enemy General! \n"
                               "Defeat him to retrieve the key \n"
                               "Are you Ready? \n"
                               "Press y to continue...")
            elif inp == 'E':
                next_state = 3.5
                output = 'S'
            
            else:
                next_state = 4
                output = 'W'
            
            return next_state, output
        

        elif state == 6:
            
            if inp == 'y':
                print("Fight!\n")
                attack = input("Press a to attack \n")
                if attack == 'a':
                    print("Clang... Clang... Clang... \n"
                          "After a series of sword clashing... \n")
                else:
                    next_state = 6
                    output = "y"
                    return next_state, output
                
                if self.Boss_defeat() == True:
                    self.key += 1
                    print("\nCongratz! You have defeated the boss!\n"  
                          "You have retrieved the key!\n"
                          "You have {} keys, {} keys to go! \n"
                          "Teleporting you to your last checkpoint!".format(self.key, 3 - self.key))
                    
                    output = 'E'
                    next_state = 3
                     
                    
                else:
                    self.durability -= 1
                    if self.AmourDurability() == True:
                        next_state = 1 
                        output = "y"
                        
                    else:
                        output = input("You have died! \n"
                                       "Your armour durability will drop by 1 \n"
                                       "You left {} armour durability \n"
                                       "Press R to retry \n".format(self.durability))
                        next_state = 5
                        
                    
            else:
                next_state = 5
                output = "N"
               
             
            return next_state, output
           
        elif state == 7:
            
            if inp == 'W':
                self.interlude()
                next_state = 8
                output = input("Checkpoint Reached! \n"
                               "Press W to move West \n"
                               "Press S to move South \n"
                               "Press E to move East")
            elif inp == "S":
                next_state = 3
                output = "E"
            else:
               next_state = 3.5
               output = "N"
           
            return next_state , output
                         
        elif state == 8:    
           
            if inp == "W":
                self.interlude()
                next_state = 11
                output = input("Press N to go North \n"
                               "Press W to go West")
            elif inp == "S":
                self.interlude()
                next_state = 9
                output = input("Press E to move East \n"
                               "Press N to go North")
                    
            elif inp == "E":
                next_state = 3.5
                output = "N"
            
            else:
                next_state = 7
                output = "W"
           
            return next_state , output 
        
        elif state == 9:
           
            if inp == "E" or inp == "R" or inp == "r":
                self.interlude()
                next_state = 10
                output = input("Encountered Enemy General! \n"
                               "Defeat him to retrieve the key \n"
                               "Are you Ready? \n"
                               "Press y to continue...")
            elif inp == "N":
                next_state = 7
                output = "W"
            
            else:
                next_state = 8
                output = "S"
            
            return next_state, output
        
        elif state == 10:
           
            if inp == "y":
                print("Fight!\n")
                attack = input("Press a to attack \n")
                if attack == 'a':
                    print("Clang... Clang... Clang... \n"
                          "After a series of sword clashing... \n")
                else:
                    next_state = 10
                    output = "y"
                    return next_state, output
                
                if self.Boss_defeat() == True:
                    self.key += 1
                    self.AmourDurability()
                    print("\nCongratz! You have defeated the boss!\n"  
                          "You have retrieved the key!\n"
                          "You have {} keys, {} keys to go! \n"
                          "Teleporting you to your last checkpoint!".format(self.key, 3 - self.key))
                    next_state =  7
                    output = "W"
                else:
                    self.durability -= 1
                    if self.AmourDurability() == True:
                        next_state = 1 
                        output = "y"
                    else:    
                        output = input("You have died! \n"
                                       "Your armour durability will drop by 1 \n"
                                       "You left {} armour durability \n"
                                       "Press R to retry \n".format(self.durability))
                        next_state = 9
               
            else:
                next_state = 9
                output = "E"
            
            return next_state, output
       
        elif state == 11:
            if inp == "N" or inp == "R":
                self.interlude()
                print("\nYou have reached the Dark Lord's room! \n")
                if self.key == 3:
                    next_state = 12
                    output = input("\nYou have acquired 3 keys. \n"
                                   "You may enter. \n"
                                   "Would you like to unlock the door? \n"
                                   "Press y to continue...")
                else:
                    print("You need {} more key to unlock this door.".format(3 - self.key))
                    next_state = 8
                    output = 'W'
            
            elif inp == "W":
                self.interlude()
                next_state = 13
                output = input("Press S to move South \n"
                               "Press E to move East")
                
            else:
                next_state = 8
                output = "W"
            
                    
            return next_state, output
        
        elif state == 12:
            if inp == "y":
                print("\nDark King: Here to save your little princess?! \n"
                      "Princess: HELP MEEEEE! \n"
                      "Prepare to fight ... \n")
                attack = input("Press a to attack")
                if attack == "a":
                    print("After a long and ardous battle... \n")
                    if self.FinalBoss_defeat() == True:
                        print("\nCongratz! You have defeated the final boss!\n"
                              "You have rescued the princess! \n"
                              "You have completed game!")
                        output = 'F'
                        next_state = 99
                    else:
                        self.durability -= 1
                        if self.AmourDurability() == True:
                            next_state = 1 
                            output = "y"
                        
                        else: 
                            output = input("You have died! \n"
                                           "Your armour durability will drop by 1 \n"
                                           "You left {} armour durability \n"
                                           "Press R to retry \n".format(self.durability))
                            next_state = 11
                else:
                    next_state = 12
                    inp = "y"
                
            else:
                next_state = 11
                output = "N"
                
            return next_state, output 
        
            
        elif state == 13:
            if inp == "S":
                self.interlude()
                self.soldier()
                if self.AmourDurability() == True:
                    next_state = 1 
                    output = "y"
                    
                else:
                    next_state = 14
                    output = input("Press N to move North \n"
                                   "Press E to move East")
                    
            
            elif inp == "E":
                self.interlude()
                next_state = 8
                output = "W"
            
            else:
                next_state = 11
                output = "W"

            return next_state, output
        elif state == 14:
            if inp == "E":
                self.interlude()
                next_state = 15
                output = input("Press S to move South \n"
                               "Press W to move West")
            elif inp == "N":
                next_state = 11
                output = "W"
            
            else:
                next_state = 13
                output = "S"
            
            return next_state, output
        
        elif state == 15:
            
            if inp == "S" or inp == "R" or inp == "r":
                next_state = 16
                output = input("Encountered Enemy General! \n"
                               "Defeat him to retrieve the key \n"
                               "Are you Ready? \n"
                               "Press y to continue...")
            elif inp == "W":
                next_state = 13
                output = "S"
            
            else:
                next_state = 14
                output = "E"
                
            return next_state, output
        
        elif state == 16:
            
            if inp == "y":
                print("Fight!\n")
                attack = input("Press a to attack \n")
                if attack == 'a':
                    print("Clang... Clang... Clang... \n"
                          "After a series of sword clashing... \n")
                else:
                    next_state = 16
                    output = "y"
                    return next_state, output
                
                if self.Boss_defeat() == True:
                    self.key += 1
                    print("\nCongratz! You have defeated the boss!\n"  
                          "You have retrieved the key!\n"
                          "You have {} keys, {} keys to go! \n"
                          "Teleporting you to your last checkpoint!".format(self.key, 3 - self.key))
                    next_state =  7
                    output = "W"
                else:
                    self.durability -= 1
                    if self.AmourDurability() == True:
                        next_state = 1 
                        output = "y"
                    else:     
                        output = input("You have died! \n"
                                       "Your armour durability will drop by 1 \n"
                                       "You left {} armour durability \n"
                                       "Press R to retry \n".format(self.durability))
                        next_state = 15
            else:
                next_state = 15
                output = "S"
               
            return next_state, output
        
               


game = Maze()           
game.start()
game.step(0)
    





    
    
        
        
        
        
    
    
    
        
