# coding: utf-8

import spidev
import time

# SPI setup
spi=spidev.SpiDev()         # SPI object generation
spi.open(0,0)               # open SPI with bus:0 ,device:0
spi.bits_per_word=8        # 8 bits per word
spi.max_speed_hz=1000000    # maximum clock speed
spi.mode=0                  # SPI transmission mode

reg_dict = {0x18:1, 0x28:1,\
            0x2C:4, 0x24:4,\
            0x4C:4, 0x44:4,\
            0xEC:2, 0xE4:2,\
            0x3C:4, 0x34:4,\
            0x5C:4, 0x54:4,\
            0x6C:2, 0x64:2,\
            0x9C:4, 0x94:4,\
            0x1C:4, 0x14:4,\
            0x7C:4, 0x74:3,\
            0x8C:2, 0x84:2,\
            0xAC:2, 0xA4:2,\
            0xFC:1, 0xF4:1,\
            0xF0:1,        \
            #0xAC:2, 0xA4:2,\       
            0x0C:2         \
            }


def command(cmd):
    ad=spi.xfer2([cmd])

def reg_read(addr):
    global reg_dict
    nobyte=reg_dict[addr]
    ad=spi.xfer2([addr+[0xAA]*nobyte])
    rv=0
    for x in range(nobyte):
        rv=rv+ad[x+1]*256**(nobyte-1-x)
    return rv
    
def reg_write(addr_data):
    ad=spi.xfer2(addr_data)
        
