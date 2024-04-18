import matplotlib.pyplot as plt
import pandas as pd

# Your data
time_periods = ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10', 't11', 't12']
storage = [250.00, 0.00, 0.00, 0.00, 0.00, 436.70, 1000.00, 1000.00, 1000.00, 1000.00, 872.00, 1000.00]
input_flow = [128.00, 125.00, 234.00, 360.00, 541.00, 645.00, 807.00, 512.00, 267.00, 210.00, 181.00, 128.00]
release_flow = [878.00, 375.00, 234.00, 360.00, 541.00, 208.30, 243.70, 512.00, 267.00, 210.00, 309.00, 0.00]
demand = [0.00, 0.00, 0.00, 64.50, 109.80, 184.40, 243.70, 200.90, 99.50, 0.00, 0.00, 0.00]
storage_new = [300.00, 214.00, 0.00, 0.00, 51.00, 195.00, 300.00, 277.10, 300.00, 300.00, 300.00, 300.00]
input_flow_new = [39.00, 39.00, 52.00, 121.00, 168.00, 144.00, 105.00, 78.00, 49.00, 44.00, 45.00, 39.00]
release_flow_new = [39.00, 125.00, 266.00, 121.00, 117.00, 0.00, 0.00, 100.00, 26.10, 44.00, 45.00, 39.00]
demand_new = [0.00, 0.00, 0.00, 13.50, 15.00, 22.10, 26.00, 24.90, 13.00, 0.00, 0.00, 0.00]

# Create a DataFrame
data = pd.DataFrame({'Time Periods': time_periods,
                     'Storage_Reservoir1': storage,
                     'Input Flow_Reservoir1': input_flow,
                     'Release Flow_Reservoir1': release_flow,
                     'Demand_Group1': demand,
                     'Storage_Reservoir2': storage_new,
                     'Input Flow_Reservoir2': input_flow_new,
                     'Release Flow_Reservoir2': release_flow_new,
                     'Demand_Group2': demand_new})

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(data['Time Periods'], data['Input Flow_Reservoir1'], marker='o', label='Input Flow_Reservoir1')
plt.plot(data['Time Periods'], data['Release Flow_Reservoir1'], marker='o', label='Release Flow_Reservoir1')
plt.plot(data['Time Periods'], data['Demand_Group1'], marker='o', label='Demand Group1')
plt.plot(data['Time Periods'], data['Storage_Reservoir1'], marker='o', label='Storage Reservoir1')
plt.plot(data['Time Periods'], data['Input Flow_Reservoir2'], marker='o', label='Input Flow_Reservoir2')
plt.plot(data['Time Periods'], data['Release Flow_Reservoir2'], marker='o', label='Release Flow_Reservoir2')
plt.plot(data['Time Periods'], data['Demand_Group2'], marker='o', label='Demand Group2')
plt.plot(data['Time Periods'], data['Storage_Reservoir2'], marker='o', label='Storage Reservoir2')

plt.title('Flows Over Time Periods')
plt.xlabel('Time Periods')
plt.ylabel('Volume')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()

