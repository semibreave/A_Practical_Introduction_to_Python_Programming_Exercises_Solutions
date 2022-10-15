import random


rsp = ['r','s','p']

player_win = 0

computer_win= 0


for i in range(5):
 p = input('Enter <r>ock,<s>cissor or <p>aper:')
 c = rsp[random.randint(0,2)]

 if(  ( (p=='r')and(c=='r') ) or ( (p=='s')and(c=='s') ) or ( (p=='p')and(c=='p') )):
  print('You:',p,' Computer:',c,' Is a draw',sep='')

 elif(  ( (p=='r')and(c=='s') ) or ( (p=='s')and(c=='p') ) or ( (p=='p')and(c=='r') )):
  print('You:',p,' Computer:',c,' You win!',sep='')
  player_win += 1

 else:
  print('You:',p,' Computer:',c,' You lose',sep='')
  computer_win += 1

print()

if(player_win > computer_win):print("You're a winner!","Total win:",player_win,"Computer total win:",computer_win)

elif(computer_win > player_win ):print("You lose!","Total win:",player_win,"Computer total win:",computer_win)

else:print("Is a draw game","Total win:",player_win,"Computer total win:",computer_win)

