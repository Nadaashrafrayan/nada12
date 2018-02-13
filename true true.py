a = str(input(" player 1 enter your name:"))
b = str(input(" player 2 enter your name:"))
ncoins=int(input("enter num of coins you have :"))
bank_1=0
bank_2=0
sum=bank_1+bank_2
Rcoins =ncoins
while Rcoins>0:
    print (a)
    if bank_1==0:
            print ("choose from 1 to",ncoins-1)
    else:
            print ("choose from 1 to",player_2*2)
            if player_1>player_2*2:
              print("invaled number")
              print (a)
              print ("choose from 1 to", player_2 * 2)
              player_1=int(input("-->:"))
        
    player_1=int(input("-->:"))
          
    bank_1 =bank_1 +player_1
    Rcoins=Rcoins-player_1
    print("Rcoins =",Rcoins)    

    if Rcoins<=0:
               print (a,",you win")
    else:
              print (b)
              print ("choose from 1 to", player_1 * 2)

              player_2=int(input("-->:"))
              if player_2>player_1*2:
                   print("invaled number")
                   print (b)
                   print ("choose from 1 to", player_1 * 2)
                   
                   player_2=int(input("-->:"))
                   bank_2=bank_2+player_2
                   Rcoins=Rcoins-player_2

              else:
                   bank_2=bank_2+player_2
         
                   Rcoins=Rcoins-player_2
              if Rcoins==0:
                      print (b,"is win")
    print("Rcoins =",Rcoins)    
