print("===== Data Science Career Expert System =====")

python = input("Do you like Python? (yes/no): ").lower()
math = input("Do you like Mathematics and Statistics? (yes/no): ").lower()
data = input("Do you like working with Data? (yes/no): ").lower()
ml = input("Are you interested in Machine Learning? (yes/no): ").lower()

if python == "yes" and math == "yes" and ml == "yes":
    result = "Machine Learning"

elif python == "yes" and data == "yes":
    result = "Data Analyst"

elif python == "yes" and ml == "yes":
    result = "Data Scientist"

elif data == "yes":
    result = "Business Intelligence"

else:
    result = "Data Science Beginner"

print("\n--- Expert System Result ---")
print("Recommended Field:", result)
print("Thank you for using the Expert System!")