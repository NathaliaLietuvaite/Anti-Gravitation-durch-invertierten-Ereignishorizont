SIM ?= verilator
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/qrad_dds_phase_core.sv
TOPLEVEL = qrad_dds_phase_core
COCOTB_TEST_MODULES = test_qrad_dds_cocotb
EXTRA_ARGS += --timing -Wall

include $(shell cocotb-config --makefiles)/Makefile.sim
