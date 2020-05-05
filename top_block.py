#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Meteor M2 Receiver 4 USRP (QT)
# Author: Antoine CAILLOT
# Description: Demodulator of Meteor M2 satellites
# GNU Radio version: 3.7.13.5
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from datetime import datetime
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import os.path
import sip
import sys
import time
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Meteor M2 Receiver 4 USRP (QT) ")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Meteor M2 Receiver 4 USRP (QT) ")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.symbol_rate = symbol_rate = 72000
        self.signal_samp_rate = signal_samp_rate = 140e3
        self.path_to_save_dir = path_to_save_dir = os.path.expanduser("~/Desktop")
        self.decim_factor = decim_factor = 4
        self.usrp_samp_rate = usrp_samp_rate = signal_samp_rate*decim_factor
        self.samp_per_sec = samp_per_sec = (signal_samp_rate * 1.0) / (symbol_rate * 1.0)
        self.rx_freq_old = rx_freq_old = 137.1e6
        self.rx_freq = rx_freq = 137.1e6
        self.rf_gain = rf_gain = 20
        self.record = record = False
        self.pll_alpha = pll_alpha = 0.015
        self.file_path = file_path = path_to_save_dir + "/LRPT_" + datetime.now().strftime("%d%m%Y_%H%M")+".s"
        self.clock_alpha = clock_alpha = 0.001

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_tab_widget_0 = Qt.QTabWidget()
        self.qtgui_tab_widget_0_widget_0 = Qt.QWidget()
        self.qtgui_tab_widget_0_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_0_widget_0)
        self.qtgui_tab_widget_0_grid_layout_0 = Qt.QGridLayout()
        self.qtgui_tab_widget_0_layout_0.addLayout(self.qtgui_tab_widget_0_grid_layout_0)
        self.qtgui_tab_widget_0.addTab(self.qtgui_tab_widget_0_widget_0, 'Reception')
        self.qtgui_tab_widget_0_widget_1 = Qt.QWidget()
        self.qtgui_tab_widget_0_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_0_widget_1)
        self.qtgui_tab_widget_0_grid_layout_1 = Qt.QGridLayout()
        self.qtgui_tab_widget_0_layout_1.addLayout(self.qtgui_tab_widget_0_grid_layout_1)
        self.qtgui_tab_widget_0.addTab(self.qtgui_tab_widget_0_widget_1, 'Demodulation')
        self.qtgui_tab_widget_0_widget_2 = Qt.QWidget()
        self.qtgui_tab_widget_0_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_0_widget_2)
        self.qtgui_tab_widget_0_grid_layout_2 = Qt.QGridLayout()
        self.qtgui_tab_widget_0_layout_2.addLayout(self.qtgui_tab_widget_0_grid_layout_2)
        self.qtgui_tab_widget_0.addTab(self.qtgui_tab_widget_0_widget_2, 'Decoding')
        self.top_grid_layout.addWidget(self.qtgui_tab_widget_0)
        self._rx_freq_options = (137.1e6, 137.9e6, 101.8e6, )
        self._rx_freq_labels = ('137.1 MHz', '137.9 MHz', 'Test FM', )
        self._rx_freq_tool_bar = Qt.QToolBar(self)
        self._rx_freq_tool_bar.addWidget(Qt.QLabel('RX Frequency'+": "))
        self._rx_freq_combo_box = Qt.QComboBox()
        self._rx_freq_tool_bar.addWidget(self._rx_freq_combo_box)
        for label in self._rx_freq_labels: self._rx_freq_combo_box.addItem(label)
        self._rx_freq_callback = lambda i: Qt.QMetaObject.invokeMethod(self._rx_freq_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._rx_freq_options.index(i)))
        self._rx_freq_callback(self.rx_freq)
        self._rx_freq_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_rx_freq(self._rx_freq_options[i]))
        self.qtgui_tab_widget_0_grid_layout_0.addWidget(self._rx_freq_tool_bar, 0, 2, 1, 1)
        for r in range(0, 1):
            self.qtgui_tab_widget_0_grid_layout_0.setRowStretch(r, 1)
        for c in range(2, 3):
            self.qtgui_tab_widget_0_grid_layout_0.setColumnStretch(c, 1)
        self._rf_gain_range = Range(0, 65, 5, 20, 200)
        self._rf_gain_win = RangeWidget(self._rf_gain_range, self.set_rf_gain, 'RF input gain', "counter_slider", float)
        self.qtgui_tab_widget_0_grid_layout_0.addWidget(self._rf_gain_win, 0, 0, 1, 2)
        for r in range(0, 1):
            self.qtgui_tab_widget_0_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 2):
            self.qtgui_tab_widget_0_grid_layout_0.setColumnStretch(c, 1)
        _record_check_box = Qt.QCheckBox('Raw I/Q Record')
        self._record_choices = {True: True, False: False}
        self._record_choices_inv = dict((v,k) for k,v in self._record_choices.iteritems())
        self._record_callback = lambda i: Qt.QMetaObject.invokeMethod(_record_check_box, "setChecked", Qt.Q_ARG("bool", self._record_choices_inv[i]))
        self._record_callback(self.record)
        _record_check_box.stateChanged.connect(lambda i: self.set_record(self._record_choices[bool(i)]))
        self.qtgui_tab_widget_0_grid_layout_0.addWidget(_record_check_box, 0, 3, 1, 1)
        for r in range(0, 1):
            self.qtgui_tab_widget_0_grid_layout_0.setRowStretch(r, 1)
        for c in range(3, 4):
            self.qtgui_tab_widget_0_grid_layout_0.setColumnStretch(c, 1)
        self._pll_alpha_range = Range(0.001, 0.100, 0.001, 0.015, 200)
        self._pll_alpha_win = RangeWidget(self._pll_alpha_range, self.set_pll_alpha, 'PLL alpha', "counter_slider", float)
        self.qtgui_tab_widget_0_grid_layout_2.addWidget(self._pll_alpha_win, 4, 0, 1, 1)
        for r in range(4, 5):
            self.qtgui_tab_widget_0_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_0_grid_layout_2.setColumnStretch(c, 1)
        self._clock_alpha_range = Range(0.001, 0.01, 0.001, 0.001, 200)
        self._clock_alpha_win = RangeWidget(self._clock_alpha_range, self.set_clock_alpha, 'Clock alpha', "counter_slider", float)
        self.qtgui_tab_widget_0_grid_layout_2.addWidget(self._clock_alpha_win, 3, 0, 1, 1)
        for r in range(3, 4):
            self.qtgui_tab_widget_0_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_0_grid_layout_2.setColumnStretch(c, 1)
        self.root_raised_cosine_filter_0 = filter.fir_filter_ccf(1, firdes.root_raised_cosine(
        	1, signal_samp_rate, symbol_rate, 0.6, 361))
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=decim_factor,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq, #fc
        	signal_samp_rate, #bw
        	'Shifted signal', #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(True)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [6, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-100, -30)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_0_grid_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_win, 2, 0, 1, 4)
        for r in range(2, 3):
            self.qtgui_tab_widget_0_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 4):
            self.qtgui_tab_widget_0_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq+signal_samp_rate, #fc
        	usrp_samp_rate, #bw
        	'Centered on RAW signal', #name
        	3 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 0)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(True)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(True)

        if not True:
          self.qtgui_freq_sink_x_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)

        labels = ['Filtered', 'Shifted', 'RAW', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "black", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(3):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_0_grid_layout_0.addWidget(self._qtgui_freq_sink_x_1_win, 1, 0, 1, 4)
        for r in range(1, 2):
            self.qtgui_tab_widget_0_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 4):
            self.qtgui_tab_widget_0_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq, #fc
        	signal_samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_0_grid_layout_1.addWidget(self._qtgui_freq_sink_x_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.qtgui_tab_widget_0_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_0_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(1.0 / symbol_rate)
        self.qtgui_const_sink_x_0.set_y_axis(-1, 1)
        self.qtgui_const_sink_x_0.set_x_axis(-1, 1)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_0_grid_layout_2.addWidget(self._qtgui_const_sink_x_0_win, 0, 0, 3, 1)
        for r in range(0, 3):
            self.qtgui_tab_widget_0_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_0_grid_layout_2.setColumnStretch(c, 1)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	2, usrp_samp_rate, signal_samp_rate, 25e3, firdes.WIN_HAMMING, 6.76))
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(pll_alpha, 4, False)
        self.digital_constellation_soft_decoder_cf_0 = digital.constellation_soft_decoder_cf(digital.constellation_calcdist(([-1-1j, -1+1j, 1+1j, 1-1j]), ([0, 1, 3, 2]), 4, 1).base())
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_cc(samp_per_sec, clock_alpha**2/4.0, 0.5, clock_alpha, 0.005)
        self.blocks_wavfile_sink_1 = blocks.wavfile_sink(file_path+"_rawIQ.wav", 2, int(usrp_samp_rate/decim_factor), 8)
        self.blocks_mute_xx_0 = blocks.mute_cc(bool(record))
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 127)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, file_path, False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(usrp_samp_rate, analog.GR_COS_WAVE, signal_samp_rate, 1, 0)
        self.analog_rail_ff_0 = analog.rail_ff(-1, 1)
        self.analog_agc_xx_0 = analog.agc_cc(100e-3, 500e-3, 1.0)
        self.analog_agc_xx_0.set_max_gain(4e3)
        self.USRP = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		args='peak=0.003906',
        		channels=range(1),
        	),
        )
        self.USRP.set_samp_rate(usrp_samp_rate)
        self.USRP.set_center_freq(rx_freq+signal_samp_rate, 0)
        self.USRP.set_gain(rf_gain, 0)
        self.USRP.set_antenna('TX/RX', 0)
        self.USRP.set_bandwidth(usrp_samp_rate, 0)
        self.USRP.set_auto_dc_offset(True, 0)
        self.USRP.set_auto_iq_balance(True, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.USRP, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.USRP, 0), (self.blocks_mute_xx_0, 0))
        self.connect((self.USRP, 0), (self.qtgui_freq_sink_x_1, 2))
        self.connect((self.analog_agc_xx_0, 0), (self.root_raised_cosine_filter_0, 0))
        self.connect((self.analog_rail_ff_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_wavfile_sink_1, 1))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_wavfile_sink_1, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_freq_sink_x_1, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.blocks_mute_xx_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_constellation_soft_decoder_cf_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.digital_constellation_soft_decoder_cf_0, 0), (self.analog_rail_ff_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_agc_xx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.digital_costas_loop_cc_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_symbol_rate(self):
        return self.symbol_rate

    def set_symbol_rate(self, symbol_rate):
        self.symbol_rate = symbol_rate
        self.set_samp_per_sec((self.signal_samp_rate * 1.0) / (self.symbol_rate * 1.0))
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.signal_samp_rate, self.symbol_rate, 0.6, 361))
        self.qtgui_const_sink_x_0.set_update_time(1.0 / self.symbol_rate)

    def get_signal_samp_rate(self):
        return self.signal_samp_rate

    def set_signal_samp_rate(self, signal_samp_rate):
        self.signal_samp_rate = signal_samp_rate
        self.set_usrp_samp_rate(self.signal_samp_rate*self.decim_factor)
        self.set_samp_per_sec((self.signal_samp_rate * 1.0) / (self.symbol_rate * 1.0))
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.signal_samp_rate, self.symbol_rate, 0.6, 361))
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.signal_samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(self.rx_freq+self.signal_samp_rate, self.usrp_samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq, self.signal_samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(2, self.usrp_samp_rate, self.signal_samp_rate, 25e3, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0.set_frequency(self.signal_samp_rate)
        self.USRP.set_center_freq(self.rx_freq+self.signal_samp_rate, 0)

    def get_path_to_save_dir(self):
        return self.path_to_save_dir

    def set_path_to_save_dir(self, path_to_save_dir):
        self.path_to_save_dir = path_to_save_dir
        self.set_file_path(self.path_to_save_dir + "/LRPT_" + datetime.now().strftime("%d%m%Y_%H%M")+".s")

    def get_decim_factor(self):
        return self.decim_factor

    def set_decim_factor(self, decim_factor):
        self.decim_factor = decim_factor
        self.set_usrp_samp_rate(self.signal_samp_rate*self.decim_factor)

    def get_usrp_samp_rate(self):
        return self.usrp_samp_rate

    def set_usrp_samp_rate(self, usrp_samp_rate):
        self.usrp_samp_rate = usrp_samp_rate
        self.qtgui_freq_sink_x_1.set_frequency_range(self.rx_freq+self.signal_samp_rate, self.usrp_samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(2, self.usrp_samp_rate, self.signal_samp_rate, 25e3, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0.set_sampling_freq(self.usrp_samp_rate)
        self.USRP.set_samp_rate(self.usrp_samp_rate)
        self.USRP.set_bandwidth(self.usrp_samp_rate, 0)

    def get_samp_per_sec(self):
        return self.samp_per_sec

    def set_samp_per_sec(self, samp_per_sec):
        self.samp_per_sec = samp_per_sec
        self.digital_clock_recovery_mm_xx_0.set_omega(self.samp_per_sec)

    def get_rx_freq_old(self):
        return self.rx_freq_old

    def set_rx_freq_old(self, rx_freq_old):
        self.rx_freq_old = rx_freq_old

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        self._rx_freq_callback(self.rx_freq)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.signal_samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(self.rx_freq+self.signal_samp_rate, self.usrp_samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq, self.signal_samp_rate)
        self.USRP.set_center_freq(self.rx_freq+self.signal_samp_rate, 0)

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self.USRP.set_gain(self.rf_gain, 0)


    def get_record(self):
        return self.record

    def set_record(self, record):
        self.record = record
        self._record_callback(self.record)
        self.blocks_mute_xx_0.set_mute(bool(self.record))

    def get_pll_alpha(self):
        return self.pll_alpha

    def set_pll_alpha(self, pll_alpha):
        self.pll_alpha = pll_alpha
        self.digital_costas_loop_cc_0.set_loop_bandwidth(self.pll_alpha)

    def get_file_path(self):
        return self.file_path

    def set_file_path(self, file_path):
        self.file_path = file_path
        self.blocks_wavfile_sink_1.open(self.file_path+"_rawIQ.wav")
        self.blocks_file_sink_0.open(self.file_path)

    def get_clock_alpha(self):
        return self.clock_alpha

    def set_clock_alpha(self, clock_alpha):
        self.clock_alpha = clock_alpha
        self.digital_clock_recovery_mm_xx_0.set_gain_omega(self.clock_alpha**2/4.0)
        self.digital_clock_recovery_mm_xx_0.set_gain_mu(self.clock_alpha)


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
