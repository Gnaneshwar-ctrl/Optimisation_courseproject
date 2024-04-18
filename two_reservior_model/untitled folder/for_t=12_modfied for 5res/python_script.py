import matplotlib.pyplot as plt
import pandas as pd

# Your data
time_periods = ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10', 't11', 't12']
## Reser 1
storage = [419.35, 0.00, 0.00, 0.00, 40.35, 685.35, 1000.00, 1000.00, 1000.00, 969.75, 1000.00, 1000.00]
input_flow = [128.00, 125.00, 234.00, 360.00, 541.00, 645.00, 807.00, 512.00, 267.00, 210.00, 181.00, 128.00]
release_flow = [708.65, 544.35, 234.00, 360.00, 500.65, 0.00, 492.35, 512.00, 267.00,240.25, 150.75, 128.00]
demand = [0.00, 0.00, 0.00, 64.50, 109.80, 184.40, 243.70, 200.90, 99.50, 0.00, 0.00, 0.00]
storage_new = [0.00, 0.00, 52.00, 0.00, 51.00, 195.00, 300.00, 300.00, 300.00, 216.00, 261.00, 300.00]
input_flow_new = [39.00, 39.00, 52.00, 121.00, 168.00, 144.00, 105.00, 78.00, 49.00, 44.00, 45.00, 39.00]
release_flow_new = [339.00, 39.00, 0.00, 173.00, 117.00, 0.00, 0.00, 78.00, 49.00, 128.00, 0.00, 0.00]
demand_new = [0.00, 0.00, 0.00, 13.50, 15.00, 22.10, 26.00, 24.90, 13.00, 0.00, 0.00, 0.00]
## Reser 3
storage_new_1 = [1000.00, 544.35, 778.35, 499.35, 1000.00, 1000.00, 1000.00, 1000.00, 759.75, 1000.00, 1000.00, 1000.00]
input_flow_new_1 = [708.65, 544.35, 234.00, 360.00, 500.65, 0.00, 492.35, 512.00, 267.00, 240.25, 150.75, 128.00]
release_flow_new_1 =[208.65, 1000.00, 0.00, 639.00, 0.00, 0.00, 492.35, 512.00, 507.25, 0.00, 150.75, 128.00]
## Reser 4
storage_new_2 = [88.00, 127.00, 127.00, 300.00, 300.00, 300.00, 300.00, 300.00, 300.00, 300.00, 300.00, 300.00]
input_flow_new_2 = [339.00, 39.00, 0.00, 173.00, 117.00, 0.00, 0.00, 78.00, 49.00, 128.00, 0.00, 0.00]
release_flow_new_2 = [401.00, 0.00, 0.00, 0.00, 117.00, 0.00, 0.00, 78.00, 49.00, 128.00, 0.00, 0.00]
## Reser 5 
storage_new_3 = [0.00, 500.00, 0.00, 500.00, 454.60, 251.35, 500.00, 500.00, 500.00, 500.00, 500.00, 500.00]
input_flow_new_3 = [609.65, 1000.00, 0.00, 639.00, 117.00, 0.00, 492.35, 590.00, 556.25, 128.00, 150.75, 128.00]
release_flow_new_3 = [709.65, 500.00, 500.00, 139.00, 162.40, 203.25, 243.70, 590.00, 556.25, 128.00, 150.75, 128.00]


# Create a DataFrame
data = pd.DataFrame({'Time Periods': time_periods,
                     'Storage_Reservoir1': storage,
                     'Input Flow_Reservoir1': input_flow,
                     'Release Flow_Reservoir1': release_flow,
                     'Demand_Group1': demand,
                     'Storage_Reservoir2': storage_new,
                     'Input Flow_Reservoir2': input_flow_new,
                     'Release Flow_Reservoir2': release_flow_new,
                     'Demand_Group2': demand_new,
                     'Storage_Reservoir3': storage_new_1,
                     'Input Flow_Reservoir3': input_flow_new_1,
                     'Release Flow_Reservoir3': release_flow_new_1,
                     'Storage_Reservoir4': storage_new_2,
                     'Input Flow_Reservoir4': input_flow_new_2,
                     'Release Flow_Reservoir4': release_flow_new_2,
                     'Storage_Reservoir5': storage_new_3,
                     'Input Flow_Reservoir5': input_flow_new_3,
                     'Release Flow_Reservoir5': release_flow_new_3})

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
#r3
plt.plot(data['Time Periods'], data['Input Flow_Reservoir3'], marker='o', label='Input Flow_Reservoir3')
plt.plot(data['Time Periods'], data['Release Flow_Reservoir3'], marker='o', label='Release Flow_Reservoir3')
plt.plot(data['Time Periods'], data['Storage_Reservoir3'], marker='o', label='Storage Reservoir3')
#r4
plt.plot(data['Time Periods'], data['Input Flow_Reservoir4'], marker='o', label='Input Flow_Reservoir4')
plt.plot(data['Time Periods'], data['Release Flow_Reservoir4'], marker='o', label='Release Flow_Reservoir4')
plt.plot(data['Time Periods'], data['Storage_Reservoir4'], marker='o', label='Storage Reservoir4')
#r5
plt.plot(data['Time Periods'], data['Input Flow_Reservoir5'], marker='o', label='Input Flow_Reservoir5')
plt.plot(data['Time Periods'], data['Release Flow_Reservoir5'], marker='o', label='Release Flow_Reservoir5')
plt.plot(data['Time Periods'], data['Storage_Reservoir5'], marker='o', label='Storage Reservoir5')

plt.title('Flows Over Time Periods')
plt.xlabel('Time Periods')
plt.ylabel('Volume')
plt.xticks(rotation=45)
# plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()

