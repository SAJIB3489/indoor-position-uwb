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


## Task 1: Setup the DWM1001C devices using node type Anchors, Tag's and Listen the information through Listener module from external PC, measure the distance and analysis the data.

a)  Configure the DWM1001C devices using Mobile Application ``DRTLS_Manager_R2.apk``
















#### Software need to be installed:

1. Embedded Studio: https://www.segger.com/downloads/embedded-studio/
2. J-Link Software and Documentation pack (Download the latest version): https://www.segger.com/downloads/jlink/
3. Arm GNU Toolchain (Download the latest version): https://developer.arm.com/downloads/-/gnu-rm
4. MobaXterm Home Edition ( **Download the Portable edition** For SSH Connection and serial port): https://mobaxterm.mobatek.net/download-home-edition.html


**Step 1:** Erase the chip and install Firmware
1. Open the SEGGER folder from your pc where you selected the path. Open the JFlashLite software and configure it. Select the **Target Device** ``NRF52832_XXAA`` **Interface** ``SWD`` and **Speed** ``1000kHz``. Then **Data File** selgo to the **Factory_Firmware_Image** and select the file ``DWM1001_PANS_R2.0.hex``  from your **local folder** (Download the folder from Onedrive). **Click** the **Erase Chip** and after completing the process click on **Program Device**. All done.