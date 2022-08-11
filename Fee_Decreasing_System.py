Fee_Amount = float(input("Please tell me the fee amount between 1 ~ 20 : "))

if 20.00 >= Fee_Amount >= 1.00 :
	Decrease_Percent = (Fee_Amount*40+150)/19

Decreased_Amount=Decrease_Percent*Fee_Amount/100
Fee=Fee_Amount-Decreased_Amount
print(f"Your fee will decrease by %{Decrease_Percent} ; so you will pay {Fee_Amount} - {Decreased_Amount} = {Fee} ")
