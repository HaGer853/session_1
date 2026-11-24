team_members=int(input("Enter your number of team members: "))
number_month=int(input("Enter number of month: "))
salary=float(input("Enter your salary: "))
total_cloud=float(input("enter your total cloud cost: "))
salary_cost= team_members * number_month * salary
subtotal= salary_cost + total_cloud
vat = subtotal * .14
total_cloud =subtotal + vat
print(f"salary_cost = {salary_cost : ,.2f}")
print(f"subtotal = {subtotal : ,.2f}")
print(f"vat = {vat : ,.2f}")
print(f"total_cloud = {total_cloud : ,.2f}")

