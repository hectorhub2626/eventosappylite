import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# --- DATOS ORIGINALES ---
RAW_DATA = [
    {"tvd": 10586.61, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_A1S", "interprete": "EIZM", "md": 10586.61, "tvdss": -9639.61, "diffMdTvd": 0},
    {"tvd": 11045.34, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_A2S", "interprete": "EIZM", "md": 11045.34, "tvdss": -10098.34, "diffMdTvd": 0},
    {"tvd": 11418.64, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_A3S", "interprete": "EIZM", "md": 11418.64, "tvdss": -10471.64, "diffMdTvd": 0},
    {"tvd": 11870.50, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_B1S", "interprete": "EIZM", "md": 11870.50, "tvdss": -10923.50, "diffMdTvd": 0},
    {"tvd": 12157.47, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_C1S", "interprete": "EIZM", "md": 12157.47, "tvdss": -11210.47, "diffMdTvd": 0},
    {"tvd": 12247.00, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_D1S", "interprete": "EIZM", "md": 12247.00, "tvdss": -11300.00, "diffMdTvd": 0},
    {"tvd": 12402.70, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_E1S", "interprete": "EIZM", "md": 12402.70, "tvdss": -11455.70, "diffMdTvd": 0},
    {"tvd": 12500.29, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_E2S", "interprete": "EIZM", "md": 12500.29, "tvdss": -11553.29, "diffMdTvd": 0},
    {"tvd": 12597.32, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_E3S", "interprete": "EIZM", "md": 12597.32, "tvdss": -11650.32, "diffMdTvd": 0},
    {"tvd": 12699.70, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_F1S", "interprete": "EIZM", "md": 12699.70, "tvdss": -11752.70, "diffMdTvd": 0},
    {"tvd": 12838.68, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_F2S", "interprete": "EIZM", "md": 12838.68, "tvdss": -11891.68, "diffMdTvd": 0},
    {"tvd": 12903.53, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_F2M", "interprete": "EIZM", "md": 12903.53, "tvdss": -11956.53, "diffMdTvd": 0},
    {"tvd": 13094.82, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_F2I", "interprete": "EIZM", "md": 13094.82, "tvdss": -12147.82, "diffMdTvd": 0},
    {"tvd": 13162.17, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_F3S", "interprete": "EIZM", "md": 13162.17, "tvdss": -12215.17, "diffMdTvd": 0},
    {"tvd": 13329.39, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_G1S", "interprete": "EIZM", "md": 13329.39, "tvdss": -12382.39, "diffMdTvd": 0},
    {"tvd": 13420.23, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_H1S", "interprete": "EIZM", "md": 13420.23, "tvdss": -12473.23, "diffMdTvd": 0},
    {"tvd": 13498.47, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_H2S", "interprete": "EIZM", "md": 13498.47, "tvdss": -12551.47, "diffMdTvd": 0},
    {"tvd": 13565.79, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_H3S", "interprete": "EIZM", "md": 13565.79, "tvdss": -12618.79, "diffMdTvd": 0},
    {"tvd": 13706.20, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_I1S", "interprete": "EIZM", "md": 13706.20, "tvdss": -12759.20, "diffMdTvd": 0},
    {"tvd": 13878.32, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_J1S", "interprete": "EIZM", "md": 13878.32, "tvdss": -12931.32, "diffMdTvd": 0},
    {"tvd": 14048.14, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_K1S", "interprete": "EIZM", "md": 14048.14, "tvdss": -13101.14, "diffMdTvd": 0},
    {"tvd": 14148.84, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_K1M", "interprete": "EIZM", "md": 14148.84, "tvdss": -13201.84, "diffMdTvd": 0},
    {"tvd": 14206.47, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_K1I", "interprete": "EIZM", "md": 14206.47, "tvdss": -13259.47, "diffMdTvd": 0},
    {"tvd": 14243.97, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_L1S", "interprete": "EIZM", "md": 14243.97, "tvdss": -13296.97, "diffMdTvd": 0},
    {"tvd": 14281.47, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_L1I", "interprete": "EIZM", "md": 14281.47, "tvdss": -13334.47, "diffMdTvd": 0},
    {"tvd": 14312.72, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_L2S", "interprete": "EIZM", "md": 14312.72, "tvdss": -13365.72, "diffMdTvd": 0},
    {"tvd": 14361.68, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_L2I", "interprete": "EIZM", "md": 14361.68, "tvdss": -13414.68, "diffMdTvd": 0},
    {"tvd": 14422.23, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_L3S", "interprete": "EIZM", "md": 14422.23, "tvdss": -13475.23, "diffMdTvd": 0},
    {"tvd": 14466.89, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_L3I", "interprete": "EIZM", "md": 14466.89, "tvdss": -13519.89, "diffMdTvd": 0},
    {"tvd": 14508.54, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_L4S", "interprete": "EIZM", "md": 14508.54, "tvdss": -13561.54, "diffMdTvd": 0},
    {"tvd": 14557.52, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_M1S", "interprete": "EIZM", "md": 14557.52, "tvdss": -13610.52, "diffMdTvd": 0},
    {"tvd": 14610.64, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_M2S", "interprete": "EIZM", "md": 14610.64, "tvdss": -13663.64, "diffMdTvd": 0},
    {"tvd": 14667.93, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_M3S", "interprete": "EIZM", "md": 14667.93, "tvdss": -13720.93, "diffMdTvd": 0},
    {"tvd": 14728.35, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_M4S", "interprete": "EIZM", "md": 14728.35, "tvdss": -13781.35, "diffMdTvd": 0},
    {"tvd": 14771.06, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_N1S", "interprete": "EIZM", "md": 14771.06, "tvdss": -13824.06, "diffMdTvd": 0},
    {"tvd": 14828.35, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_O1S", "interprete": "EIZM", "md": 14828.35, "tvdss": -13881.35, "diffMdTvd": 0},
    {"tvd": 14889.81, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_P1S", "interprete": "EIZM", "md": 14889.81, "tvdss": -13942.81, "diffMdTvd": 0},
    {"tvd": 14963.85, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_P2S", "interprete": "EIZM", "md": 14963.85, "tvdss": -14016.85, "diffMdTvd": 0},
    {"tvd": 15035.34, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_R1S", "interprete": "EIZM", "md": 15035.34, "tvdss": -14088.34, "diffMdTvd": 0},
    {"tvd": 15065.50, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_R1I", "interprete": "EIZM", "md": 15065.50, "tvdss": -14118.50, "diffMdTvd": 0},
    {"tvd": 15095.86, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_R2S", "interprete": "EIZM", "md": 15095.86, "tvdss": -14148.86, "diffMdTvd": 0},
    {"tvd": 15126.15, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_R2I", "interprete": "EIZM", "md": 15126.15, "tvdss": -14179.15, "diffMdTvd": 0},
    {"tvd": 15147.59, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_R3S", "interprete": "EIZM", "md": 15147.59, "tvdss": -14200.59, "diffMdTvd": 0},
    {"tvd": 15185.96, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_R3I", "interprete": "EIZM", "md": 15185.96, "tvdss": -14238.96, "diffMdTvd": 0},
    {"tvd": 15216.43, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_R4S", "interprete": "EIZM", "md": 15216.43, "tvdss": -14269.43, "diffMdTvd": 0},
    {"tvd": 15245.77, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_R4M", "interprete": "EIZM", "md": 15245.77, "tvdss": -14298.77, "diffMdTvd": 0},
    {"tvd": 15307.83, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_R4I", "interprete": "EIZM", "md": 15307.83, "tvdss": -14360.83, "diffMdTvd": 0},
    {"tvd": 15342.82, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_S1S", "interprete": "EIZM", "md": 15342.82, "tvdss": -14395.82, "diffMdTvd": 0},
    {"tvd": 15366.51, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_S2S", "interprete": "EIZM", "md": 15366.51, "tvdss": -14419.51, "diffMdTvd": 0},
    {"tvd": 15404.88, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_S3S", "interprete": "EIZM", "md": 15404.88, "tvdss": -14457.88, "diffMdTvd": 0},
    {"tvd": 15457.92, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_S3I", "interprete": "EIZM", "md": 15457.92, "tvdss": -14510.92, "diffMdTvd": 0},
    {"tvd": 15517.73, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_S4S", "interprete": "EIZM", "md": 15517.73, "tvdss": -14570.73, "diffMdTvd": 0},
    {"tvd": 15549.40, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_S5S", "interprete": "EIZM", "md": 15549.40, "tvdss": -14602.40, "diffMdTvd": 0},
    {"tvd": 15660.49, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_T1S", "interprete": "EIZM", "md": 15660.49, "tvdss": -14713.49, "diffMdTvd": 0},
    {"tvd": 15711.53, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_U1S", "interprete": "EIZM", "md": 15711.53, "tvdss": -14764.53, "diffMdTvd": 0},
    {"tvd": 15762.57, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_U1M", "interprete": "EIZM", "md": 15762.57, "tvdss": -14815.57, "diffMdTvd": 0},
    {"tvd": 15802.31, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Ofic_U1I", "interprete": "EIZM", "md": 15802.31, "tvdss": -14855.31, "diffMdTvd": 0},
    {"tvd": 15871.75, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Mer_U2S", "interprete": "EIZM", "md": 15871.75, "tvdss": -14924.75, "diffMdTvd": 0},
    {"tvd": 15892.94, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Mer_U3S", "interprete": "EIZM", "md": 15892.94, "tvdss": -14945.94, "diffMdTvd": 0},
    {"tvd": 15975.95, "uwi": "00108AGM0001X 01", "pozo": "AGM-001", "unidad": "Fs_Mer_U4S", "interprete": "EIZM", "md": 15975.95, "tvdss": -15028.95, "diffMdTvd": 0},
    # AGM-003
    {"tvd": 10515.90, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_A1S", "interprete": "EIZM", "md": 10515.90, "tvdss": -9640.90, "diffMdTvd": 0},
    {"tvd": 11820.67, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_B1S", "interprete": "EIZM", "md": 11820.67, "tvdss": -10945.67, "diffMdTvd": 0},
    {"tvd": 14797.28, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_R1S", "interprete": "EIZM", "md": 14797.28, "tvdss": -13922.28, "diffMdTvd": 0},
    {"tvd": 11043.79, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_A2S", "interprete": "EIZM", "md": 11043.79, "tvdss": -10168.79, "diffMdTvd": 0},
    {"tvd": 11333.88, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_A3S", "interprete": "EIZM", "md": 11333.88, "tvdss": -10458.88, "diffMdTvd": 0},
    {"tvd": 14168.64, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_L3S", "interprete": "EIZM", "md": 14168.64, "tvdss": -13293.64, "diffMdTvd": 0},
    {"tvd": 12256.82, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_E2S", "interprete": "EIZM", "md": 12256.82, "tvdss": -11381.82, "diffMdTvd": 0},
    {"tvd": 12361.40, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_E3S", "interprete": "EIZM", "md": 12361.40, "tvdss": -11486.40, "diffMdTvd": 0},
    {"tvd": 13486.46, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_I1S", "interprete": "EIZM", "md": 13486.46, "tvdss": -12611.46, "diffMdTvd": 0},
    {"tvd": 13337.58, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_H3S", "interprete": "EIZM", "md": 13337.58, "tvdss": -12462.58, "diffMdTvd": 0},
    {"tvd": 13994.28, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_L1S", "interprete": "EIZM", "md": 13994.28, "tvdss": -13119.28, "diffMdTvd": 0},
    {"tvd": 12723.87, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_F2M", "interprete": "EIZM", "md": 12723.87, "tvdss": -11848.87, "diffMdTvd": 0},
    {"tvd": 12474.41, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_F1S", "interprete": "EIZM", "md": 12474.41, "tvdss": -11599.41, "diffMdTvd": 0},
    {"tvd": 12939.58, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_F3S", "interprete": "EIZM", "md": 12939.58, "tvdss": -12064.58, "diffMdTvd": 0},
    {"tvd": 12857.55, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_F2I", "interprete": "EIZM", "md": 12857.55, "tvdss": -11982.55, "diffMdTvd": 0},
    {"tvd": 13190.01, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_H1S", "interprete": "EIZM", "md": 13190.01, "tvdss": -12315.01, "diffMdTvd": 0},
    {"tvd": 13103.64, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_G1S", "interprete": "EIZM", "md": 13103.64, "tvdss": -12228.64, "diffMdTvd": 0},
    {"tvd": 13684.52, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_J1S", "interprete": "EIZM", "md": 13684.52, "tvdss": -12809.52, "diffMdTvd": 0},
    {"tvd": 14855.82, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_R2S", "interprete": "EIZM", "md": 14855.82, "tvdss": -13980.82, "diffMdTvd": 0},
    {"tvd": 14034.45, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_L1I", "interprete": "EIZM", "md": 14034.45, "tvdss": -13159.45, "diffMdTvd": 0},
    {"tvd": 13905.62, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_K1M", "interprete": "EIZM", "md": 13905.62, "tvdss": -13030.62, "diffMdTvd": 0},
    {"tvd": 14368.12, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_M2S", "interprete": "EIZM", "md": 14368.12, "tvdss": -13493.12, "diffMdTvd": 0},
    {"tvd": 14480.92, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_M4S", "interprete": "EIZM", "md": 14480.92, "tvdss": -13605.92, "diffMdTvd": 0},
    {"tvd": 14644.28, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_P1S", "interprete": "EIZM", "md": 14644.28, "tvdss": -13769.28, "diffMdTvd": 0},
    {"tvd": 15310.85, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_S5S", "interprete": "EIZM", "md": 15310.85, "tvdss": -14435.85, "diffMdTvd": 0},
    {"tvd": 14999.91, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_R4M", "interprete": "EIZM", "md": 14999.91, "tvdss": -14124.91, "diffMdTvd": 0},
    {"tvd": 15086.47, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_S1S", "interprete": "EIZM", "md": 15086.47, "tvdss": -14211.47, "diffMdTvd": 0},
    {"tvd": 13813.21, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_K1S", "interprete": "EIZM", "md": 13813.21, "tvdss": -12938.21, "diffMdTvd": 0},
    {"tvd": 14113.80, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_L2I", "interprete": "EIZM", "md": 14113.80, "tvdss": -13238.80, "diffMdTvd": 0},
    {"tvd": 14913.21, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_R3S", "interprete": "EIZM", "md": 14913.21, "tvdss": -14038.21, "diffMdTvd": 0},
    {"tvd": 13267.85, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_H2S", "interprete": "EIZM", "md": 13267.85, "tvdss": -12392.85, "diffMdTvd": 0},
    {"tvd": 14217.07, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_L3I", "interprete": "EIZM", "md": 14217.07, "tvdss": -13342.07, "diffMdTvd": 0},
    {"tvd": 12646.22, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_F2S", "interprete": "EIZM", "md": 12646.22, "tvdss": -11771.22, "diffMdTvd": 0},
    {"tvd": 13959.09, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_K1I", "interprete": "EIZM", "md": 13959.09, "tvdss": -13084.09, "diffMdTvd": 0},
    {"tvd": 14062.99, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_L2S", "interprete": "EIZM", "md": 14062.99, "tvdss": -13187.99, "diffMdTvd": 0},
    {"tvd": 14424.37, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_M3S", "interprete": "EIZM", "md": 14424.37, "tvdss": -13549.37, "diffMdTvd": 0},
    {"tvd": 15284.88, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_S4S", "interprete": "EIZM", "md": 15284.88, "tvdss": -14409.88, "diffMdTvd": 0},
    {"tvd": 14252.49, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_L4S", "interprete": "EIZM", "md": 14252.49, "tvdss": -13377.49, "diffMdTvd": 0},
    {"tvd": 14733.34, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_P2S", "interprete": "EIZM", "md": 14733.34, "tvdss": -13858.34, "diffMdTvd": 0},
    {"tvd": 14592.37, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_O1S", "interprete": "EIZM", "md": 14592.37, "tvdss": -13717.37, "diffMdTvd": 0},
    {"tvd": 14517.72, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_N1S", "interprete": "EIZM", "md": 14517.72, "tvdss": -13642.72, "diffMdTvd": 0},
    {"tvd": 15216.94, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_S3I", "interprete": "EIZM", "md": 15216.94, "tvdss": -14341.94, "diffMdTvd": 0},
    {"tvd": 14874.75, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_R2I", "interprete": "EIZM", "md": 14874.75, "tvdss": -13999.75, "diffMdTvd": 0},
    {"tvd": 14962.25, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_R4S", "interprete": "EIZM", "md": 14962.25, "tvdss": -14087.25, "diffMdTvd": 0},
    {"tvd": 15118.50, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_S2S", "interprete": "EIZM", "md": 15118.50, "tvdss": -14243.50, "diffMdTvd": 0},
    {"tvd": 14310.82, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_M1S", "interprete": "EIZM", "md": 14310.82, "tvdss": -13435.82, "diffMdTvd": 0},
    {"tvd": 14824.67, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_R1I", "interprete": "EIZM", "md": 14824.67, "tvdss": -13949.67, "diffMdTvd": 0},
    {"tvd": 15175.71, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_S3S", "interprete": "EIZM", "md": 15175.71, "tvdss": -14300.71, "diffMdTvd": 0},
    {"tvd": 15055.92, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_R4I", "interprete": "EIZM", "md": 15055.92, "tvdss": -14180.92, "diffMdTvd": 0},
    {"tvd": 14899.67, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_R3I", "interprete": "EIZM", "md": 14899.67, "tvdss": -14024.67, "diffMdTvd": 0},
    {"tvd": 12139.58, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_E1S", "interprete": "EIZM", "md": 12139.58, "tvdss": -11264.58, "diffMdTvd": 0},
    {"tvd": 15657.98, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Mer_U2S", "interprete": "EIZM", "md": 15657.98, "tvdss": -14782.98, "diffMdTvd": 0},
    {"tvd": 15486.58, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_U1S", "interprete": "EIZM", "md": 15486.58, "tvdss": -14611.58, "diffMdTvd": 0},
    {"tvd": 15516.89, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_U1M", "interprete": "EIZM", "md": 15516.89, "tvdss": -14641.89, "diffMdTvd": 0},
    {"tvd": 15549.29, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_U1I", "interprete": "EIZM", "md": 15549.29, "tvdss": -14674.29, "diffMdTvd": 0},
    {"tvd": 15767.83, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Mer_U4S", "interprete": "EIZM", "md": 15767.83, "tvdss": -14892.83, "diffMdTvd": 0},
    {"tvd": 15667.39, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Mer_U3S", "interprete": "EIZM", "md": 15667.39, "tvdss": -14792.39, "diffMdTvd": 0},
    {"tvd": 12132.00, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_D1S", "interprete": "EIZM", "md": 12132.00, "tvdss": -11257.00, "diffMdTvd": 0},
    {"tvd": 15427.56, "uwi": "00108AGM0003  01", "pozo": "AGM-003", "unidad": "Fs_Ofic_T1S", "interprete": "EIZM", "md": 15427.56, "tvdss": -14552.56, "diffMdTvd": 0},
    # AGM-005
    {"tvd": 15144.06, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_R2S", "interprete": "EIZM", "md": 15144.06, "tvdss": -14149.06, "diffMdTvd": 0},
    {"tvd": 15084.20, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_R1S", "interprete": "EIZM", "md": 15084.20, "tvdss": -14089.20, "diffMdTvd": 0},
    {"tvd": 13965.24, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_J1S", "interprete": "EIZM", "md": 13965.24, "tvdss": -12970.24, "diffMdTvd": 0},
    {"tvd": 13776.81, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_I1S", "interprete": "EIZM", "md": 13776.81, "tvdss": -12781.81, "diffMdTvd": 0},
    {"tvd": 13634.33, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_H3S", "interprete": "EIZM", "md": 13634.33, "tvdss": -12639.33, "diffMdTvd": 0},
    {"tvd": 13553.84, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_H2S", "interprete": "EIZM", "md": 13553.84, "tvdss": -12558.84, "diffMdTvd": 0},
    {"tvd": 13494.56, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_H1S", "interprete": "EIZM", "md": 13494.56, "tvdss": -12499.56, "diffMdTvd": 0},
    {"tvd": 13389.05, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_G1S", "interprete": "EIZM", "md": 13389.05, "tvdss": -12394.05, "diffMdTvd": 0},
    {"tvd": 13241.13, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_F3S", "interprete": "EIZM", "md": 13241.13, "tvdss": -12246.13, "diffMdTvd": 0},
    {"tvd": 13158.01, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_F2I", "interprete": "EIZM", "md": 13158.01, "tvdss": -12163.01, "diffMdTvd": 0},
    {"tvd": 13020.67, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_F2M", "interprete": "EIZM", "md": 13020.67, "tvdss": -12025.67, "diffMdTvd": 0},
    {"tvd": 14230.27, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_K1M", "interprete": "EIZM", "md": 14230.27, "tvdss": -13235.27, "diffMdTvd": 0},
    {"tvd": 14274.34, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_K1I", "interprete": "EIZM", "md": 14274.34, "tvdss": -13279.34, "diffMdTvd": 0},
    {"tvd": 14303.36, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_L1S", "interprete": "EIZM", "md": 14303.36, "tvdss": -13308.36, "diffMdTvd": 0},
    {"tvd": 14350.86, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_L1I", "interprete": "EIZM", "md": 14350.86, "tvdss": -13355.86, "diffMdTvd": 0},
    {"tvd": 14125.24, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_K1S", "interprete": "EIZM", "md": 14125.24, "tvdss": -13130.24, "diffMdTvd": 0},
    {"tvd": 14914.21, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_P1S", "interprete": "EIZM", "md": 14914.21, "tvdss": -13919.21, "diffMdTvd": 0},
    {"tvd": 15012.71, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_P2S", "interprete": "EIZM", "md": 15012.71, "tvdss": -14017.71, "diffMdTvd": 0},
    {"tvd": 14825.93, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_N1S", "interprete": "EIZM", "md": 14825.93, "tvdss": -13830.93, "diffMdTvd": 0},
    {"tvd": 14873.43, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_O1S", "interprete": "EIZM", "md": 14873.43, "tvdss": -13878.43, "diffMdTvd": 0},
    {"tvd": 14591.72, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_L4S", "interprete": "EIZM", "md": 14591.72, "tvdss": -13596.72, "diffMdTvd": 0},
    {"tvd": 14432.74, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_L2I", "interprete": "EIZM", "md": 14432.74, "tvdss": -13437.74, "diffMdTvd": 0},
    {"tvd": 14394.48, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_L2S", "interprete": "EIZM", "md": 14394.48, "tvdss": -13399.48, "diffMdTvd": 0},
    {"tvd": 14514.64, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_L3S", "interprete": "EIZM", "md": 14514.64, "tvdss": -13519.64, "diffMdTvd": 0},
    {"tvd": 14562.56, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_L3I", "interprete": "EIZM", "md": 14562.56, "tvdss": -13567.56, "diffMdTvd": 0},
    {"tvd": 14787.67, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_M4S", "interprete": "EIZM", "md": 14787.67, "tvdss": -13792.67, "diffMdTvd": 0},
    {"tvd": 14724.05, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_M3S", "interprete": "EIZM", "md": 14724.05, "tvdss": -13729.05, "diffMdTvd": 0},
    {"tvd": 14670.67, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_M2S", "interprete": "EIZM", "md": 14670.67, "tvdss": -13675.67, "diffMdTvd": 0},
    {"tvd": 14623.79, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_M1S", "interprete": "EIZM", "md": 14623.79, "tvdss": -13628.79, "diffMdTvd": 0},
    {"tvd": 12769.06, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_F1S", "interprete": "EIZM", "md": 12769.06, "tvdss": -11774.06, "diffMdTvd": 0},
    {"tvd": 12655.93, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_E3S", "interprete": "EIZM", "md": 12655.93, "tvdss": -11660.93, "diffMdTvd": 0},
    {"tvd": 12905.16, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_F2S", "interprete": "EIZM", "md": 12905.16, "tvdss": -11910.16, "diffMdTvd": 0},
    {"tvd": 15117.67, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_R1I", "interprete": "EIZM", "md": 15117.67, "tvdss": -14122.67, "diffMdTvd": 0},
    {"tvd": 15500.31, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_S3I", "interprete": "EIZM", "md": 15500.31, "tvdss": -14505.31, "diffMdTvd": 0},
    {"tvd": 15309.99, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_R4M", "interprete": "EIZM", "md": 15309.99, "tvdss": -14314.99, "diffMdTvd": 0},
    {"tvd": 15394.85, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_S2S", "interprete": "EIZM", "md": 15394.85, "tvdss": -14399.85, "diffMdTvd": 0},
    {"tvd": 15347.97, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_R4I", "interprete": "EIZM", "md": 15347.97, "tvdss": -14352.97, "diffMdTvd": 0},
    {"tvd": 15169.36, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_R2I", "interprete": "EIZM", "md": 15169.36, "tvdss": -14174.36, "diffMdTvd": 0},
    {"tvd": 11020.93, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_A1S", "interprete": "EIZM", "md": 11020.93, "tvdss": -10025.93, "diffMdTvd": 0},
    {"tvd": 15225.79, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_R3I", "interprete": "EIZM", "md": 15225.79, "tvdss": -14230.79, "diffMdTvd": 0},
    {"tvd": 15255.30, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_R4S", "interprete": "EIZM", "md": 15255.30, "tvdss": -14260.30, "diffMdTvd": 0},
    {"tvd": 15191.07, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_R3S", "interprete": "EIZM", "md": 15191.07, "tvdss": -14196.07, "diffMdTvd": 0},
    {"tvd": 15462.77, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_S3S", "interprete": "EIZM", "md": 15462.77, "tvdss": -14467.77, "diffMdTvd": 0},
    {"tvd": 15597.32, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_S5S", "interprete": "EIZM", "md": 15597.32, "tvdss": -14602.32, "diffMdTvd": 0},
    {"tvd": 15563.46, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_S4S", "interprete": "EIZM", "md": 15563.46, "tvdss": -14568.46, "diffMdTvd": 0},
    {"tvd": 15381.17, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_S1S", "interprete": "EIZM", "md": 15381.17, "tvdss": -14386.17, "diffMdTvd": 0},
    {"tvd": 11716.24, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_A3S", "interprete": "EIZM", "md": 11716.24, "tvdss": -10721.24, "diffMdTvd": 0},
    {"tvd": 12044.36, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_B1S", "interprete": "EIZM", "md": 12044.36, "tvdss": -11049.36, "diffMdTvd": 0},
    {"tvd": 11356.86, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_A2S", "interprete": "EIZM", "md": 11356.86, "tvdss": -10361.86, "diffMdTvd": 0},
    {"tvd": 12552.18, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_E2S", "interprete": "EIZM", "md": 12552.18, "tvdss": -11557.18, "diffMdTvd": 0},
    {"tvd": 12248.44, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_C1S", "interprete": "EIZM", "md": 12248.44, "tvdss": -11253.44, "diffMdTvd": 0},
    {"tvd": 12451.28, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_E1S", "interprete": "EIZM", "md": 12451.28, "tvdss": -11456.28, "diffMdTvd": 0},
    {"tvd": 15797.33, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_U1M", "interprete": "EIZM", "md": 15797.33, "tvdss": -14802.33, "diffMdTvd": 0},
    {"tvd": 15766.96, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_U1S", "interprete": "EIZM", "md": 15766.96, "tvdss": -14771.96, "diffMdTvd": 0},
    {"tvd": 12387.00, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_D1S", "interprete": "EIZM", "md": 12387.00, "tvdss": -11392.00, "diffMdTvd": 0},
    {"tvd": 15722.33, "uwi": "00108AGM0005  01", "pozo": "AGM-005", "unidad": "Fs_Ofic_T1S", "interprete": "EIZM", "md": 15722.33, "tvdss": -14727.33, "diffMdTvd": 0},
    # AGM-007
    {"tvd": 13497.17, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_I1S", "interprete": "EIZM", "md": 13499.47, "tvdss": -12678.17, "diffMdTvd": 2.30},
    {"tvd": 13105.25, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_G1S", "interprete": "EIZM", "md": 13106.92, "tvdss": -12286.25, "diffMdTvd": 1.67},
    {"tvd": 14818.82, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_R2S", "interprete": "EIZM", "md": 14825.83, "tvdss": -13999.82, "diffMdTvd": 7.01},
    {"tvd": 14201.88, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_L3S", "interprete": "EIZM", "md": 14206.57, "tvdss": -13382.88, "diffMdTvd": 4.69},
    {"tvd": 13664.30, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_J1S", "interprete": "EIZM", "md": 13667.07, "tvdss": -12845.30, "diffMdTvd": 2.77},
    {"tvd": 14004.79, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_L1S", "interprete": "EIZM", "md": 14008.79, "tvdss": -13185.79, "diffMdTvd": 4.00},
    {"tvd": 13351.90, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_H3S", "interprete": "EIZM", "md": 13353.89, "tvdss": -12532.90, "diffMdTvd": 1.99},
    {"tvd": 13206.53, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_H1S", "interprete": "EIZM", "md": 13208.31, "tvdss": -12387.53, "diffMdTvd": 1.78},
    {"tvd": 12952.01, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_F3S", "interprete": "EIZM", "md": 12953.54, "tvdss": -12133.01, "diffMdTvd": 1.53},
    {"tvd": 12858.48, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_F2I", "interprete": "EIZM", "md": 12859.95, "tvdss": -12039.48, "diffMdTvd": 1.47},
    {"tvd": 12533.67, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_F1S", "interprete": "EIZM", "md": 12535.00, "tvdss": -11714.67, "diffMdTvd": 1.33},
    {"tvd": 12754.14, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_F2M", "interprete": "EIZM", "md": 12755.56, "tvdss": -11935.14, "diffMdTvd": 1.42},
    {"tvd": 12457.33, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_E3S", "interprete": "EIZM", "md": 12458.64, "tvdss": -11638.33, "diffMdTvd": 1.31},
    {"tvd": 14043.06, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_L1I", "interprete": "EIZM", "md": 14047.20, "tvdss": -13224.06, "diffMdTvd": 4.14},
    {"tvd": 15274.16, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_S5S", "interprete": "EIZM", "md": 15283.24, "tvdss": -14455.16, "diffMdTvd": 9.08},
    {"tvd": 14761.43, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_R1S", "interprete": "EIZM", "md": 14768.22, "tvdss": -13942.43, "diffMdTvd": 6.79},
    {"tvd": 14595.65, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_P1S", "interprete": "EIZM", "md": 14601.78, "tvdss": -13776.65, "diffMdTvd": 6.13},
    {"tvd": 14473.42, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_M4S", "interprete": "EIZM", "md": 14479.07, "tvdss": -13654.42, "diffMdTvd": 5.65},
    {"tvd": 14373.97, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_M2S", "interprete": "EIZM", "md": 14379.25, "tvdss": -13554.97, "diffMdTvd": 5.28},
    {"tvd": 15070.11, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_S1S", "interprete": "EIZM", "md": 15078.21, "tvdss": -14251.11, "diffMdTvd": 8.10},
    {"tvd": 14977.02, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_R4M", "interprete": "EIZM", "md": 14984.69, "tvdss": -14158.02, "diffMdTvd": 7.67},
    {"tvd": 13935.59, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_K1M", "interprete": "EIZM", "md": 13939.33, "tvdss": -13116.59, "diffMdTvd": 3.74},
    {"tvd": 14306.67, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_M1S", "interprete": "EIZM", "md": 14311.72, "tvdss": -13487.67, "diffMdTvd": 5.05},
    {"tvd": 14123.63, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_L2I", "interprete": "EIZM", "md": 14128.05, "tvdss": -13304.63, "diffMdTvd": 4.42},
    {"tvd": 14255.69, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_L3I", "interprete": "EIZM", "md": 14260.56, "tvdss": -13436.69, "diffMdTvd": 4.87},
    {"tvd": 10867.50, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_A1S", "interprete": "EIZM", "md": 10868.66, "tvdss": -10048.50, "diffMdTvd": 1.16},
    {"tvd": 11761.25, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_B1S", "interprete": "EIZM", "md": 11762.54, "tvdss": -10942.25, "diffMdTvd": 1.29},
    {"tvd": 11975.05, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_C1S", "interprete": "EIZM", "md": 11976.34, "tvdss": -11156.05, "diffMdTvd": 1.29},
    {"tvd": 12680.06, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_F2S", "interprete": "EIZM", "md": 12681.44, "tvdss": -11861.06, "diffMdTvd": 1.38},
    {"tvd": 12247.35, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_E1S", "interprete": "EIZM", "md": 12248.65, "tvdss": -11428.35, "diffMdTvd": 1.30},
    {"tvd": 13282.21, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_H2S", "interprete": "EIZM", "md": 13284.08, "tvdss": -12463.21, "diffMdTvd": 1.87},
    {"tvd": 14076.63, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_L2S", "interprete": "EIZM", "md": 14080.89, "tvdss": -13257.63, "diffMdTvd": 4.26},
    {"tvd": 14514.95, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_N1S", "interprete": "EIZM", "md": 14520.76, "tvdss": -13695.95, "diffMdTvd": 5.81},
    {"tvd": 13813.87, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_K1S", "interprete": "EIZM", "md": 13817.16, "tvdss": -12994.87, "diffMdTvd": 3.29},
    {"tvd": 12355.26, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_E2S", "interprete": "EIZM", "md": 12356.56, "tvdss": -11536.26, "diffMdTvd": 1.30},
    {"tvd": 15021.20, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_R4I", "interprete": "EIZM", "md": 15029.07, "tvdss": -14202.20, "diffMdTvd": 7.87},
    {"tvd": 14554.03, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_O1S", "interprete": "EIZM", "md": 14559.99, "tvdss": -13735.03, "diffMdTvd": 5.96},
    {"tvd": 14694.12, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_P2S", "interprete": "EIZM", "md": 14700.65, "tvdss": -13875.12, "diffMdTvd": 6.53},
    {"tvd": 14431.25, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_M3S", "interprete": "EIZM", "md": 14436.74, "tvdss": -13612.25, "diffMdTvd": 5.49},
    {"tvd": 14285.78, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_L4S", "interprete": "EIZM", "md": 14290.76, "tvdss": -13466.78, "diffMdTvd": 4.98},
    {"tvd": 14864.05, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_R2I", "interprete": "EIZM", "md": 14871.23, "tvdss": -14045.05, "diffMdTvd": 7.18},
    {"tvd": 14886.33, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_R3S", "interprete": "EIZM", "md": 14893.60, "tvdss": -14067.33, "diffMdTvd": 7.27},
    {"tvd": 14930.80, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_R4S", "interprete": "EIZM", "md": 14938.26, "tvdss": -14111.80, "diffMdTvd": 7.46},
    {"tvd": 14906.21, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_R3I", "interprete": "EIZM", "md": 14913.57, "tvdss": -14087.21, "diffMdTvd": 7.36},
    {"tvd": 14785.29, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_R1I", "interprete": "EIZM", "md": 14792.17, "tvdss": -13966.29, "diffMdTvd": 6.88},
    {"tvd": 15126.25, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_S3S", "interprete": "EIZM", "md": 15134.63, "tvdss": -14307.25, "diffMdTvd": 8.38},
    {"tvd": 15173.12, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_S3I", "interprete": "EIZM", "md": 15181.73, "tvdss": -14354.12, "diffMdTvd": 8.61},
    {"tvd": 15246.73, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_S4S", "interprete": "EIZM", "md": 15255.68, "tvdss": -14427.73, "diffMdTvd": 8.95},
    {"tvd": 15097.08, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_S2S", "interprete": "EIZM", "md": 15105.32, "tvdss": -14278.08, "diffMdTvd": 8.24},
    {"tvd": 13963.58, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_K1I", "interprete": "EIZM", "md": 13967.42, "tvdss": -13144.58, "diffMdTvd": 3.84},
    {"tvd": 11206.39, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_A2S", "interprete": "EIZM", "md": 11207.61, "tvdss": -10387.39, "diffMdTvd": 1.22},
    {"tvd": 11512.38, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_A3S", "interprete": "EIZM", "md": 11513.64, "tvdss": -10693.38, "diffMdTvd": 1.26},
    {"tvd": 15434.45, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_U1S", "interprete": "EIZM", "md": 15444.28, "tvdss": -14615.45, "diffMdTvd": 9.83},
    {"tvd": 15458.73, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_U1M", "interprete": "EIZM", "md": 15468.68, "tvdss": -14639.73, "diffMdTvd": 9.95},
    {"tvd": 12222.00, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_D1S", "interprete": "EIZM", "md": 12224.60, "tvdss": -11374.00, "diffMdTvd": 2.60},
    {"tvd": 15369.17, "uwi": "00108AGM0007  01", "pozo": "AGM-007", "unidad": "Fs_Ofic_T1S", "interprete": "EIZM", "md": 15378.68, "tvdss": -14550.17, "diffMdTvd": 9.51},
    # AGM-008
    {"tvd": 15082.62, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_S1S", "interprete": "EIZM", "md": 15083.65, "tvdss": -14200.62, "diffMdTvd": 1.03},
    {"tvd": 13460.73, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_I1S", "interprete": "EIZM", "md": 13461.72, "tvdss": -12578.73, "diffMdTvd": 0.99},
    {"tvd": 12465.04, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_F1S", "interprete": "EIZM", "md": 12466.01, "tvdss": -11583.04, "diffMdTvd": 0.97},
    {"tvd": 12350.88, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_E3S", "interprete": "EIZM", "md": 12351.85, "tvdss": -11468.88, "diffMdTvd": 0.97},
    {"tvd": 13174.05, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_H1S", "interprete": "EIZM", "md": 13175.03, "tvdss": -12292.05, "diffMdTvd": 0.98},
    {"tvd": 14154.17, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_L3S", "interprete": "EIZM", "md": 14155.18, "tvdss": -13272.17, "diffMdTvd": 1.01},
    {"tvd": 13981.01, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_L1S", "interprete": "EIZM", "md": 13982.01, "tvdss": -13099.01, "diffMdTvd": 1.00},
    {"tvd": 12708.49, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_F2M", "interprete": "EIZM", "md": 12709.46, "tvdss": -11826.49, "diffMdTvd": 0.97},
    {"tvd": 12925.37, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_F3S", "interprete": "EIZM", "md": 12926.35, "tvdss": -12043.37, "diffMdTvd": 0.98},
    {"tvd": 12846.38, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_F2I", "interprete": "EIZM", "md": 12847.36, "tvdss": -11964.38, "diffMdTvd": 0.98},
    {"tvd": 13323.13, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_H3S", "interprete": "EIZM", "md": 13324.12, "tvdss": -12441.13, "diffMdTvd": 0.99},
    {"tvd": 13083.98, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_G1S", "interprete": "EIZM", "md": 13084.96, "tvdss": -12201.98, "diffMdTvd": 0.98},
    {"tvd": 13661.47, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_J1S", "interprete": "EIZM", "md": 13662.47, "tvdss": -12779.47, "diffMdTvd": 1.00},
    {"tvd": 14027.79, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_L1I", "interprete": "EIZM", "md": 14028.79, "tvdss": -13145.79, "diffMdTvd": 1.00},
    {"tvd": 14352.76, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_M2S", "interprete": "EIZM", "md": 14353.77, "tvdss": -13470.76, "diffMdTvd": 1.01},
    {"tvd": 14779.53, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_R1S", "interprete": "EIZM", "md": 14780.55, "tvdss": -13897.53, "diffMdTvd": 1.02},
    {"tvd": 11260.89, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_A3S", "interprete": "EIZM", "md": 11261.83, "tvdss": -10378.89, "diffMdTvd": 0.94},
    {"tvd": 10902.39, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_A2S", "interprete": "EIZM", "md": 10903.32, "tvdss": -10020.39, "diffMdTvd": 0.93},
    {"tvd": 11668.20, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_B1S", "interprete": "EIZM", "md": 11669.15, "tvdss": -10786.20, "diffMdTvd": 0.95},
    {"tvd": 11901.51, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_C1S", "interprete": "EIZM", "md": 11902.47, "tvdss": -11019.51, "diffMdTvd": 0.96},
    {"tvd": 14632.13, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_P1S", "interprete": "EIZM", "md": 14633.15, "tvdss": -13750.13, "diffMdTvd": 1.02},
    {"tvd": 14470.12, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_M4S", "interprete": "EIZM", "md": 14471.13, "tvdss": -13588.12, "diffMdTvd": 1.01},
    {"tvd": 13893.51, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_K1M", "interprete": "EIZM", "md": 13894.51, "tvdss": -13011.51, "diffMdTvd": 1.00},
    {"tvd": 15299.02, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_S5S", "interprete": "EIZM", "md": 15300.05, "tvdss": -14417.02, "diffMdTvd": 1.03},
    {"tvd": 14984.21, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_R4M", "interprete": "EIZM", "md": 14985.23, "tvdss": -14102.21, "diffMdTvd": 1.02},
    {"tvd": 14865.44, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_R2I", "interprete": "EIZM", "md": 14866.46, "tvdss": -13983.44, "diffMdTvd": 1.02},
    {"tvd": 12276.01, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_E2S", "interprete": "EIZM", "md": 12276.97, "tvdss": -11394.01, "diffMdTvd": 0.96},
    {"tvd": 13799.91, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_K1S", "interprete": "EIZM", "md": 13800.91, "tvdss": -12917.91, "diffMdTvd": 1.00},
    {"tvd": 14092.35, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_L2I", "interprete": "EIZM", "md": 14093.35, "tvdss": -13210.35, "diffMdTvd": 1.00},
    {"tvd": 14890.29, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_R3S", "interprete": "EIZM", "md": 14891.31, "tvdss": -14008.29, "diffMdTvd": 1.02},
    {"tvd": 13258.66, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_H2S", "interprete": "EIZM", "md": 13259.65, "tvdss": -12376.66, "diffMdTvd": 0.99},
    {"tvd": 14210.05, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_L3I", "interprete": "EIZM", "md": 14211.06, "tvdss": -13328.05, "diffMdTvd": 1.01},
    {"tvd": 10323.73, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_A1S", "interprete": "EIZM", "md": 10324.65, "tvdss": -9441.73, "diffMdTvd": 0.92},
    {"tvd": 12138.42, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_E1S", "interprete": "EIZM", "md": 12139.38, "tvdss": -11256.42, "diffMdTvd": 0.96},
    {"tvd": 12640.62, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_F2S", "interprete": "EIZM", "md": 12641.59, "tvdss": -11758.62, "diffMdTvd": 0.97},
    {"tvd": 14304.84, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_M1S", "interprete": "EIZM", "md": 14305.85, "tvdss": -13422.84, "diffMdTvd": 1.01},
    {"tvd": 14249.63, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_L4S", "interprete": "EIZM", "md": 14250.64, "tvdss": -13367.63, "diffMdTvd": 1.01},
    {"tvd": 14051.73, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_L2S", "interprete": "EIZM", "md": 14052.73, "tvdss": -13169.73, "diffMdTvd": 1.00},
    {"tvd": 14815.12, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_R1I", "interprete": "EIZM", "md": 14816.14, "tvdss": -13933.12, "diffMdTvd": 1.02},
    {"tvd": 14708.69, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_P2S", "interprete": "EIZM", "md": 14709.71, "tvdss": -13826.69, "diffMdTvd": 1.02},
    {"tvd": 14560.42, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_O1S", "interprete": "EIZM", "md": 14561.43, "tvdss": -13678.42, "diffMdTvd": 1.01},
    {"tvd": 14403.80, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_M3S", "interprete": "EIZM", "md": 14404.81, "tvdss": -13521.80, "diffMdTvd": 1.01},
    {"tvd": 14506.92, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_N1S", "interprete": "EIZM", "md": 14507.93, "tvdss": -13624.92, "diffMdTvd": 1.01},
    {"tvd": 14843.07, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_R2S", "interprete": "EIZM", "md": 14844.09, "tvdss": -13961.07, "diffMdTvd": 1.02},
    {"tvd": 14921.92, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_R3I", "interprete": "EIZM", "md": 14922.94, "tvdss": -14039.92, "diffMdTvd": 1.02},
    {"tvd": 14950.56, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_R4S", "interprete": "EIZM", "md": 14951.58, "tvdss": -14068.56, "diffMdTvd": 1.02},
    {"tvd": 15109.67, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_S2S", "interprete": "EIZM", "md": 15110.70, "tvdss": -14227.67, "diffMdTvd": 1.03},
    {"tvd": 15265.61, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_S4S", "interprete": "EIZM", "md": 15266.64, "tvdss": -14383.61, "diffMdTvd": 1.03},
    {"tvd": 15049.76, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_R4I", "interprete": "EIZM", "md": 15050.79, "tvdss": -14167.76, "diffMdTvd": 1.03},
    {"tvd": 15198.78, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_S3I", "interprete": "EIZM", "md": 15199.81, "tvdss": -14316.78, "diffMdTvd": 1.03},
    {"tvd": 15151.84, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_S3S", "interprete": "EIZM", "md": 15152.87, "tvdss": -14269.84, "diffMdTvd": 1.03},
    {"tvd": 13946.64, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_K1I", "interprete": "EIZM", "md": 13947.64, "tvdss": -13064.64, "diffMdTvd": 1.00},
    {"tvd": 15460.67, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_U1S", "interprete": "EIZM", "md": 15461.71, "tvdss": -14578.67, "diffMdTvd": 1.04},
    {"tvd": 15579.42, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_U1I", "interprete": "EIZM", "md": 15580.46, "tvdss": -14697.42, "diffMdTvd": 1.04},
    {"tvd": 15638.79, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Mer_U2S", "interprete": "EIZM", "md": 15639.83, "tvdss": -14756.79, "diffMdTvd": 1.04},
    {"tvd": 15527.34, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Ofic_U1M", "interprete": "EIZM", "md": 15528.37, "tvdss": -14645.34, "diffMdTvd": 1.03},
    {"tvd": 15649.21, "uwi": "00108AGM0008  01", "pozo": "AGM-008", "unidad": "Fs_Mer_U3S", "interprete": "EIZM", "md": 15650.25, "tvdss": -14767.21, "diffMdTvd": 1.04}
]


class StratigraphicApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Visor de Topes Estratigráficos / Muestras")
        self.geometry("1200x800")
        
        # DataFrame de Pandas local para manipulación eficiente
        self.df_raw = pd.DataFrame(RAW_DATA)
        self.df_filtered = self.df_raw.copy()
        
        # Configurar Estilos TTK
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("KPI.TFrame", background="#1e293b", relief="flat")
        self.style.configure("KPI.TLabel", background="#1e293b", foreground="#f8fafc", font=("Segoe UI", 10))
        self.style.configure("KPIVal.TLabel", background="#1e293b", foreground="#38bdf8", font=("Segoe UI", 16, "bold"))
        
        self._build_ui()
        self._apply_filters()

    def _build_ui(self):
        # Header / Barra Superior
        header_frame = ttk.Frame(self, padding="10")
        header_frame.pack(side=tk.TOP, fill=tk.X)

        title_label = ttk.Label(
            header_frame, 
            text="Panel de Control Estratigráfico", 
            font=("Segoe UI", 16, "bold")
        )
        title_label.pack(side=tk.LEFT, padx=5)

        btn_export = ttk.Button(header_frame, text="📥 Exportar CSV", command=self._export_csv)
        btn_export.pack(side=tk.RIGHT, padx=5)

        # Panel de Filtros y Búsqueda
        filter_frame = ttk.LabelFrame(self, text=" Filtros de Búsqueda ", padding="10")
        filter_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        # Buscador por texto
        ttk.Label(filter_frame, text="Buscar:").grid(row=0, column=0, sticky=tk.W, padx=5)
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", lambda *args: self._apply_filters())
        search_entry = ttk.Entry(filter_frame, textvariable=self.search_var, width=25)
        search_entry.grid(row=0, column=1, padx=5, sticky=tk.W)

        # Filtro por Muestra / Pozo
        ttk.Label(filter_frame, text="Muestra / Pozo:").grid(row=0, column=2, sticky=tk.W, padx=5)
        self.pozo_combo = ttk.Combobox(filter_frame, state="readonly", width=15)
        pozos = ["Todos"] + sorted(self.df_raw["pozo"].unique().tolist())
        self.pozo_combo["values"] = pozos
        self.pozo_combo.current(0)
        self.pozo_combo.bind("<<ComboboxSelected>>", lambda e: self._apply_filters())
        self.pozo_combo.grid(row=0, column=3, padx=5, sticky=tk.W)

        # Filtro por Unidad
        ttk.Label(filter_frame, text="Unidad:").grid(row=0, column=4, sticky=tk.W, padx=5)
        self.unidad_combo = ttk.Combobox(filter_frame, state="readonly", width=15)
        unidades = ["Todas"] + sorted(self.df_raw["unidad"].unique().tolist())
        self.unidad_combo["values"] = unidades
        self.unidad_combo.current(0)
        self.unidad_combo.bind("<<ComboboxSelected>>", lambda e: self._apply_filters())
        self.unidad_combo.grid(row=0, column=5, padx=5, sticky=tk.W)

        btn_reset = ttk.Button(filter_frame, text="🔄 Limpiar Filtros", command=self._reset_filters)
        btn_reset.grid(row=0, column=6, padx=15, sticky=tk.W)

        # Panel de Tarjetas KPI
        kpi_container = ttk.Frame(self, padding="10")
        kpi_container.pack(side=tk.TOP, fill=tk.X)

        self.kpi_records = self._create_kpi_card(kpi_container, "Total Registros", "0")
        self.kpi_pozos = self._create_kpi_card(kpi_container, "Muestras / Pozos", "0")
        self.kpi_unidades = self._create_kpi_card(kpi_container, "Unidades Únicas", "0")
        self.kpi_avg_tvd = self._create_kpi_card(kpi_container, "TVD Promedio (ft)", "0.0")

        # Pestañas Principales (Tabla / Gráficos)
        notebook = ttk.Notebook(self)
        notebook.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Pestaña 1: Tabla de Datos
        tab_table = ttk.Frame(notebook)
        notebook.add(tab_table, text="📊 Tabla de Datos")
        self._build_table_view(tab_table)

        # Pestaña 2: Perfil Strat
        tab_chart = ttk.Frame(notebook)
        notebook.add(tab_chart, text="📈 Perfil Strat / Profundidad")
        self._build_chart_view(tab_chart)

    def _create_kpi_card(self, parent, title, initial_val):
        frame = ttk.Frame(parent, style="KPI.TFrame", padding="10")
        frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5)
        
        lbl_title = ttk.Label(frame, text=title, style="KPI.TLabel")
        lbl_title.pack(anchor=tk.W)
        
        lbl_val = ttk.Label(frame, text=initial_val, style="KPIVal.TLabel")
        lbl_val.pack(anchor=tk.W, pady=(5, 0))
        
        return lbl_val

    def _build_table_view(self, parent):
        columns = ("pozo", "unidad", "tvd", "md", "tvdss", "uwi", "interprete", "diffMdTvd")
        
        tree_scroll_y = ttk.Scrollbar(parent, orient=tk.VERTICAL)
        tree_scroll_x = ttk.Scrollbar(parent, orient=tk.HORIZONTAL)

        self.tree = ttk.Treeview(
            parent,
            columns=columns,
            show="headings",
            yscrollcommand=tree_scroll_y.set,
            xscrollcommand=tree_scroll_x.set
        )

        tree_scroll_y.config(command=self.tree.yview)
        tree_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        tree_scroll_x.config(command=self.tree.xview)
        tree_scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

        headers = {
            "pozo": "Muestra / Pozo",
            "unidad": "Unidad Estratigráfica",
            "tvd": "TVD (ft)",
            "md": "MD (ft)",
            "tvdss": "TVDSS (ft)",
            "uwi": "UWI",
            "interprete": "Intérprete",
            "diffMdTvd": "Δ MD-TVD"
        }

        for col, heading_text in headers.items():
            self.tree.heading(col, text=heading_text, command=lambda c=col: self._sort_column(c, False))
            self.tree.column(col, anchor=tk.CENTER, width=120)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def _build_chart_view(self, parent):
        self.fig, self.ax = plt.subplots(figsize=(8, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=parent)
        
        toolbar = NavigationToolbar2Tk(self.canvas, parent)
        toolbar.update()
        
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def _apply_filters(self):
        # Filtrado local mediante Pandas en lugar de llamadas complejas
        df = self.df_raw.copy()

        search_txt = self.search_var.get().strip().lower()
        selected_pozo = self.pozo_combo.get()
        selected_unidad = self.unidad_combo.get()

        if selected_pozo != "Todos":
            df = df[df["pozo"] == selected_pozo]

        if selected_unidad != "Todas":
            df = df[df["unidad"] == selected_unidad]

        if search_txt:
            mask = (
                df["pozo"].str.lower().str.contains(search_txt) |
                df["unidad"].str.lower().str.contains(search_txt) |
                df["uwi"].str.lower().str.contains(search_txt) |
                df["interprete"].str.lower().str.contains(search_txt)
            )
            df = df[mask]

        self.df_filtered = df
        self._update_kpis()
        self._update_table()
        self._update_chart()

    def _reset_filters(self):
        self.search_var.set("")
        self.pozo_combo.current(0)
        self.unidad_combo.current(0)
        self._apply_filters()

    def _update_kpis(self):
        total_records = len(self.df_filtered)
        unique_pozos = self.df_filtered["pozo"].nunique() if total_records > 0 else 0
        unique_unidades = self.df_filtered["unidad"].nunique() if total_records > 0 else 0
        avg_tvd = self.df_filtered["tvd"].mean() if total_records > 0 else 0.0

        self.kpi_records.config(text=str(total_records))
        self.kpi_pozos.config(text=str(unique_pozos))
        self.kpi_unidades.config(text=str(unique_unidades))
        self.kpi_avg_tvd.config(text=f"{avg_tvd:,.2f}")

    def _update_table(self):
        # Limpiar registros existentes
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insertar registros filtrados
        for _, row in self.df_filtered.iterrows():
            self.tree.insert("", tk.END, values=(
                row["pozo"],
                row["unidad"],
                f"{row['tvd']:,.2f}",
                f"{row['md']:,.2f}",
                f"{row['tvdss']:,.2f}",
                row["uwi"],
                row["interprete"],
                f"{row['diffMdTvd']:,.2f}"
            ))

    def _update_chart(self):
        self.ax.clear()

        if not self.df_filtered.empty:
            # Graficar TVD vs Muestra/Pozo usando un marcador nativo para evitar problemas de renderizado
            pozos = self.df_filtered["pozo"].unique()
            
            for pozo in pozos:
                sub_df = self.df_filtered[self.df_filtered["pozo"] == pozo].sort_values("tvd")
                self.ax.plot(
                    [pozo] * len(sub_df), 
                    sub_df["tvd"], 
                    marker="o", 
                    linestyle="-", 
                    alpha=0.7, 
                    label=pozo
                )

            self.ax.set_ylabel("Profundidad TVD (ft)")
            self.ax.set_xlabel("Muestra / Pozo")
            self.ax.set_title("Perfil de Profundidad Vert. Verdadera (TVD) por Muestra")
            self.ax.invert_yaxis()  # La profundidad aumenta hacia abajo
            self.ax.grid(True, linestyle="--", alpha=0.5)
            self.ax.legend(loc="upper right")
        else:
            self.ax.text(0.5, 0.5, "Sin datos disponibles", horizontalalignment='center', verticalalignment='center')

        self.fig.tight_layout()
        self.canvas.draw()

    def _sort_column(self, col, reverse):
        # Ordenar DataFrame por columna
        self.df_filtered = self.df_filtered.sort_values(by=col, ascending=not reverse)
        self._update_table()
        self.tree.heading(col, command=lambda: self._sort_column(col, not reverse))

    def _export_csv(self):
        if self.df_filtered.empty:
            messagebox.showwarning("Advertencia", "No hay datos para exportar.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")],
            title="Guardar datos como CSV"
        )
        if file_path:
            self.df_filtered.to_csv(file_path, index=False)
            messagebox.showinfo("Éxito", f"Archivo guardado exitosamente en:\n{file_path}")


if __name__ == "__main__":
    app = StratigraphicApp()
    app.mainloop()
