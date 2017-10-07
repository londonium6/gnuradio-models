#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sat Oct  7 01:35:22 2017
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

from gnuradio import analog
from gnuradio import audio
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.tr_width = tr_width = 10e3
        self.samp_rate = samp_rate = 1.2e6
        self.deci_2 = deci_2 = 3
        self.deci_1 = deci_1 = 9
        self.cutoff = cutoff = 100e3
        self.Frequency = Frequency = 104.3e6

        ##################################################
        # Blocks
        ##################################################
        _tr_width_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tr_width_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tr_width_sizer,
        	value=self.tr_width,
        	callback=self.set_tr_width,
        	label='tr_width',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tr_width_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tr_width_sizer,
        	value=self.tr_width,
        	callback=self.set_tr_width,
        	minimum=1e3,
        	maximum=100e3,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_tr_width_sizer)
        _cutoff_sizer = wx.BoxSizer(wx.VERTICAL)
        self._cutoff_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_cutoff_sizer,
        	value=self.cutoff,
        	callback=self.set_cutoff,
        	label='cutoff',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._cutoff_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_cutoff_sizer,
        	value=self.cutoff,
        	callback=self.set_cutoff,
        	minimum=50e3,
        	maximum=200e3,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_cutoff_sizer)
        _Frequency_sizer = wx.BoxSizer(wx.VERTICAL)
        self._Frequency_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_Frequency_sizer,
        	value=self.Frequency,
        	callback=self.set_Frequency,
        	label='Frequency',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._Frequency_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_Frequency_sizer,
        	value=self.Frequency,
        	callback=self.set_Frequency,
        	minimum=88e6,
        	maximum=108e6,
        	num_steps=(108-88)*10,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_Frequency_sizer)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(Frequency, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(10, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
          
        self.low_pass_filter_0 = filter.fir_filter_ccf(deci_1, firdes.low_pass(
        	1, samp_rate, cutoff, tr_width, firdes.WIN_HAMMING, 6.76))
        self.audio_sink_0 = audio.sink(44100, '', True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=samp_rate/deci_1,
        	audio_decimation=deci_2,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.analog_wfm_rcv_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.low_pass_filter_0, 0))    

    def get_tr_width(self):
        return self.tr_width

    def set_tr_width(self, tr_width):
        self.tr_width = tr_width
        self._tr_width_slider.set_value(self.tr_width)
        self._tr_width_text_box.set_value(self.tr_width)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.tr_width, firdes.WIN_HAMMING, 6.76))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.tr_width, firdes.WIN_HAMMING, 6.76))

    def get_deci_2(self):
        return self.deci_2

    def set_deci_2(self, deci_2):
        self.deci_2 = deci_2

    def get_deci_1(self):
        return self.deci_1

    def set_deci_1(self, deci_1):
        self.deci_1 = deci_1

    def get_cutoff(self):
        return self.cutoff

    def set_cutoff(self, cutoff):
        self.cutoff = cutoff
        self._cutoff_slider.set_value(self.cutoff)
        self._cutoff_text_box.set_value(self.cutoff)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.tr_width, firdes.WIN_HAMMING, 6.76))

    def get_Frequency(self):
        return self.Frequency

    def set_Frequency(self, Frequency):
        self.Frequency = Frequency
        self._Frequency_slider.set_value(self.Frequency)
        self._Frequency_text_box.set_value(self.Frequency)
        self.rtlsdr_source_0.set_center_freq(self.Frequency, 0)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
