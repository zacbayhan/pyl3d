#!/usr/bin/python
import smbus

bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)


DEVICE_ADDRESS = 0x69      #7 bit address (will be left shifted to add the read write bit)
DEVICE_REG_MODE1 = 0x00
DEVICE_REG_LEDOUT0 = 0x1d

REG_WHO_AM_I   = 0x0F

REG_CTRL_REG1   = 0x20
REG_CTRL_REG2   = 0x21
REG_CTRL_REG3   = 0x22
REG_CTRL_REG4   = 0x23
REG_CTRL_REG5   = 0x24
REG_REFERENCE   = 0x25
REG_OUT_TEMP    = 0x26
REG_STATUS_REG  = 0x27

REG_OUT_X_L     = 0x28
REG_OUT_X_H     = 0x29
REG_OUT_Y_L     = 0x2A
REG_OUT_Y_H     = 0x2B
REG_OUT_Z_L     = 0x2C
REG_OUT_Z_H     = 0x2D

REG_FIFO_CTRL_REG = 0x2E
REG_FIFO_SRC_REG  = 0x2F

REG_INT1_CFG      = 0x30
REG_INT1_SRC      = 0x31
REG_INT1_THS_XH   = 0x32
REG_INT1_THS_XL   = 0x33
REG_INT1_THS_YH   = 0x34
REG_INT1_THS_YL   = 0x35
REG_INT1_THS_ZH   = 0x36
REG_INT1_THS_ZL   = 0x37
REG_INT1_DURATION = 0x38


def who_am_i():
    # returns bool, based on value of who_am_i register
    return bus.read_byte_data(DEVICE_ADDRESS, REG_WHO_AM_I)

def get_temp():
    temp = bus.read_byte_data(DEVICE_ADDRESS, 0x26)
    print 'temp: ', temp


def calibrate():
    if(who_am_i() != True):
        print 'ERROR: unmatched register'

def get_scale():
    return ((bus.read_byte_data(DEVICE_ADDRESS, REG_CTRL_REG4) >> 0x04) & 0x03)

def main():
    print 'who_am_i: ', bin(who_am_i())
    print 'Temp: ', get_temp()
    print 'pre  shifted: ' , bus.read_byte_data(DEVICE_ADDRESS, REG_CTRL_REG4)
    print 'post shifted: ' , get_scale()

    bus.close()


main()
