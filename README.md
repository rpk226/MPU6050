# MPU6050
# MPU6050 Interface with STM32F446RE Nucleo and Python Visualization

## 📘 Overview
This project demonstrates how to interface the MPU6050 IMU sensor with the STM32F446RE Nucleo board using I2C, transmit the data over UART, and visualize it in real time using Python on Ubuntu.

---

## 🧩 Hardware Used
- STM32F446RE Nucleo Board
- MPU6050 (Accelerometer + Gyroscope)

---

## 🔌 Hardware Configuration

### I2C Configuration
- Peripheral: **I2C1**
- Pins:
  - **PB8 → SCL (Clock)**
  - **PB9 → SDA (Data)**

### Wiring

| MPU6050 Pin | STM32 Nucleo Pin |
|------------|------------------|
| VIN        | 3.3V / 5V        |
| GND        | GND              |
| SDA        | PB9 (D14)        |
| SCL        | PB8 (D15)        |

---

## ⚙️ STM32 Configuration

Configured using STM32CubeIDE:

- I2C1 enabled
- Mode: I2C
- Clock speed: 100 kHz
- UART (USART2) enabled for serial communication
- Baud rate: 115200

---

## 📡 Data Transmission

The STM32 sends sensor data over UART in CSV format:

Ax,Ay,Az,Temp,Gx,Gy,Gz


Example:

0.01,-0.98,1.00,36.5,0.02,-0.01,0.03


---

## 🐧 Reading Data in Ubuntu

When connected via USB, the board appears as:


/dev/ttyACM0


## 🔍 Check Available Ports

List available serial ports:

```bash
ls /dev/ttyACM*  ```


🖥️ Viewing Raw Data in Terminal

You can view the raw UART data using screen:

```bash 
screen /dev/ttyACM0 115200
``` 

Install Dependencies
``` bash 
pip install pyserial matplotlib
```