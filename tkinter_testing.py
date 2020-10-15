# import the modules  
import tkinter 
import random 
  
# list of possible colour. 
attacks = [['Fireball', 30], ['Slash', 20]] 
enemy_health = random.randint(100, 200)
player_health = 300

timeleft = 1
attacked_time = 0
  
# function that will start the game. 
def startGame(event): 
      
    if timeleft == 1: 
          
        # start the countdown timer. 
        countdown() 
          
    attack() 
   
def attack(): 
  
    # use the globally declared 'score' 
    # and 'play' variables above. 
    global enemy_health 
    global player_health
    global timeleft 
    global attacked_time
  
    # if a game is currently in play 
    if timeleft > 0: 
  
        # make the text entry box active. 
        e.focus_set() 
  
        # if the colour typed is equal 
        # to the colour of the text 
        for i in attacks:
            if e.get().lower() == i[0].lower(): 
              enemy_health -= i[1]
              if enemy_health <= 0:
                  enemy_health = 0
                  timeleft = 0
              break
        #if timeleft % 2 == 0:
        
        # clear the text entry box. 
        e.delete(0, tkinter.END) 
          
          
        # change the colour to type, by changing the 
        # text _and_ the colour to a random colour value 
          
        # update the enemy_health. 
        scoreLabel.config(text = "Enemy Health: " + str(enemy_health)) 
        player_label.config(text = "Player Health: " + str(player_health))
  
  
# Countdown timer function  
def countdown(): 
  
    global timeleft 
    global player_health
    player_health -= random.randint(10,40)
    # if a game is in play 
    if timeleft > 0: 
  
        # decrement the timer. 
        timeleft += 1
          
        # update the time left label 
        timeLabel.config(text = "Time played: "
                               + str(timeleft)) 
                                 
        # run the function again after 1 second. 
        timeLabel.after(1000, countdown) 
    elif timeleft == 0 and enemy_health == 0:
        timeLabel.config(text="Victory!")
    elif player_health <= 0:
        timeLabel.config(text="Defeat!")
  
# Driver Code 
  
# create a GUI window 
root = tkinter.Tk() 
  
# set the title 
root.title("COLORGAME") 
  
# set the size 
root.geometry("375x200") 
  
# add an instructions label
instruct_text = "Available attacks: "
for i in attacks:
    instruct_text += i[0] + " "
instructions = tkinter.Label(root, text = instruct_text, 
                                      font = ('Helvetica', 12)) 
instructions.pack()  
  
# add a score label 
scoreLabel = tkinter.Label(root, text = "Press enter to start", 
                                      font = ('Helvetica', 12)) 
scoreLabel.pack() 

player_label = tkinter.Label(root, text = "Player Health: " + str(player_health), 
                                      font = ('Helvetica', 12))
player_label.pack()
# add a time left label 
timeLabel = tkinter.Label(root, text = "Time left: " +
              str(timeleft), font = ('Helvetica', 12)) 
                
timeLabel.pack() 
  
# add a label for displaying the colours 
label = tkinter.Label(root, font = ('Helvetica', 60)) 
label.pack() 
  
# add a text entry box for 
# typing in colours 
e = tkinter.Entry(root) 
  
# run the 'startGame' function  
# when the enter key is pressed 
root.bind('<Return>', startGame) 
e.pack() 
  
# set focus on the entry box 
e.focus_set() 
  
# start the GUI 
root.mainloop() 