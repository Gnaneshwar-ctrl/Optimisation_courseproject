import matplotlib.pyplot as plt
import pandas as pd

# Your data
time_periods = ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10', 't11', 't12', 't13', 't14', 't15', 't16', 't17', 't18', 't19', 't20', 't21', 't22', 't23', 't24']
## Reser 1
storage = [419.35, 544.35, 0.00, 360.00, 901.00, 1000.00, 1000.00, 1000.00, 1000.00, 1000.00, 1000.00, 240.35, 246.35, 0.00, 234.00, 0.00, 0.00, 414.35, 1000.00, 1000.00, 1000.00, 1000.00, 1000.00, 1000.00]
input_flow = [128.00, 125.00, 234.00, 360.00, 541.00, 645.00, 807.00, 512.00, 267.00, 210.00, 181.00, 128.00, 128.00, 125.00, 234.00, 360.00, 541.00, 645.00, 807.00, 512.00, 267.00, 210.00, 181.00, 128.00]
release_flow = [708.65, 0.00, 778.35, 0.00, 0.00, 546.00, 807.00, 512.00, 267.00, 210.00, 181.00, 887.65, 122.00, 371.35, 0.00, 594.00, 541.00, 230.65, 221.35, 512.00, 267.00, 210.00, 181.00, 128.00]
demand = [0.00, 0.00, 0.00, 64.50, 109.80, 184.40, 243.70, 200.90, 99.50, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 64.50, 109.80, 184.40, 243.70, 200.90, 99.50, 0.00, 0.00, 0.00]
storage_new = [0.00, 0.00, 52.00, 0.00, 0.00, 68.00, 173.00, 251.00, 300.00, 216.00, 261.00, 300.00, 0.00, 0.00, 52.00, 0.00, 0.00, 217.35, 300.00, 300.00, 300.00, 300.00, 300.00, 300.00]
input_flow_new = [39.00, 39.00, 52.00, 121.00, 168.00, 144.00, 105.00, 78.00, 49.00, 44.00, 45.00, 39.00, 39.00, 39.00, 52.00, 121.00, 168.00, 144.00, 105.00, 78.00, 49.00, 44.00, 45.00, 39.00]
release_flow_new = [339.00, 39.00, 0.00, 173.00, 168.00, 76.00, 0.00, 0.00, 0.00, 128.00, 0.00, 0.00, 339.00, 39.00, 0.00, 173.00, 168.00, 0.00, 22.35, 78.00, 49.00, 128.00, 0.00, 0.00]
demand_new = [0.00, 0.00, 0.00, 13.50, 15.00, 22.10, 26.00, 24.90, 13.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 13.50, 15.00, 22.10, 26.00, 24.90, 13.00, 0.00, 0.00, 0.00]
## Reser 3
storage_new_1 = [961.00, 0.00, 778.35, 756.35, 390.70, 936.70, 1000.00, 899.10, 1000.00, 431.35, 112.35, 1000.00, 1000.00, 871.35, 0.00, 594.00, 365.65, 0.00, 1000.00, 1000.00, 1000.00, 1000.00, 1000.00, 1000.00]
input_flow_new_1 = [708.65, 0.00, 778.35, 0.00, 0.00, 546.00, 807.00, 512.00, 267.00, 210.00, 181.00, 887.65, 122.00, 371.35, 0.00, 594.00, 390.70, 936.70, 221.35, 512.00, 267.00, 210.00, 181.00, 128.00]
release_flow_new_1 =[247.65, 961.00, 0.00, 22.00, 365.65, 0.00, 743.70, 612.90, 166.10, 778.65, 500.00, 0.00, 339.00, 500.00, 871.35, 0.00, 365.65, 76.00, 221.35, 512.00, 267.00, 210.00, 181.00, 128.00]
## Reser 4
storage_new_2 = [0.00, 39.00, 0.00, 56.00, 0.00, 300.00, 0.00, 0.00, 0.00, 300.00, 0.00, 0.00, 378.00, 0.00, 0.00, 117.00, 0.00, 0.00, 300.00, 300.00, 300.00, 300.00, 300.00, 300.00]
input_flow_new_2 = [339.00, 39.00, 0.00, 173.00, 168.00, 76.00, 300.00, 300.00, 300.00, 128.00, 300.00, 300.00, 261.00, 300.00, 300.00, 173.00, 224.00, 300.00, 300.00, 300.00, 300.00, 300.00, 300.00, 300.00]
release_flow_new_2 = [489.00, 39.00, 0.00, 117.00, 365.65, 0.00, 743.70, 612.90, 166.10, 906.65, 500.00, 0.00, 500.00, 500.00, 871.35, 139.00, 0.00, 267.65, 230.65, 243.70, 316.00, 338.00, 181.00, 128.00]
## Reser 5 
storage_new_3 = [0.00, 500.00, 500.00, 0.00, 162.40, 162.40, 243.70, 500.00, 572.75, 500.00, 500.00, 500.00, 0.00, 500.00, 500.00, 139.00, 0.00, 500.00, 500.00, 500.00, 500.00, 500.00, 500.00, 500.00]
input_flow_new_3 = [736.65, 1000.00, 0.00, 139.00, 203.25, 203.25, 500.00, 500.00, 93.35, 500.00, 500.00, 0.00, 500.00, 0.00, 500.00, 0.00, 365.65, 500.00, 500.00, 500.00, 500.00, 500.00, 500.00, 500.00]
release_flow_new_3 = [836.65, 500.00, 500.00, 139.00, 162.40, 203.25, 243.70, 612.90, 500.00, 500.00, 500.00, 500.00, 500.00, 0.00, 500.00, 139.00, 0.00, 500.00, 500.00, 500.00, 500.00, 500.00, 500.00, 500.00]


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
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()

