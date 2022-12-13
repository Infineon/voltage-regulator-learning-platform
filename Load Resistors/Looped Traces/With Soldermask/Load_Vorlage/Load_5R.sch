EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector_Generic:Conn_02x05_Odd_Even J1
U 1 1 61069FAE
P 4400 3900
F 0 "J1" H 4450 4317 50  0000 C CNN
F 1 "Conn_02x05_Odd_Even" H 4450 4226 50  0000 C CNN
F 2 "Connector_IDC:IDC-Header_2x05_P2.54mm_Vertical" H 4400 3900 50  0001 C CNN
F 3 "~" H 4400 3900 50  0001 C CNN
	1    4400 3900
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR01
U 1 1 6106BBD0
P 4800 4150
F 0 "#PWR01" H 4800 3900 50  0001 C CNN
F 1 "GND" H 4805 3977 50  0000 C CNN
F 2 "" H 4800 4150 50  0001 C CNN
F 3 "" H 4800 4150 50  0001 C CNN
	1    4800 4150
	1    0    0    -1  
$EndComp
Wire Wire Line
	4700 4100 4800 4100
Wire Wire Line
	4800 4100 4800 4150
Wire Wire Line
	4200 4100 3750 4100
Text Label 3750 4100 0    50   ~ 0
NTC_ext
$Comp
L Mechanical:MountingHole H1
U 1 1 6106C733
P 3650 2200
F 0 "H1" H 3750 2246 50  0000 L CNN
F 1 "MountingHole" H 3750 2155 50  0000 L CNN
F 2 "MountingHole:MountingHole_3.2mm_M3" H 3650 2200 50  0001 C CNN
F 3 "~" H 3650 2200 50  0001 C CNN
	1    3650 2200
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H2
U 1 1 6106DA4A
P 4600 2200
F 0 "H2" H 4700 2246 50  0000 L CNN
F 1 "MountingHole" H 4700 2155 50  0000 L CNN
F 2 "MountingHole:MountingHole_3.2mm_M3" H 4600 2200 50  0001 C CNN
F 3 "~" H 4600 2200 50  0001 C CNN
	1    4600 2200
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H3
U 1 1 6106DC5F
P 5400 2200
F 0 "H3" H 5500 2246 50  0000 L CNN
F 1 "MountingHole" H 5500 2155 50  0000 L CNN
F 2 "MountingHole:MountingHole_3.2mm_M3" H 5400 2200 50  0001 C CNN
F 3 "~" H 5400 2200 50  0001 C CNN
	1    5400 2200
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H4
U 1 1 6106DE57
P 6250 2200
F 0 "H4" H 6350 2246 50  0000 L CNN
F 1 "MountingHole" H 6350 2155 50  0000 L CNN
F 2 "MountingHole:MountingHole_3.2mm_M3" H 6250 2200 50  0001 C CNN
F 3 "~" H 6250 2200 50  0001 C CNN
	1    6250 2200
	1    0    0    -1  
$EndComp
Wire Wire Line
	4200 3700 4200 3800
Connection ~ 4200 3800
Wire Wire Line
	4200 3800 4200 3900
Connection ~ 4200 3900
Wire Wire Line
	4200 3900 4200 4000
Wire Wire Line
	4700 4000 4700 3900
Connection ~ 4700 3800
Wire Wire Line
	4700 3800 4700 3700
Connection ~ 4700 3900
Wire Wire Line
	4700 3900 4700 3800
Wire Wire Line
	4200 3700 4200 3600
Wire Wire Line
	4200 3600 4700 3600
Wire Wire Line
	4700 3600 4700 3700
Connection ~ 4200 3700
Connection ~ 4700 3700
Wire Wire Line
	3750 3800 4200 3800
Text Label 3750 3800 0    50   ~ 0
Loads
$Comp
L Device:Thermistor_NTC TH1
U 1 1 610A81AB
P 3750 4450
F 0 "TH1" H 3597 4404 50  0000 R CNN
F 1 "Thermistor_NTC" H 3597 4495 50  0000 R CNN
F 2 "Resistor_SMD:R_0603_1608Metric_Pad0.98x0.95mm_HandSolder" H 3750 4500 50  0001 C CNN
F 3 "~" H 3750 4500 50  0001 C CNN
	1    3750 4450
	-1   0    0    1   
$EndComp
Wire Wire Line
	3750 4300 3750 4100
$Comp
L power:GND #PWR0101
U 1 1 610AC81D
P 3750 4650
F 0 "#PWR0101" H 3750 4400 50  0001 C CNN
F 1 "GND" H 3755 4477 50  0000 C CNN
F 2 "" H 3750 4650 50  0001 C CNN
F 3 "" H 3750 4650 50  0001 C CNN
	1    3750 4650
	1    0    0    -1  
$EndComp
Wire Wire Line
	3750 4650 3750 4600
$EndSCHEMATC
