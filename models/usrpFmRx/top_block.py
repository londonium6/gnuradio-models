#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sat Oct  7 01:36:29 2017
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
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
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
        self.tr_width = tr_width = 1e3
        self.squelchLvl = squelchLvl = -15
        self.samp_rate = samp_rate = 4e6
        self.deci_2 = deci_2 = 10
        self.deci_1 = deci_1 = 8
        self.cutoff = cutoff = 10e3
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
        	minimum=1e2,
        	maximum=1e4,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_tr_width_sizer)
        _squelchLvl_sizer = wx.BoxSizer(wx.VERTICAL)
        self._squelchLvl_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_squelchLvl_sizer,
        	value=self.squelchLvl,
        	callback=self.set_squelchLvl,
        	label='squelchLvl',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._squelchLvl_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_squelchLvl_sizer,
        	value=self.squelchLvl,
        	callback=self.set_squelchLvl,
        	minimum=-100,
        	maximum=0,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_squelchLvl_sizer)
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
        	minimum=1e3,
        	maximum=25e3,
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
        	maximum=600e6,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_Frequency_sizer)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(Frequency, 0)
        self.uhd_usrp_source_0.set_gain(32, 0)
        self.uhd_usrp_source_0.set_antenna('TX/RX', 0)
        self.low_pass_filter_0 = filter.fir_filter_ccf(deci_1, firdes.low_pass(
        	1, samp_rate, 110e3, 10e3, firdes.WIN_HAMMING, 6.76))
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_pwr_squelch_xx_0 = analog.pwr_squelch_ff(squelchLvl, 1e-4, 0, True)
        self.analog_fm_demod_cf_0 = analog.fm_demod_cf(
        	channel_rate=samp_rate/deci_1,
        	audio_decim=deci_2,
        	deviation=75e3,
        	audio_pass=cutoff,
        	audio_stop=tr_width+cutoff,
        	gain=1.0,
        	tau=75e-6,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_fm_demod_cf_0, 0), (self.analog_pwr_squelch_xx_0, 0))    
        self.connect((self.analog_pwr_squelch_xx_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.analog_fm_demod_cf_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_0, 0))    

    def get_tr_width(self):
        return self.tr_width

    def set_tr_width(self, tr_width):
        self.tr_width = tr_width
        self._tr_width_slider.set_value(self.tr_width)
        self._tr_width_text_box.set_value(self.tr_width)

    def get_squelchLvl(self):
        return self.squelchLvl

    def set_squelchLvl(self, squelchLvl):
        self.squelchLvl = squelchLvl
        self._squelchLvl_slider.set_value(self.squelchLvl)
        self._squelchLvl_text_box.set_value(self.squelchLvl)
        self.analog_pwr_squelch_xx_0.set_threshold(self.squelchLvl)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 110e3, 10e3, firdes.WIN_HAMMING, 6.76))

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

    def get_Frequency(self):
        return self.Frequency

    def set_Frequency(self, Frequency):
        self.Frequency = Frequency
        self._Frequency_slider.set_value(self.Frequency)
        self._Frequency_text_box.set_value(self.Frequency)
        self.uhd_usrp_source_0.set_center_freq(self.Frequency, 0)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
