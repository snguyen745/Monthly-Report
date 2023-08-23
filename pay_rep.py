NUM_COLS = 60  # number of columns in pay rep sheet

# constants for the index of each column in the pay rep sheet
DATE = 0
PATIENT = 1
BILLING_CODES = 3
    # G = 4, 14, s0, s1
    # C = 4/14/s0/s1 + SPH, PREM, STY, or CUS (remove G)
    # I = OPTOS
    # D = DIL
    # T = Topo
    # F = SPH, PREM, STY, or CUS w/o 4, 14, s0, or s1
    # O = 201-203 or 211-213
    # L = LAK
    # DK = DEK
    # M = HMask
    # S = HAS
    # D3 = De3
    # OA = OATP
    # N = 4 or s0
    # P = 14 or s1
    # T = leave blank

FEES_TOTAL = 5  # U & C = Fees Total - 70 (only if Paid Ins > 0)
PAID_INS = 12  # reimbursement
CASH = 18
CHECK = 19
DEBIT_CARD = 33
VISA = 34  # used for credit card along with next three
MASTER_CARD = 35
AMEX = 36
DISCOVER = 37

# columns in pay rep sheet currently not in use
# SERVICE_CODES = 2
# FEES_PAT = 6  # ignore
# FEES_PAT_TOTAL = 7  # ignore
# FEES_INS = 8  # ignore
# FEES_INS_TOTAL = 9  # ignore
# PAID = 10  # ignore
# PAID_PAT = 11  # ignore
# ADJUSTMENTS = 13
# INVOICE = 14
# BALANCE = 15
# PREV_BALANCE = 16
# PAY_TYPE = 17
# CREDIT_CARD = 20
# INSURANCE_PAID = 21
# DOCTOR = 22
# SALES_PERSON = 23
# DESCRIPTIONS = 24  # ignore
# FRAME_INFO = 25
# LOC_ID = 26
# INS_CC = 27
# EFT = 28
# PURCHASE = 29
# DIAG_CODES = 30  # ignore
# ACCT_ID = 31  # ignore
# DOB = 32
# NONE = 38
# OFFICE_VISIT = 39
# EYE_EXAM = 40
# TESTING = 41
# POST_OP = 42
# DIAG_PROC = 43
# CL_EXAM = 44
# OTHER = 45
# DISCOUNTS = 46
# PRODUCT = 47
# REFRACTIVE_OV = 48
# QNT_NONE = 49
# QNT_OFFICE_VISIT = 50
# QNT_EYE_EXAM = 51
# QNT_TESTING = 52
# QNT_POST_OP = 53
# QNT_DIAG_PROC = 54
# QNT_CL_EXAM = 55
# QNT_OTHER = 56
# QNT_DISCOUNTS = 57
# QNT_PRODUCT = 58
# QNT_REFRACTIVE_OV = 59