#import PIN and I2C from machine library 
from machine import Pin, I2C

#Define I2C bus 
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))

#Device address on the I2C bus
MPU6050_ADDR = 0x68

#PWR_MGMT_1 memory address
MPU6050_PWR_MGMT_1 = 0x6B

#Accelerometer and Gyroscope's high and low register for each axis
MPU6050_ACCEL_XOUT_H = 0x3B
MPU6050_ACCEL_XOUT_L = 0x3C
MPU6050_ACCEL_YOUT_H = 0x3D
MPU6050_ACCEL_YOUT_L = 0x3E
MPU6050_ACCEL_ZOUT_H = 0x3F
MPU6050_ACCEL_ZOUT_L = 0x40
MPU6050_GYRO_XOUT_H = 0x43
MPU6050_GYRO_XOUT_L = 0x44
MPU6050_GYRO_YOUT_H = 0x45
MPU6050_GYRO_YOUT_L = 0x46
MPU6050_GYRO_ZOUT_H = 0x47
MPU6050_GYRO_ZOUT_L = 0x48

#Accelerometer's LSB/g (least significant bits per gravitational force) sensitivity
MPU6050_LSBG = 16384.0

#Gyroscope's LSB/g sensitivity
MPU6050_LSBDS = 131.0 


#Set all bits in the PWR_MGMT_1 register to 0
def mpu6050_init(i2c):
    i2c.writeto_mem(MPU6050_ADDR, MPU6050_PWR_MGMT_1, bytes([0]))


def combine_register_values(h, l):
    if not h[0] & 0x80:
        return h[0] << 8 | l[0]
    return -((h[0] ^ 255) << 8) |  (l[0] ^ 255) + 1


#Get Accelerometer values
def mpu6050_get_accel(i2c):
    accel_x_h = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_XOUT_H, 1)
    accel_x_l = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_XOUT_L, 1)
    accel_y_h = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_YOUT_H, 1)
    accel_y_l = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_YOUT_L, 1)
    accel_z_h = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_ZOUT_H, 1)
    accel_z_l = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_ACCEL_ZOUT_L, 1)
    
    return [combine_register_values(accel_x_h, accel_x_l) / MPU6050_LSBG,
            combine_register_values(accel_y_h, accel_y_l) / MPU6050_LSBG,
            combine_register_values(accel_z_h, accel_z_l) / MPU6050_LSBG]


#Get Gyroscope values
def mpu6050_get_gyro(i2c):
    gyro_x_h = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_GYRO_XOUT_H, 1)
    gyro_x_l = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_GYRO_XOUT_L, 1)
    gyro_y_h = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_GYRO_YOUT_H, 1)
    gyro_y_l = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_GYRO_YOUT_L, 1)
    gyro_z_h = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_GYRO_ZOUT_H, 1)
    gyro_z_l = i2c.readfrom_mem(MPU6050_ADDR, MPU6050_GYRO_ZOUT_L, 1)
    
    return [combine_register_values(gyro_x_h, gyro_x_l) / MPU6050_LSBDS,
            combine_register_values(gyro_y_h, gyro_y_l) / MPU6050_LSBDS,
            combine_register_values(gyro_z_h, gyro_z_l) / MPU6050_LSBDS]


if __name__ == "__main__":
    i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
    mpu6050_init(i2c)
    
    while True:
        print("Accelerometer:\t", mpu6050_get_accel(i2c), "g") #Print Accelerometer values (X,Y,Z) 
        #print("Gyroscope:\t", mpu6050_get_gyro(i2c), "°/s") #Print Gyroscope values (X,Y,Z)
