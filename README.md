# Learning Platform for Switching Regulators


![Version 2.1](https://lh3.googleusercontent.com/mXw2e0O1Dn3ATKSt-0rPezoyeXoYsjjkwz_hUE6YXK8_qli8aZ7eyc0MIbelMhmXK4NhRsszs4dfDzUFlKky3QdYGnb7FjAEE3_e-Uz8WDJy7oJ0dezl6m6FXUo_xRJERlX-5XpMrsyX32wyKVDfA5MTR2tn5k2pCWXyUoHVZTqoZmKslX4L5VfZKfjh9H-OjmKw1kN9PrDjy_jHbO9Fr1rQ2G7N5EgFg-yqUvR9dl16PT6xJKW7FBoOOLqhIzwGbuTw3m2zcqjijmyu8Qf8Lrfm5DedqFJIVvnHmt-sHnwzYJsG3omO0gYdKWcSONqeOlObcjiL2m9TEDPe6qeiVB_8jKI6CMoJqcmXCVso6T7XEXtXLayqkl0LiICHAiDbPOu-QSOfDgTRjW7IXbJHu_y8vdR56oAaTkAz2wrDOfWzNw0dOChXK45EL5qBpT6IKl9Oxd1MhC8-W4EKGFpzN-Nepwh7qiYwk68KNA3qucZcgvnAFlr1rdKmRJzJMjX1-e54mAmmQHMjCrYoXyXMm4GvY_sdWRXFtKw_H-WAV8ZMdPTUJsE_psaZ93cOK-VPjgP0RAC-FOlMa3lIPlDNL-FeWZeLN2h4aRv5xjJFAKP4ino7imyzRSx_NHUWSau6Pim_xqnS3H4CndBPxLg1aX8eEMbXVFe46lRfmnEmKalpLvJQVDRwc4riEU8XFptBmd1gOHQGW58tXpos3WzOdWk9q1K8n2ZpMAtKQlYBkhM0jMjAwHFdmvCsynseb5w=w1250-h890-no?authuser=0)

This platform is designed with the intention of providing an interactive educational opertunity to university students with diverse technical backgrounds on switching regulators (namely buck converters). The project aims to develop the students' skills on using basic microcontroller IO features as starters and then build upon those skills to use a gate driver to implement a buck converter and monitor its output and efficiency. Along the Buck converter design process, the students get to use the the on board's peripherals to understand the different properties of buck converters and how they could be optimized. 

## Project's History
The project was introduced as a bachelor thesis of **Lukas Wiegert**. (*version 1.0*). Continued and further developed by **Adrian Keil** (*Versions: 1.0 ,1.1 ,1.2*) and finalized by **Youssef Tarkhan** (*versions: 2.1, 2.2*). The boards are used by the Technical University of Munich to teach the students and assess the quality and functionality of these boards and provide an open source curriculum.
# Board Breakdown

![Block Diagram](https://lh3.googleusercontent.com/YcGAyyHS-4aoX9yGmsiNlIIkMnGP5UTXa0rZAErdtPAgV_91_FOJs0IKJrnPAjHqbJo5bOiqF_GSscV1sULOKV991ZT8mbX3_FvjuUV_4GhbcZs1wfuCCiG0n6VV0fdYLG_zZznKOcvpl409V6kfVaJLvUymsPXuQAIIeA9UXrrCvi5B6BGhYMnbzn4UCUFgwp1gXBMzgJUGYYJ2-VgNjphOvSgSBHuygkYGh5gEBgyjziOkeor8mO57H0dwDDTpAMET-RTzhdwcMDeMVJMOqU7JcFYQdKIvRJqd4piBksiZ2KeiNGIKb7Zs4QyfNAO8brn7ItFXhn3dSoF7nif3gLL4uBvRbLr2rNCtdcnu3h4Q_zKE30SmgJ81bwTDPzAXrQq7pu6PdMKDt9yIvBxrD4cGMxGibhIs5PCVc-BTvvPnTi0AmV1Wxzi95GsroMPuXAvQcsaFgbET9TfDxxn74JL7MaoG1WdIHq3EI1wdDWZVdzTGbHisIBOM8jrwL9aq6NcgsJspy1vrykpGAqRGaD2uO0zmt1ClQTHeaeq8iTtA-jsk-0oMXXAZ-EWqm98AFRupSX9_aiGSupPMayUcqGRaSoq-WWEkCMXRdMXPK5lUlG4xdb9lSzNcHTIoHcxkpiAPKJwKz4JvuGnl_FztBT4uILtTwCPMaDLWjOzmTdtvepMHpr5Rvx-Ctb7-hYlh0Q2Eq4hlAmjN7Ox7Xh-5rC9Jhn-pQEquOacZhTjBihOOLedKBxO8uuSnB3oj5vM=w1531-h744-no?authuser=0)
Brief summary: As you can see from the block diagram, the board needs an input connection. (Bannana ports are provided at the bottom side of the board in version 2.2).  After the board makes sure that the polarity and the voltage are in check, the power is fed into the board's internal powersupply compartment. If the voltage level is below 10V then you will observe the undervoltage LED glowing in RED. The powerline feeding the whole board interfaces two optional possibilities for input current measurement. Power is then fed onto the power stage which consists of the components needed for the buck switching with a **VOut** output (*In older versions of the board there used to be additional banana ports for the **Vout** terminal and an additional ground banana port*.) Power is additionally fed into the arduino peripherals for basic microcontroller usage (LEDS, Switches, Buttons and Potentiometers). 

*Note that for every measurable quantity such as the input current for instance, there is a testpoint that could be attached onto an oscilloscope in order to have an easier experience when trying the measure this quantity*

# Microcontroller Pinouts
The labelling of the XMC1300 Bootkit pins is placed on the bottom layer's silk screen.

## XMC 1300 Bootkit Pins
| **Pin** 	| **Net**              	| **Type** 	|
|---------	|----------------------	|----------	|
| A0      	| In_Curr_ADC          	| Input    	|
| A1      	| Inductor_Current_ADC 	| Input    	|
| A2      	| UserPot1             	| Input    	|
| A3      	| Vin_Meas             	| Input    	|
| A4      	| Vout_Meas            	| Input    	|
| A5      	| NTC_ext              	| Input    	|
| D0      	| NC                   	| NC       	|
| D1      	| NC                   	| NC       	|
| D2      	| UserBtn1             	| Input    	|
| D3      	| Cntrl1               	| Output   	|
| D4      	| Cntrl2               	| Output   	|
| D5      	| Cntrl3               	| Output   	|
| D6      	| Buck_Cntrl_Arduino   	| Output   	|
| D7      	| UserBtn2             	| Input    	|
| D8      	| Shutdown             	| Input    	|
| D9      	| User_LED1            	| Output   	|
| D10     	| User_LED2            	| Output   	|
| D11     	| User_LED3            	| Output   	|
| D12     	| UserSw               	| Input    	|
| D13     	| User_LED4            	| Output   	|

## XMC2GO Pins
| **Arduino Pin** 	| **XMC2GO Pin** 	| **Net**              	| **Type** 	|
|-----------------	|----------------	|----------------------	|----------	|
| 0               	| P0.6           	| NC                   	| NC       	|
| 1               	| P0.7           	| NC                   	| NC       	|
| 2               	| P0.8           	| NC                   	| NC       	|
| 3               	| P0.9           	| NC                   	| NC       	|
| 4               	| P0.14          	| UserBtn2             	| Input    	|
| 5               	| P0.15          	| UserPot1             	| Input    	|
| 6               	| P2.0           	| UserPot2             	| Input    	|
| 7               	| P2.6           	| In_Curr_ADC          	| Input    	|
| 8               	| P0.5           	| Buck_Cntrl_Arduino   	| Output   	|
| 9               	| P0.0           	| UserBtn1             	| Input    	|
| 10              	| P2.11          	| Vin_Meas             	| Input    	|
| 11              	| P2.10          	| UserSw               	| Input    	|
| 12              	| P2.9           	| Vout_Meas            	| Input    	|
| 13              	| P2.7           	| Inductor_Current_ADC 	| Input    	|

# Board Peripherals
As previously mentioned, what makes the board special is all the bells and whistles it comes with. 

## Power Supply
The Optimum input Voltage for the board input is around **15V**. In case the voltage goes over 19V the board goes into a hysterisis where it only gets back in operation when the voltage level goes below ****. Feel free to check the simulation files if you want to get a deeper insight into how the hysterisis works on a circuit design level. (You will have to install the spice model files for the ATL431, [click here](https://www.youtube.com/watch?v=EwAxUvS5z-0) for a guide on how to do that)
Along with the input being fed into the board, the board additionally has 3 additional power components which are:
- **12V LDO**: 
					-  Gate driver IC
					- Input Internal Current Sense Amplifier
					- Safety Latch 
					- Safety Circuit Comparator
					- Safety LEDs
					
					
- **5V Buck**: 
					- 3V3 LDO
					- Arduino Compatable MCU 
					- Safety Circuitry Voltage Threshhold (*Under-Voltage Detection*)
- **3V3 LDO**:
					- Output Internal Current Sense Amplifier
					- ADC Compensation for MCU Input
					- Safety Comparator Circuit
					- XMC2GO
## Interactive User Utensils
The board is equipped with:
- 2 User programmable potentiometers
- 2 User programmable buttons
- 4 User programmable LEDs
- 1 User programmable Switch

##  Buck Operation
As previously mentioned, the buck operation takes place over a gate driver; what happens: is that the gate driver takes in pulse width modulated signals from the microcontroller (that could be the XMC2GO or the XMC 1100 Bootkit) or an external controller through the **PWM** pin on the external control pin header.  The users have to modify the **BUCK CNTRL** switch to adapt the circuitry to whether or not the control signal would be coming from the external control pin header or through the onboard controller pins(*XMC2GO/XMC1100 Bootkit*). The students get to change the frequency and duty cycle of the signal in order to achieve their desired output voltage. 
### External Inductor and Capacitors

### Filter Capacitor


### Error Flags
Because when dealing with students, safety is definitely a top priority ( and since the system is in the hands of "pseudo" experts, the board is equipped with an embedded safety mechanism to stop the buck operation in case of the occurance of any of the following flags:

 - **Undervoltage**
	 - If the voltage falls beneath 10V, the undervoltage LED will turn on and the gate driver will go into fault mode which will stop the buck operation.
 - **Overcurrent**
	 - If output current goes above ~3A, the over current LED will turn on and the gate driver will go into fault mode which will stop the buck operation.
 - **Overtemperature** (External)
	 - If the temperature at the external load resistor board rises above the calibrated threshhold, the external overtemperature LED will turn on and the gate driver will go into fault mode which will stop the buck operation.  
 - **Overtemperature** (Internal)
	 - If the temperature of the board rises above the calibrated threshhold, the internal overtemperature LED will turn on and the gate driver will go into fault mode which will stop the buck operation.  


### NTC Calibration
- For making sure that the temperature on board is in check, negative thermal coefficient resistors are chosen . The onboard maximum temperature could easily be calibrated by adjusting a potentiometer for temperature limitation between (50°C and 90°C)

## Current Measurement
- **Input Current Measurement** Measuring the input current is optional, you can control it through the 
-  **Output Current Measurement** will sync all your files, folders and settings automatically. This will allow you to fetch your workspace on any other device.

The main method of current measurement is the combination of a shunt resistor and a current sense amplifier. This setup is repeated in the input and output current measurement system. The operation relies on a voltage drop accross the shunt resistor proportional to the current flowing through it. This voltage drop is amplified by the current sense amplifier into a new voltage value. This voltage value is read by the micro-controller's ADC and it's used to subsequently calculate the value of the current.

# Whats new in version 2.1?

- All jumpers are replaced with switches
- Additional Programmable Potentiometer
- Button Pin Bug fix
- XMC2Go Support
- External Peripheral Header
- External Input Current Sensor Support
- Input Current Measurement Disabling switch
- On board overheating protection with heat limit calibration
- More Testpoints 

## Possible shield combinations 
With the addition of the XMC2GO support, it has now become possible to use 
### Current Sense Shield2GO
![Current Sense S2Go](https://lh3.googleusercontent.com/u-2VhvUzSasAnN3VMJLjT_i6g_vxOhuAZEKvBkC19CTkAa9LT_9QvvrCKZU-fY3A2CV5dDFmKlfoDQSYuR_kbJNlabG51AxxkkoK8sQFl9xDTXuel90S6lfZUhYkoDdCySHUKoAEiwP4bHpRps46wT0KBFmwamhO_hpi1SIfGQINMbmdqoURgEJgG9Z0agBP2Jh_C_odMtRpI5mZQgyGJabZKxXKAhWSF4R7U8MzVv9bZuu2Ej_8UMb23Ao0IY5oTIxgJUPi3ZMgPJ9zPTNRahP9J1ikQfywHjtFcrxcqJN21Y5LhQ-_j76Q_YWz_z3wf5Tof8z7LDLcAKsNQxBwkiPz4tMrMoYmExHWaXEVJQ_3p6UsPaHTwGTpYRprqwlEXBCj2YLa95S5HBqlL61y13ABPX1AnT1LOVM_L13p3HXzRWy_jtnTMfvb8NY6Zzw-3HnSJBrinHHndZMj6L5bsQZN4fJoLasN6Cf9hpXFuzUZ1Bg6ThkP6daYJlpjaEfFKn0N4R33HLvx1cdGZYsR7djbH3aYa7P38MJK6Aq79f-yPphqb_LsOcXu-B8gDW0Kq29l2J37eqGjbZgZsDWWKUSa63dNXj2j_q7GF2oluJIIkac7TXBzoAYFeo35N0rNe0hsb2vWtlRRv7O3nTgCDWB-RoFEZVKzxViLMRbSkQaOnSkMogHHtLkZ5_A_q_UAluyUeypTS5XZyDHZo4bNd3qyaNU6nQoEnbiUIeuE1aQL-JfgejRI85Bv3j8YtEA=w492-h186-no?authuser=0)
-- This shield can be used as an alternative to the shunt resistor + current sense amplifier combination to measure the input current. To use it all you'll have to do is to  stack it on top of the XMC2GO. This could also be used to introduce students to different communication protocols, since this shield supports SPI communication.

# Simulation Files
To provide a rich experience to students, the simulation files for most of the building blocks of the learning platform are provided. These simulations are accessable of LTSPICE, which is an open source freeware, that is very popular in the industry.  

You can find these simulations under the Directory /Simulations.

# FAQ
- Can this board be fully hand assembled?
	- Yes, infact for the last summer semester, due to some delays we had to assemble the boards to University using solder paste and a hot gun. However starting from version 2.1, all  0603 SMD capacitors and resistors have been replaced by 1206 ones; so it should be feasible to even solder the components using with a soldering iron. The only difficulty would be soldering the ATL431, which is responsible for the input voltage hysterisis so even if you were not capable of soldering it, know that you'll have to take care of the input voltage because the board won't shut down if the voltage exceeds the limit.
	
- What type of background experience does it require to participate in this course?
	- Absolutely none, within the scope of this course: students get to have first contact with microcontrollers and even blink LEDs and then get to deal with pulse width modulation. Students also have the possibility of dealing with different communication protocols through the addition of XMC2Go shields.

- How much does it cost to currently produce one board?
	- Board production costs around 70$ as of now, however this price is heavily impacted by the current scarcity of semiconductor products on the market.

- What was the last board version tested by University?
	- The last version tested by University was version 2.0. This version ran smoothly however due to input ripples, the input current measurement shunt resistor would get destroyed. This lead to the introduction of disabling and externally measuring the input current measurement in version 2.1.
																																																



# Future Strategy 
This project is not yet fully disclosed, and it will remain under  development so feel free to reach out to youssef.tarkhan@infineon.com for any inquiries or suggestions anytime. 