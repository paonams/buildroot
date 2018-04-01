//[*]--------------------------------------------------------------------------------------------------[*]
//
//
// 
//  I2C INA231(Sensor) driver
//  2013.07.17
// 
//
//[*]--------------------------------------------------------------------------------------------------[*]
#ifndef _INA231_MISC_H_
#define _INA231_MISC_H_

//[*]--------------------------------------------------------------------------------------------------[*]
struct ina231_iocreg	{
    unsigned char   name[20];
    unsigned int    enable;
	unsigned int	cur_uV;
	unsigned int	cur_uA;
	unsigned int	cur_uW;
} 	__attribute__ ((packed));

#define INA231_IOCGREG		_IOR('i', 1, struct ina231_iocreg *)
#define INA231_IOCSSTATUS	_IOW('i', 2, struct ina231_iocreg *)
#define INA231_IOCGSTATUS   _IOR('i', 3, struct ina231_iocreg *)

//[*]--------------------------------------------------------------------------------------------------[*]
extern  void 	ina231_misc_remove	(struct device *dev);
extern  int		ina231_misc_probe	(struct ina231_sensor *sensor);

//[*]--------------------------------------------------------------------------------------------------[*]
#endif  // _INA231_MISC_H_
//[*]--------------------------------------------------------------------------------------------------[*]
//[*]--------------------------------------------------------------------------------------------------[*]
