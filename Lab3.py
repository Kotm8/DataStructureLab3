def find_min_cost(official, memo):
    if official in memo:
        return memo[official]
    
    min_cost = float('inf')
    for bribe, required_signatures in signature_requirements[official]:
        cost = bribe
        for sub in required_signatures:
            cost += find_min_cost(sub, memo)
        min_cost = min(min_cost, cost)
    
    memo[official] = min_cost
    return min_cost


official_amount = int(input("Enter number of officials: "))


subordinates = [[] for _ in range(official_amount)]
signature_requirements = [[] for _ in range(official_amount)]


for i in range(official_amount):
    input_data = input(f"Enter subordinates and signature requirements for official {i}: ").split()
    num_subordinates = int(input_data[0])
    index = 1
    
    if num_subordinates > 0:
        subordinates[i] = list(map(int, input_data[1:num_subordinates + 1]))
        index = num_subordinates + 1
    
    num_requirements = int(input_data[index])
    index += 1
    
    for _ in range(num_requirements):
        bribe = int(input_data[index])
        num_required_signatures = int(input_data[index + 1])
        required_signatures = [int(id) for id in input_data[index + 2:index + 2 + num_required_signatures]]
        signature_requirements[i].append((bribe, required_signatures))
        index += 2 + num_required_signatures


memo = {}
result = find_min_cost(0, memo)
print(f"Minimum bribe cost to obtain the top official's signature: {result}")
