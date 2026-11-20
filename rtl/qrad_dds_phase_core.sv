// ============================================================================
// rtl/qrad_dds_phase_core.sv
// Module M-04 (WORK-ORDER-AGH-03 / Revision V2.0-AGH)
// Synthesizable IEEE 1800-2017 Quarter-Wave Sine DDS (20 MHz @ 100 MHz clk),
// Exact 0-LSB 0/180-deg A/B Phase Inversion Toggle, and Fail-Closed Interlock.
//
// Supersedes the historical sawtooth/placeholder snippet in QRAD-CE-V3.md.
// Interfaces directly with V-MAX-12 odos_gate_core.sv via ext_gate_pass_i.
// ============================================================================
`timescale 1ns/1ps

module qrad_dds_phase_core #(
    parameter logic [31:0] PHASE_STEP = 32'd858993459  // 20.000000 MHz @ 100 MHz clk
) (
    input  logic               clk_i,
    input  logic               rst_ni,
    input  logic               enable_i,
    input  logic               ext_gate_pass_i,
    input  logic [31:0]        phase_offset_i,
    output logic signed [13:0] dac_data_o,
    output logic               veto_pin_o,
    output logic [31:0]        phase_acc_o
);

    logic [31:0] phase_acc_q;
    logic [31:0] eff_phase_w;
    logic [1:0]  quad_w;
    logic [5:0]  raw_idx_w;
    logic [5:0]  lut_idx_w;
    logic [13:0] qwave_mag;
    logic signed [13:0] sine_sample_w;
    logic        permitted_w;

    // Effective phase with exact A/B offset (0x0000_0000 = 0 deg, 0x8000_0000 = 180 deg)
    assign eff_phase_w = phase_acc_q + phase_offset_i;
    assign quad_w      = eff_phase_w[31:30];
    assign raw_idx_w   = eff_phase_w[29:24];
    assign lut_idx_w   = quad_w[0] ? (6'd63 - raw_idx_w) : raw_idx_w;
    assign permitted_w = enable_i & ext_gate_pass_i;
    assign phase_acc_o = eff_phase_w;

    // Half-step centered quarter-wave sine LUT: guarantees exact 0-LSB antisymmetry (-sin(x) = sin(x+pi))
    always_comb begin
        unique case (lut_idx_w)
            6'd 0: qwave_mag = 14'd101;
            6'd 1: qwave_mag = 14'd301;
            6'd 2: qwave_mag = 14'd502;
            6'd 3: qwave_mag = 14'd703;
            6'd 4: qwave_mag = 14'd903;
            6'd 5: qwave_mag = 14'd1102;
            6'd 6: qwave_mag = 14'd1301;
            6'd 7: qwave_mag = 14'd1499;
            6'd 8: qwave_mag = 14'd1696;
            6'd 9: qwave_mag = 14'd1893;
            6'd10: qwave_mag = 14'd2088;
            6'd11: qwave_mag = 14'd2281;
            6'd12: qwave_mag = 14'd2474;
            6'd13: qwave_mag = 14'd2665;
            6'd14: qwave_mag = 14'd2854;
            6'd15: qwave_mag = 14'd3041;
            6'd16: qwave_mag = 14'd3227;
            6'd17: qwave_mag = 14'd3411;
            6'd18: qwave_mag = 14'd3593;
            6'd19: qwave_mag = 14'd3772;
            6'd20: qwave_mag = 14'd3950;
            6'd21: qwave_mag = 14'd4124;
            6'd22: qwave_mag = 14'd4297;
            6'd23: qwave_mag = 14'd4467;
            6'd24: qwave_mag = 14'd4634;
            6'd25: qwave_mag = 14'd4798;
            6'd26: qwave_mag = 14'd4960;
            6'd27: qwave_mag = 14'd5118;
            6'd28: qwave_mag = 14'd5274;
            6'd29: qwave_mag = 14'd5426;
            6'd30: qwave_mag = 14'd5575;
            6'd31: qwave_mag = 14'd5720;
            6'd32: qwave_mag = 14'd5863;
            6'd33: qwave_mag = 14'd6001;
            6'd34: qwave_mag = 14'd6136;
            6'd35: qwave_mag = 14'd6267;
            6'd36: qwave_mag = 14'd6395;
            6'd37: qwave_mag = 14'd6519;
            6'd38: qwave_mag = 14'd6638;
            6'd39: qwave_mag = 14'd6754;
            6'd40: qwave_mag = 14'd6866;
            6'd41: qwave_mag = 14'd6973;
            6'd42: qwave_mag = 14'd7077;
            6'd43: qwave_mag = 14'd7176;
            6'd44: qwave_mag = 14'd7271;
            6'd45: qwave_mag = 14'd7361;
            6'd46: qwave_mag = 14'd7447;
            6'd47: qwave_mag = 14'd7528;
            6'd48: qwave_mag = 14'd7605;
            6'd49: qwave_mag = 14'd7678;
            6'd50: qwave_mag = 14'd7745;
            6'd51: qwave_mag = 14'd7809;
            6'd52: qwave_mag = 14'd7867;
            6'd53: qwave_mag = 14'd7921;
            6'd54: qwave_mag = 14'd7969;
            6'd55: qwave_mag = 14'd8013;
            6'd56: qwave_mag = 14'd8053;
            6'd57: qwave_mag = 14'd8087;
            6'd58: qwave_mag = 14'd8116;
            6'd59: qwave_mag = 14'd8141;
            6'd60: qwave_mag = 14'd8161;
            6'd61: qwave_mag = 14'd8176;
            6'd62: qwave_mag = 14'd8185;
            6'd63: qwave_mag = 14'd8190;
            default: qwave_mag = 14'd0;
        endcase
    end

    assign sine_sample_w = quad_w[1] ? -$signed(qwave_mag) : $signed(qwave_mag);

    // Fail-closed synchronous output & accumulator stage
    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            phase_acc_q <= 32'd0;
            dac_data_o  <= 14'sd0;
            veto_pin_o  <= 1'b1;  // Fail-closed on reset
        end else if (!permitted_w) begin
            // Hold output clamped to zero and keep hardware veto asserted
            dac_data_o  <= 14'sd0;
            veto_pin_o  <= 1'b1;
        end else begin
            phase_acc_q <= phase_acc_q + PHASE_STEP;
            dac_data_o  <= sine_sample_w;
            veto_pin_o  <= 1'b0;
        end
    end

endmodule
