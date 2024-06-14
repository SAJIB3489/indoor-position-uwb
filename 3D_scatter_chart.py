import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import re


# Here is the Function to extract X, Y, and Z coordinates from raw data

def extract_coordinates(data):
    pattern = r"C337\[(\d*\.\d+),(\d*\.\d+),(\-?\d*\.\d+)"
    coordinates = re.findall(pattern, data)
    return [(float(x), float(y), float(z)) for x, y, z in coordinates]



# Our Raw data string for the tag that we got through listener device
#You can copy paste your data here from the Putty terminal


raw_data = """
[000969.170 INF] loc_data: 1
 0) C337[0.46,0.50,0.00,56,x0D]
 
[000970.170 INF] loc_data: 1
 0) C337[0.80,0.38,0.18,56,x0D]
 
[000971.170 INF] loc_data: 1
 0) C337[0.02,0.10,0.00,56,x0D]
 
[000972.170 INF] loc_data: 1
 0) C337[0.30,0.70,0.08,56,x0D]
 
[000973.170 INF] loc_data: 1
 0) C337[0.99,0.20,0.15,59,x0D]
 
 [000973.170 INF] loc_data: 1
 0) C337[0.55,0.30,0.07,59,x0D]
"""

# Extract coordinates from raw data
tag_positions = extract_coordinates(raw_data)

# Add your anchors level number and anchors data

anchors = {
    "DW8018": (0.00, 0.00, 0.00),
    "DW0B01": (0.42, 0.00, 0.00),
    "DW06A1": (0.42, 0.28, 0.00),
    "DW4108": (0.00, 0.28, 0.00)
}

# Create a 3D scatter plot with the tag's movement highlighted
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the anchors
for name, (x, y, z) in anchors.items():
    ax.scatter(x, y, z, color='red', label=name)
    ax.text(x, y, z, name, color='black')

# Plot the tag positions with lines connecting them to show movement
tag_x, tag_y, tag_z = zip(*tag_positions)
sc = ax.scatter(tag_x, tag_y, tag_z, c=tag_z, cmap='viridis', label='DWC337', s=50)
ax.plot(tag_x, tag_y, tag_z, color='blue')

# Now Adding labels and title
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Scatter Plot of UWB Devices with Tag Movement')

# It will create a color bar
cbar = plt.colorbar(sc, ax=ax, shrink=0.5, aspect=5)
cbar.set_label('Tag Z Position')

# Adding legend
ax.legend()

plt.show()
