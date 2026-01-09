Amount =int(input("Withdraw user amount"))
note1 =Amount//100
note2 =(Amount%100)//5
note3 = ((Amount%100)%50)//10
print("amount for 100 rupes",note1)
print("amount for 50 rupes",note2)
print("amount for 10 rupes",note3)