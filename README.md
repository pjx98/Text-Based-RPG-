## **Story**

You are a knight in the kingdom of Mario. One day, the evil Dark King kidnapped the princess
of your kingdom. The King of Mario has ordered you to save the princess from the Dark Lord's
clutches and bring her back safely. However, in order to find the Dark King, you need to 
find 3 keys from each of his 3 generals which will unlock the door to his personal room where
you can defeat him and rescue the princess.

## **Features**

- A huge maze map for players to be lost in 
- Many enemies to meet and bosses to kill
- Simple game available for all ages


## **General Controls**
- Use N S W E to move in North, South, East, West directions 
- Follow the instructions during the game
- Controls are **case sensitive**
- For example:
```
Press N to move North
Press S to move South
Press W to move West
```


## **Armour Durability**
- Players have starting armour durability of 10
- Every death will decrease their armour durability by 1
- When it reaches 0, players will be teleported to the start of the maze with full armour durability

## **Enemy Soldier**
- Basic foot soldier which you will encounter throughout the maze 

## **Enemy General(Boss)**
- There are 3 enemy general at different locations of the maze
- Defeat one to collect a key
- Defeat all three to get 3 keys

## **Dark Lord(Final Boss)**
- Behind a locked door in the maze
- Requires 3 keys dropped from the enemy general to unlock the door
- Defeat him to rescue the princess



# **Code Explanation**

## **Libaries & Modules**
* [Libdw](https://github.com/kurniawano/libdw) - The library used

 `from libdw import sm as sm`
* [Random](https://docs.python.org/3/library/random.html) - The module used

`import random`

## **Running the Game**

As usual, we will use the `start()` and the `step()` methods from the Libdw library to get the game running.

For example:
```python
game = Maze()           
game.start()
game.step(0)
```
In order for the game to run properly, we need the `step()` method to loop infinitely till the player has won the game for which the game will exit on its own.

After the player has defeated the Dark Lord, the condition to exit the game will be called in the form of the `next_state = 'F'` and `output = 99` whereby the `step()` method will return a string instead of its output.

To enable the `step()` method to loop infinitely, we use recursion whereby the `step()` method will return itself till a base case is called.

For example:

``` python
  def step(self, inp):
        (x, output) = self.getNextValues(self.state, inp)
        self.state = x
        if output == "F" and x == 99: # base case
            return print("\nThanks for playing! \nHope you had a great time! \nExiting Game...")
        else:         
            return self.step(output) # recursive, ensures that the state machine loops infinitely by itself
```
## **Class and Constuctor**

There is only one class which is the `Maze(sm.SM)` class which is inherited from its parent **Libdw** class.

The constructor, `__init__` method, contains the inital state, inital number of keys as well as durability.

The default values of the number of keys is 0 while the starting durability is 10.

The number of keys is capped at 3.

For example:
```python
class Maze(sm.SM):
    
    def __init__(self, key = 0, durability = 10):
        self.start_state = 0
        self.key = key
        if self.key > 3:
            self.key = 3
        self.durability = durability
```




## **General Structure**

Players will navigate their way in the maze through the commands given in the console

which uses State Machines from the Libdw library to map out the maze map.


Examples of using state machines:
```python
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
```
Different state numbers correspond to different locations in the maze


Another example:
```python
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
                    
                       
```

## **Repeatable Encounters**

### **Enemy Soldier**

Since the enemy solider is a fixed entity and occurs frequently, we create the `soldier()` method to simplify the code.

The code below shows what happens if you defeat the enemy soldier and the consequences if you failed to do so.

For example:

```python
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

```

Application of the code:

```python
if inp == 'N':
                self.interlude()
                self.soldier()
                if self.AmourDurability() == True:
                    next_state = 1 
                    output = "y"
                
                else:
                    next_state = 7       
                    output = input("Press W to move West \n"
                                   "Press S to move South"
```

### **Armour Durability**

As explained from above,  durability will decrease for every death.

When fighting enemies, there's a chance that the player will die.

After 10 deaths, durability will reach zero which would mean game over in the sense that
the player will be teleported to the beginining of the game where he will start all over again.

For example in the `soldier()` method,
the `self.durability` attribute will decrease by  1 during any fights if the player dies.

The method, `AmourDurability()`, will be used to check if `self.durability` has reached zero, whereby it will return True, and the player will be teleported to the start of the game. 

If `self.durability` has not reached zero, nothing will happen and the player will continue in his path.


For example:
```python
def AmourDurability(self):
        if self.durability == 0:
            print("You have died \n"
                  "Unfortunately, your durability has reached 0 \n"
                  "You wil not be able to continue on this path \n"
                  "you will be revived at the start of the maze with full durability \n")   
            self.Died = True
            return self.Died
        else:
            pass # Nothing happen
```
```python
if self.AmourDurability() == True:
                        next_state = 1  # teleported to entrance of the maze
                        output = "y"
```
 

## **Random Module**

In this game, we will be using the random.randint function to scale the enemies in accordance to
their ranks.

The soldier of course will be the easiest to defeat, thus it has the lowest 'score', followed by the Enemy General and the Dark Lord

For example:

```python
  def soldier_defeat(self):
        x = random.randint(0, 10) # score
        if x > 3:
            return True
        else:
            return False
```

```python
def Boss_defeat(self): ## Enemy General
        x = random.randint(0, 10)
        if x > 4:
            return True
        else:
            return False
```

```python
    def FinalBoss_defeat(self): # Dark Lord
        x = random.randint(0, 10)
        if x > 5:
            return True
        else:
            return False
```

