# 文件说明：
   stm32端代码 -> stm32串口调试.zip \
   k210端代码 -> k210.py \
   openmv端代码 -> openmv.py

# stm32端
四脚I2C OLED:  \
  SCL -> B12	SDA -> B13 \
串口1： \
  TX->A9    RX->A10 \
  波特率9600 			 \
功能： \
  接收数据并显示在OLED上

# openmv端
串口3： \
  TX-> P4    RX-> P5 \
  波特率9600 			 \
功能： \
  交替发送a,b字符;

# openmv端
串口3： \
  TX-> P4    RX-> P5 \
  波特率9600 			 \
功能： \
  交替发送a,b字符;
  
# 适用场景：
    stm32与k210,openmv等通信

# 视频链接
【电赛必备:stm32与openmv串口通信】 https://www.bilibili.com/video/BV1nk4y147Hs/?share_source=copy_web&vd_source=04aa25efc9d27d8f799d6b53683bc5de \
【电赛必备:k210与stm32串口通信】 https://www.bilibili.com/video/BV15L411X78Y/?share_source=copy_web&vd_source=04aa25efc9d27d8f799d6b53683bc5de
