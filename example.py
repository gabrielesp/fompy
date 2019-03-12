import fompy

# ------------------------------------------------------------------------------------------#
# BASIC COMMANDS 

# path_file_JCJB = './data/sim_FinFET_vd_high/'
# fds = fompy.dataset(path_file_JCJB, parser=fompy.JCJB)
# fds.print_parameters()


# ------------------------------------------------------------------------------------------#
# EXCLUDING CURVES FROM THE IMPORT

# path_file_JCJB = './data/sim_FinFET_vd_high/'
# fds = fompy.dataset(path_file_JCJB, parser=fompy.JCJB, exclude=[5,6])
# fds.print_parameters()
# fds = fompy.dataset(path_file_JCJB, parser=fompy.JCJB, interval=[0,4])
# fds.print_parameters()

# ------------------------------------------------------------------------------------------#
# DATA CONDITIONING

# path_file_JCJB = './data/sim_FinFET_vd_high/'
# fds = fompy.dataset(path_file_JCJB, parser=fompy.JCJB)
# norm_value = 35.8/10**9
# fompy.normalize(fds, norm_value)
# print(fds.dataset)

# fompy.filter(fds, theta_crit = 0.5, show_theta=True)

# ------------------------------------------------------------------------------------------#
# DIFFERENT EXTRACTION PARSERS 

# path_file_mc = './data/mc_data/'
# fds1 = fompy.dataset(path_file_mc, parser=fompy.MC)
# fds1.print_parameters()
# print(fds1.dataset)

# path_file_JCJB = './data/sim_FinFET_vd_high/'
# fds2 = fompy.dataset(path_file_JCJB, parser=fompy.JCJB)
# fds2.print_parameters()
# print(fds2.dataset)
# print(fds2.sanity_array)

# ------------------------------------------------------------------------------------------#
# SAVING EXTRACTION TO FILES

# path_to_save='./sim_data.dat'
# path_file_JCJB = './data/sim_FinFET_vd_high/'
# fds = fompy.dataset(path_file_JCJB, parser=fompy.JCJB, save_to_file = path_to_save)

# vth_array = fompy.extract(fds, fom = 'vth')
# fompy.savetotxt('./results_vth.txt', 'vth', vth_array)


# ------------------------------------------------------------------------------------------#
# VTH EXTRACTION & PLOT FULL LIST OF ARGUMENTS

# path_file_JCJB = './data/sim_FinFET_vd_high/'
# fds = fompy.dataset(path_file_JCJB, parser=fompy.JCJB)
# vth_array = fompy.extract(fds, fom = 'vth')
# print(vth_array)
# fompy.plot(fds, fom = 'vth', save_plot='./vth_plots/sd/')
# fompy.plot(fds, fom = 'vth')

# path_file_var = './data/simulations/'
# fds_var = fompy.dataset(path_file_var, parser=fompy.JCJB)
# vth_array = fompy.extract(fds_var, fom = 'vth')

# import numpy as np
# print('STDEV:',np.std(vth_array))
# print('MEAN:',np.mean(vth_array))

# path_file_JCJB = './data/sim_FinFET_vd_high/'
# fds = fompy.dataset(path_file_JCJB, parser=fompy.JCJB)
# vth_array_cc = fompy.extract(fds, fom = 'vth', method = 'CC', cc_criteria=1.5e-6)
# print(vth_array_cc)
# fompy.plot(fds, fom = 'vth',method = 'CC',cc_criteria = 1.5e-6, save_plot='./vth_plots/')

# path_file_JCJB = './data/sim_FinFET_vd_high/'
# fds = fompy.dataset(path_file_JCJB, parser=fompy.JCJB)
# vth_array_td = fompy.extract(fds, fom = 'vth', method = 'TD')
# print(vth_array_td)
# fompy.plot(fds, fom = 'vth',method = 'TD', save_plot='./vth_plots/td/')

# path_file_JCJB = './data/sim_FinFET_vd_high/'
# fds = fompy.dataset(path_file_JCJB, parser=fompy.JCJB)
# vth_array_le = fompy.extract(fds, fom = 'vth', method = 'LE')
# print(vth_array_le)
# fompy.plot(fds, fom = 'vth',method = 'LE')

# ------------------------------------------------------------------------------------------#
# IOFF EXTRACTION & PLOT FULL LIST OF ARGUMENTS

# path_file_JCJB = './data/sim_FinFET_vd_high/'
# fds = fompy.dataset(path_file_JCJB, parser=fompy.JCJB)
# ioff_array = fompy.extract(fds, fom = 'ioff', vg_ext = 0.2)
# print(ioff_array)
# fompy.savetotxt('./results_ioff.txt', 'ioff', ioff_array)


# path_file_JCJB = './data/sim_FinFET_vd_high/'
# fds = fompy.dataset(path_file_JCJB, parser=fompy.JCJB)
# ioff_array = fompy.extract(fds, fom = 'ioff', vg_ext = 0.2)
# print(ioff_array)

# fompy.plot(fds, fom = 'ioff', vg_ext = 0.2, save_plot='./ioff_plots/')


# ------------------------------------------------------------------------------------------#
# ION EXTRACTION & PLOT FULL LIST OF ARGUMENTS

# path_file_JCJB = './data/sim_FinFET_vd_high/'
# fds = fompy.dataset(path_file_JCJB, parser=fompy.JCJB)
# ion_array_vg_defined = fompy.extract(fds, fom = 'ion',vg_ext = 0.7)
# print(ion_array_vg_defined)

# ion_array_default_SD = fompy.extract(fds, fom = 'ion')
# print(ion_array_default_SD)

# ion_array_LE = fompy.extract(fds, fom = 'ion',method = 'LE')
# print(ion_array_LE)

# ion_array_TD = fompy.extract(fds, fom = 'ion',method = 'TD')
# print(ion_array_TD)

# fompy.plot(fds, fom = 'ion', vg_ext = 0.5)
# fompy.plot(fds, fom = 'ion')
# fompy.plot(fds, fom = 'ion', method='TD')

# ------------------------------------------------------------------------------------------#
# SS EXTRACTION & PLOT FULL LIST OF ARGUMENTS

# path_file_JCJB = './data/sim_FinFET_vd_high/'
# fds = fompy.dataset(path_file_JCJB, parser=fompy.JCJB)

# ss_array = fompy.extract(fds, fom = 'ss')
# print(ss_array)

# ss_array = fompy.extract(fds, fom = 'ss', vg_start = 0.05)
# print(ss_array)

# ss_array = fompy.extract(fds, fom = 'ss', vg_start = 0.05, vg_end = 0.2)
# print(ss_array)

# ss_array = fompy.extract(fds, fom = 'ss', vg_end = 0.2)
# print(ss_array)


# ------------------------------------------------------------------------------------------#
# DIBL EXTRACTION & PLOT FULL LIST OF ARGUMENTS

# path_file_JCJB = './data/sim_FinFET_vd_high/'
# path_file_low = './data/sim_FinFET_vd_low/'


# fds_hdb = fompy.dataset(path_file_JCJB, parser=fompy.JCJB)
# fds_ldb = fompy.dataset(path_file_low, parser=fompy.JCJB)
# fds_hdb.drain_bias_value = 0.7
# fds_ldb.drain_bias_value = 0.05

# dibl_array = fompy.extract(fds_hdb, fds_ldb, fom = 'dibl')
# print(dibl_array)

# fompy.plot(fds_hdb, fds_ldb, fom = 'dibl')


# ------------------------------------------------------------------------------------------#
# FULL EXTRACTION & PLOT FULL LIST OF ARGUMENTS

# path_file_JCJB = './data/sim_FinFET_vd_high/'
# path_file_low = './data/sim_FinFET_vd_low/'

# fds_hdb = fompy.dataset(path_file_JCJB, parser=fompy.JCJB)
# fds_hdb.print_parameters()
# fds_ldb = fompy.dataset(path_file_low, parser=fompy.JCJB)
# fds_ldb.print_parameters()

# vth, ioff, ion, ss= fompy.extract(fds_hdb, print_fom=True)

# fds1_parameters, fds2_parameters= fompy.extract(fds_hdb, fds_ldb, print_fom=True)


# ------------------------------------------------------------------------------------------#
# GENERATING DIFFERENT PLOTS

# path_file_var = './data/simulations/'
# fds_var = fompy.dataset(path_file_var, parser=fompy.JCJB)
# vth_array = fompy.extract(fds_var, fom = 'vth')

# fompy.plot(fds_var, plot_type='hist', parameter=vth_array, bins=5)
# fompy.plot(fds_var, plot_type='qq', parameter=vth_array)

# path_file_var = './data/simulations/'
# fds_var = fompy.dataset(path_file_var, parser=fompy.JCJB)
# fompy.plot(fds_var, plot_type='varplot')


# path_file_JCJB = './data/sim_FinFET_vd_high/'
# path_file_low = './data/sim_FinFET_vd_low/'

# fds_hdb = fompy.dataset(path_file_JCJB, parser=fompy.JCJB)
# fds_hdb.print_parameters()
# fds_ldb = fompy.dataset(path_file_low, parser=fompy.JCJB)
# fds_ldb.print_parameters()

# norm_value = 35.8/10**9
# fompy.normalize(fds_hdb, norm_value)
# fompy.normalize(fds_ldb, norm_value)

# fompy.plot(fds_hdb,fds_ldb, plot_type='calib')