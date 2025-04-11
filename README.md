## THANKS TO THE WHOLE COMMUNITY AND MAKING THESE OPTIONS TO GET RID OF OTHER DEVICES LIKE ALEXA AND KEEPING IT LOCAL AND OPEN SOURCE.
    
There are multiple options out there here is the break down I know of.
I hope all the research and testing I've done here helps save you time and money in your decision! If you plan on buying parts please kindly use my affiliate links.
<a href="https://www.amazon.ca/shop/idjmic/list/1O8CLD8X3UTK1?ref_=cm_sw_r_cp_ud_aipsflist_0R4S3R71DK1PWKB1JN01" target="_blank">Affiliate Amazon Shop for Home Assistant</a>

<iframe width="560" height="315" src="https://www.youtube.com/embed/BvSzkr2tH_A?si=mibevWw74XSVQw8U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Home Assistant Voice Preview Edition
<a href="https://idjmic.com/images/satellite/HA-Voice-PE.jpg" target="_blank">
<img src="https://idjmic.com/images/satellite/HA-Voice-PE.jpg" alt="HA Voice PE" style="max-width: 100%; height: auto;"/>
</a>

## RaspberryPi Wyoming Satellite
<a href="https://idjmic.com/images/satellite/RaspberryPi_Wyoming.jpg" target="_blank">
<img src="https://idjmic.com/images/satellite/RaspberryPi_Wyoming.jpg" alt="RaspberryPi Wyoming" style="max-width: 100%; height: auto;"/>
</a>

## YouTube Video showing RaspberryPi Wyoming Satellite full SD image ready to go!
<a href="https://youtu.be/CVquCe3s2Xo?si=iwHBeBxwTvweq0lh" target="_blank">
<img src="https://img.youtube.com/vi/CVquCe3s2Xo/maxresdefault.jpg" alt="RaspberryPi Wyoming Example" style="max-width: 100%; height: auto;"/>
</a>

## YouTube Video showing FutureProofHomes RaspberryPi Setup Manually
<a href="https://youtu.be/eTKgc0YDCwE?si=n6bkjROwIr6y7KvT" target="_blank">
<img src="https://img.youtube.com/vi/eTKgc0YDCwE/maxresdefault.jpg" alt="RaspberryPi Wyoming Setup" style="max-width: 100%; height: auto;"/>
</a>

## SeeedStudio ReSpeaker-Lite w/ESP32-S3 Soldered On board.
<a href="https://idjmic.com/images/satellite/ReSpeaker-Lite.jpg" target="_blank">
<img src="https://idjmic.com/images/satellite/ReSpeaker-Lite.jpg" alt="ReSpeaker-Lite" style="max-width: 100%; height: auto;"/>
</a>

## Koala Satellite
<a href="https://idjmic.com/images/satellite/Koala-Satellite.jpg" target="_blank">
<img src="https://idjmic.com/images/satellite/Koala-Satellite.jpg" alt="Koala-Satellite" style="max-width: 100%; height: auto;"/>
</a>

## What is it
This repository contains example code to integrate Seeed Respeaker Lite Voice Kit (with XIAO ESP32-S3 on board) with ESPHome. I have just made it my own and added 12x RGB animation.
I'm thankful for continuous help of ESPHome team and Seeed developers, that let me put this thing together. It's using <a href="https://github.com/esphome/home-assistant-voice-pe" target="_blank">official code for Voice Preview Edition by ESPHome team, as well as firmware and guides from <a href="https://wiki.seeedstudio.com/xiao_respeaker/" target="_blank">Seeed Wiki</a> and <a href="https://github.com/respeaker/ReSpeaker_Lite/tree/master" target="_blank">their repository for Respeaker.

*Disclaimer
Use this at your own risk. Expect breaking changes.
Although Voice PE is released, parts of its code are still under development and merging to ESPHome core repository with breaking changes. I will try to update YAML and XMOS board firmware as soon as I can, but it can't be instantaneous...
If you encounter a problem, before creating a ticket here, you may go to PE and Seeed repos, linked above, and see if something changed there. I'll gladly accept pull-requests. :)

## Why?
I just wanted to play around with the code tweaking and customizing it for my own Home Assistant.

What to do with it?
Thanks to Mike aka @mikey60 and his fork to nabu_microphone, this project is using 48kHz sample rate for better music playback quality.

## INSTRUCTIONS
1. Get Respeaker Lite with ESP32 soldered to it (you may solder it yourself, pins on the back can remain dry, they're not used).
2. Solder USR to D2 and MUTE to D3 pins. ATTENTION! This step is mandatory, as without it the buttons on the satellite won't work as intended.
3. Solder 12 RGB WS2812 5050 LED to 5v, GND, and LED Signal wire to GPIO2 - D0 on SeeedStudio ESP32S3 board - OPTIONAL! If adding LED lights, one of the main reasons for this fork. I used <a href="https://amzn.to/4hPLEgw" target="_blank">these LED lights</a> and currently still working on a 3D printed case.
4. Flash ReSpeaker-Lite board with 48kHz I2S firmware of version not lower than 1.1.0 to the XMOS board (pay attention to USB port, you need the main board port, not ESP32 one). Make sure you're using 48kHz version, as 16kHz version won't work with this repo. You can use included <a href="/respeaker_lite_i2s_dfu_firmware_48k_v1.1.0.bin">firmware file</a> to be sure. You can find files and flashing instructions here: <a href="https://wiki.seeedstudio.com/reSpeaker_usb_v3/"></a>
5. Flash ESPHome firmware YAML included, place <a href="/config/common/respeaker-satellite-base.yaml">this code</a> into ESPHome common directory of Home Assistant, and edit <a href="/config/respeaker-satellite-dashboard-example.yaml">dashboard</a> to your needs to ESP32Home to flash be sure to plug into USB on ESP32 not ReSpeaker.
Add device to Home Assistant.

## DFU software auto-update
Since version 2025.2.2, the firmware includes corresponding DFU firmware for Respeaker Lite board. On the first start after update, new firmware will be installed to Respeaker automatically. You will see Respeaker LED flashing yellow while installing, and green on successful install. So now there's no need to update DFU firmware. Woohoo!
