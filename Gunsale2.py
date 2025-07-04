#---GUN SALE-----#

cent=0
R1=0
R2=0
R5=0
R10=0
R20=0
R50=0
R100=0
R500=0
R1000=0
R5000=0
newL_GUN=[]
newL_QTY=[]
newL_PRICE=[]
TOTAL_AMOUNT=0
DISCOUNT=0
PRICE=0
GUN=['AK47    ','PISTOL  ','SHOTGUN','AIR GUN','AR-15  ','Revolver ']
GUN_PRICE=[500,100,2000,5000,1500,50]
print('  #METHSARA GUN SALE#  ')
print('**************************')
print('GUN_TYPE',end="     ")
print('GUN_PRICE')
for i in range(0,len(GUN)):
    print(i+1,GUN[i],end="     ")
    print(GUN_PRICE[i],"$")
print('**************************') 
print("####5%","discount if you buy more than 10000$####")   
print('your choice end (ENTER 0 KEY)') 
   
for i in range(0,len(GUN)):
   ENTER1=int(input('ENTER GUN TYPE(1,2,3,4,5,6)='))
   if ENTER1==0:
       break
   else:
       pass
   newL_GUN.append(GUN[ENTER1-1])
   ENTER2=int(input('Enter QTY='))
   newL_QTY.append(ENTER2)
for a in newL_GUN:
    for b in range(len(GUN)):
        if a==GUN[b]:
            newL_PRICE.append(GUN_PRICE[b])
        else:
            pass
for i in range(len(newL_PRICE)):
    TOTAL_AMOUNT=TOTAL_AMOUNT+(newL_QTY[i]*newL_PRICE[i])
if TOTAL_AMOUNT>10000:
    RS=TOTAL_AMOUNT*300
    DISCOUNTR=(RS*5)/100
    DISCOUNT=(DISCOUNTR)/300
    PRICE=(RS-DISCOUNTR)/300
else:
    PRICE=TOTAL_AMOUNT

print("\n")    
print('************************************',end="",) 

print('\n     ####METHSARA GUN SALE####')

print('      you are best coustamer.')
print('....................................')
print('    Address: 185/55 Nigombo Rode')
print('    Tel    :          0743591024')
print('    Date   :          DD/MM/YYYY')
print('    Manager:        A.M.METHSARA')
print('....................................')
for i in range(len(newL_GUN)):
    print('   ',newL_GUN[i],end="")
    print('          ',newL_PRICE[i],'*',newL_QTY[i],'$')
print('....................................')
print('    TOTAL AMOUNT:     ',TOTAL_AMOUNT,'$')
print('    DISCOUNT    :     ',DISCOUNT,'$')
print('.....................................')
print('    PRICE       :     ',PRICE,'$')
print('.....................................')
print('            THANK YOU!         ')

print('************************************',end="",) 
print('\n')

print('convert rupice mony!')

#gun sale pay mouny#

x=float(input('pleace enter  your amount($)='))
convert=x*300
R5000=convert//5000
y=convert%5000
R1000=y//1000
z=y%1000
R500=z//500
b=z%500
R100=b//100
c=b%100
R50=c//50
d=c%50
R20=d//20
e=d%20
R10=e//10
f=e%10
R5=f//5
a=f%5
R2=a//2
g=a%2
R1=g//1
cent=g%1
print('\n')

print('****************************************')
print()
print('Rs.5000:','          ',R5000,'*','5000')
print('Rs.1000:','          ',R1000,'   *','1000')
print('Rs.500 :','          ',R500 ,'   *','500 ')
print('Rs.100 :','          ',R100 ,'   *','100 ')
print('Rs.50  :','          ',R50  ,'   *','50  ')
print('Rs.20  :','          ',R20  ,'   *','20  ')
print('Rs.10  :','          ',R10  ,'   *','10  ')
print('Rs.5   :','          ',R5   ,'   *','5   ')
print('Rs.2   :','          ',R2   ,'   *','2   ')
print('Rs.1   :','          ',R1   ,'   *','1   ')
print('cent   :','          ',cent)
print('Total  :','          ',convert)
print()
print('*****************************************')
