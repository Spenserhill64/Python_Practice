# Variables for inputs
company_name = input('Please type the name of the insurance company>>')

company_employees = input('Please type the number of employees at the insurance company>>')

location = input('Please type the location of the company>>')

#should have proper postive to negative range
price_policy_low = input('Please provide the lowest price of insurance policies>>')

price_policy_high = input('Please provide the highest price of insurance policy>>')

# f string
print(f'We are {company_name} LLC located in {location}. Our {company_employees} employees can help you find the policy that is right for you with policies ranging from ${price_policy_low} to ${price_policy_high} per month!')