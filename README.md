## Indoor Positioning using UWB

**Product Specification**

Product Brief: DWM1001C


Description of Change:
Decawave module DWM1001C uses the **nRF52832**-CIAA chip. A new revision of this IC has been
released by Nordic which includes fixes for certain anomalies reported in **nRF52832** Rev 1.
For more information, refer to http://infocenter.nordicsemi.com/pdf/in_105_v1.0.pdf

RF Modules DWM1001C UWB XCVR Module (FCC comp) 

Manufacturer: Qorvo

Product link: https://www.qorvo.com/products/p/DWM1001C#documents

<!--Flash software: https://www.segger.com/products/debug-probes/j-link/technology/flash-download-->






### Task 1: Setup the DWM1001C devices using node type Anchors, Tag's and Listen the information through Listener module from external PC, measure the position and analysis the data.

![View](mobile_application.png)
![View](listener_diagram.png)


##### PART 1

a) Configure the DWM1001C devices using Mobile Application ``DRTLS_Manager_R2.apk`` <br>
b) Take **at least 6 DWM1001C devices**. Set 4 anchors, 1 tag and **1 anchors with Passive mode**.
c) Download the [Putty Software](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) according to your PC system configuration. <br>
d) Open the Putty, select the **Connection type** ``Serial`` and add the **Serial line** ``COM7`` (here UART port could be different for your PC. Go to **Device Manager > Ports**) and **Speed** ``112500 8N1`` and then click **Open**. <br>
e) You will see a Terminal. Click your **ENTER** button twice. Then write the command ``les`` and enter.


**Linux user:** <br> <br>
c) Install minicom. ``sudo apt-get install minicom``. <br>
d) Then open a New Terminal type ``minicom -D /dev/ttyACM0 -b 115200``. Here ``ACM0`` number will depend on your USB/UART port. OR you can use the script using ``python3 terminal_serial_data.py`` <br>
e) Click your **ENTER** button twice. Then write the command ``les`` and enter. <br>



Now you should see the distance of the **Tag device**. You can move it around and analysis the distance.


##### PART 2

At this stage we can see the data, now time to visualize the data and analysis data. Here is Python Algorithm to do this job.

1. First Download the full Repository and extract it in to your PC.
2. Download the [Visual Studio Code](https://code.visualstudio.com/) Software, [Python](https://www.python.org/) and [VS Code Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
2. Navigate the repository folder, you will find a file called ``3D_scatter_chart_analysis.py``. Open the file using the **Visual Studio Code** Software. Go to the Terminal option and click on a New Terminal option. Write the command  ``py -m pip install matplotlib``.
3. Now Run the code.

![View](chart.png)


##### Code Explainations

Here is the Function to extract X, Y, and Z coordinates from raw data
```
def extract_coordinates(data):
    pattern = r"C337\[(\d*\.\d+),(\d*\.\d+),(\-?\d*\.\d+)"
    coordinates = re.findall(pattern, data)
    return [(float(x), float(y), float(z)) for x, y, z in coordinates]
```


Our Raw data string for the tag that we got through listener device. You can copy paste your data here from the Putty terminal


```
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
```

Add your anchors level number and anchors data

```
anchors = {
    "DW8018": (0.00, 0.00, 0.00),
    "DW0B01": (0.42, 0.00, 0.00),
    "DW06A1": (0.42, 0.28, 0.00),
    "DW4108": (0.00, 0.28, 0.00)
}
```

It will create a 3D scatter plot with the tag's movement highlighted

```
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
```

Plot the anchors

```
for name, (x, y, z) in anchors.items():
    ax.scatter(x, y, z, color='red', label=name)
    ax.text(x, y, z, name, color='black')
```

Plot the tag positions with lines connecting them to show movement


```
tag_x, tag_y, tag_z = zip(*tag_positions)
sc = ax.scatter(tag_x, tag_y, tag_z, c=tag_z, cmap='viridis', label='DWC337', s=50)
ax.plot(tag_x, tag_y, tag_z, color='blue')
```

Adding labels and title
```
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Scatter Plot of UWB Devices with Tag Movement')
```

It will create a color bar


```
cbar = plt.colorbar(sc, ax=ax, shrink=0.5, aspect=5)
cbar.set_label('Tag Z Position')
```


**That's all for this task! Thank you.**


**Exercise: 1**

Anchor Placement: Use at least 6 anchors and 1 Tag. Attach the devices in the corner (with wall) of the room, ensuring they are spaced out. Keep the devices at a significant distance from each other.

Data Collection: Use a listener device connected to your PC. Move the Tag to different positions within the setup. Collect data during these movements.

Plotting the 3D Scatter Graph: Utilize Python algorithm to process the collected data. Plot a 3D scatter graph based on the data points.





### Task 2: RTLS system configuration and monitoring from a web-manager.


![View](gateway.png)


**1. Devices** <br>
a) Anchors: ``4`` <br>
b) Tag: ``1`` <br>
c) Bridge: ``1`` (attached with raspberry pi 3 B) <br>
d) Raspberry Pi 3 B: ``1``

**Process:** <br>

Firstly, you need to Flash the DWM1001 using [J-Flash Lite](https://www.segger.com/downloads/jlink/) and need to select latest “DWM1001_PANS_R2.1.hex” as data file and click on “Program Device”. Page refers (9) from [Gateway Quick Deployment Guide](/attachment/DWM1001%20Firmware%20User%20Guide.pdf).
<br>


Secondly, **CREATE AN RTLS NETWORK** Using the UART shell mode. Page refers (11-14) from [Gateway Quick Deployment Guide](/attachment/DWM1001%20Firmware%20User%20Guide.pdf).


Then you will have to do **Bridge node setup and configuration**. and **Setup the raspberry pi 3 model B**. Page refers (15-17) from [Gateway Quick Deployment Guide](/attachment/DWM1001%20Firmware%20User%20Guide.pdf). <br>

Now to check the connection, **Connect to the R3B from Windows through SSH connection**. Page refers (18) from [Gateway Quick Deployment Guide](/attachment/DWM1001%20Firmware%20User%20Guide.pdf). No need to modified any file inside the raspberry pi in this section. <br>


All done. You have to be in the same network that network connected with raspberry pi as well. Open your Morzila Firefox or Chrome. Visit 
```
https://ip_address_of_raspberrypi
```
For example: ``https://192.168.0.63``

![view](web_manager.png)


**That's all for this task! Thank you.**. For further implement please read the document from page 22-27 from [Gateway Quick Deployment Guide](/attachment/DWM1001%20Firmware%20User%20Guide.pdf).



### For DWM1001C device development, to update the firmware and debug the codes, you will need the following software.


#### Software need to be installed:

1. Embedded Studio: https://www.segger.com/downloads/embedded-studio/
2. J-Link Software and Documentation pack (Download the latest version): https://www.segger.com/downloads/jlink/
3. Arm GNU Toolchain (Download the latest version): https://developer.arm.com/downloads/-/gnu-rm
4. MobaXterm Home Edition (For SSH Connection and serial port): https://mobaxterm.mobatek.net/download-home-edition.html


<!--
**Step 1:** Erase the chip and install Firmware
1. Open the SEGGER folder from your pc where you selected the path. Open the JFlashLite software and configure it. Select the **Target Device** ``NRF52832_XXAA`` **Interface** ``SWD`` and **Speed** ``1000kHz``. Then **Data File** selgo to the **Factory_Firmware_Image** and select the file ``DWM1001_PANS_R2.0.hex``  from your **local folder** (Download the folder from Onedrive). **Click** the **Erase Chip** and after completing the process click on **Program Device**. All done!
-->