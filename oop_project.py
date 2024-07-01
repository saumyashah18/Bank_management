from BankAccount import *

Suryaraj = BankAccount(2000, "Suryaraj Jadeja")
Saumya = BankAccount(50000,"Saumya Shah")

Suryaraj.getBalance()

Saumya.deposit(5000)
Suryaraj.deposit(10000)

Saumya.withdraw(500)

Saumya.transfer(500, Suryaraj)
Saumya.transfer(500000000, Suryaraj)

Nandii  = Interestrewardacct(30000, "Nandii Kumbhani")

Nandii.getBalance()
Nandii.transfer(100,"Saumya")

Nandii.deposit(400)

Devam = SavingsAcct(1000, "Devam Shah")

Devam.withdraw(3555)
Devam.getBalance()
Devam.fee()
