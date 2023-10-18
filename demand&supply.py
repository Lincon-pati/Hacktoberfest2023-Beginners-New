import matplotlib.pyplot as plt

# Define demand and supply functions
def demand(quantity):
    return 100 - 2 * quantity

def supply(quantity):
    return 2 * quantity

# Generate a range of quantities
quantities = list(range(0, 51))

# Calculate corresponding prices using demand and supply functions
prices_demand = [demand(qty) for qty in quantities]
prices_supply = [supply(qty) for qty in quantities]

# Plot the demand and supply curves
plt.plot(quantities, prices_demand, label='Demand')
plt.plot(quantities, prices_supply, label='Supply')

# Add labels and legend
plt.xlabel('Quantity')
plt.ylabel('Price')
plt.legend()
plt.title('Demand and Supply in a Market')

# Show the plot
plt.grid(True)
plt.show()
