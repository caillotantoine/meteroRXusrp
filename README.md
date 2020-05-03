# meteroRXusrp
Receiver for LRPT signal from Meteor M2 weather satellites based on [Otti's work](https://github.com/otti-soft/meteor-m2-lrpt) for airspy. This work is based on [GNU Radio](https://github.com/gnuradio/gnuradio) and tested with the [USRP B200 mini-i](https://www.ettus.com/all-products/usrp-b200mini-i/) on MacOS Catalina. However, I expect it to work on Linux as well. 

# Before use
Change the path of the directory where the raw files should be stored in the block _path_to_save_dir_.

Be careful, MacOS Catalania doesn't allow wrinting in Document, Desktop, Music, Video, etc.. without a valid authorization (which isn't valid by default). 

# What to do with .s files
I advise you to use the [artlav's meteor_decoder](https://github.com/artlav/meteor_decoder)
```bash
medet inputFile outputFile [options]
```
As Artlav advises : 
```bash
medet inputFile outputFile -r 65 -g 65 -b 64
```
_More interesting informations and tips on artlav's github page_

You may also use the classic LRPTofflineDecoder through WINE.

# RTL-SDR 
*[UPCOMING]* You may disable the USRP source block and enable the RTL-SDR one

# QT Window flickers
If your window flickers and your eyes start bleeding, you have to edit the config file (known issue [2583](https://github.com/gnuradio/gnuradio/issues/2583)).
```bash
nano ~/.gnuradio/config.conf
```
Then modify 
```txt
[qtgui]
qss = /opt/local/share/gnuradio/themes/alt.qss
style = raster
```
to
```txt
[qtgui]
#qss = /opt/local/share/gnuradio/themes/alt.qss
#style = raster
style = native
```

# Sharing
Same with [Otti's page](https://github.com/otti-soft/meteor-m2-lrpt): Feel free to modify and improve these flow graphs, but please share :-)
