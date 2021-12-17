# QAP 5
# December 17, 2021
# ONE STOP INSURANCE
# Terence Martin-Ferraro

import datetime

f = open("OSICDef.dat", "r")

POL_NUM = int(f.readline())
BAS_PREM = float(f.readline())
ADD_CAR_DIS_RATE = float(f.readline())
EXT_LIA = float(f.readline())
GLASS_COV = float(f.readline())
OPT_LOANER = float(f.readline())
HST_RATE = float(f.readline())
PROCESS_FEE = float(f.readline())

# INPUTS

while True:
    print()
    while True:
        CustFirst = input("Enter the customers first name: ").title()
        if CustFirst == "":
            print("Invalid input - Cannot be blank - Try again.")
        else:
            break

    while True:
        CustLast = input("Enter the customers last name: ").title()
        if CustLast == "":
            print("Invalid input - Cannot be blank - Try again.")
        else:
            break

    while True:
        StAdd = input("Enter the customers street address: ").title()
        if StAdd == "":
            print("Invalid input - Cannot be blank - Try again.")
        else:
            break

    while True:
        City = input("Enter the customers city: ").title()
        if City == "":
            print("Invalid input - Cannot be blank - Try again.")
        else:
            break

    while True:
        Prov = input("Enter the customers province: ").upper()
        if Prov == "":
            print("Invalid input - Cannot be blank - Try again.")
        else:
            break

    while True:
        Postal = input("Enter the customers postal code: ").upper()
        if Postal == "":
            print("Invalid input - Cannot be blank - Try again.")
        elif len(Postal) != 6:
            print("Invalid postal code - Must be 6 characters - Try again.")
        else:
            break

    while True:
        Phone = input("Enter the customers phone number: ")
        if Phone == "":
            print("Invalid input - Cannot be blank - Try again.")
        elif len(Phone) != 10:
            print("Invalid phone number - Must be 10 digits - Try again.")
        else:
            break

    while True:
        NumCars = int(input("Enter number of cars being insured: "))
        if NumCars == "":
            print("Invalid input - Cannot be blank - Try again.")
        else:
            break

    while True:
        ExtraLiability = input("Extra liability coverage up to $1,000,000? (Y or N): ")
        if ExtraLiability.upper() == "Y":
            ExtraLiability = EXT_LIA * NumCars
            break
        elif ExtraLiability.upper() == "N":
            ExtraLiability = 0
            break
        elif ExtraLiability.upper() != "Y" or "N":
            print("Invalid input.. Must be Y or N.. Try again")

    while True:
        GlassCoverage = input("Glass coverage protection? (Y or N): ")
        if GlassCoverage.upper() == "Y":
            GlassCoverage = GLASS_COV * NumCars
            break
        elif GlassCoverage.upper() == "N":
            GlassCoverage = 0
            break
        elif GlassCoverage.upper() != "Y" or "N":
            print("Invalid input.. Must be Y or N.. Try again")

    while True:
        OptionalLoaner = input("Loaner car coverage? (Y or N): ")
        if OptionalLoaner.upper() == "Y":
            OptionalLoaner = OPT_LOANER * NumCars
            break
        elif OptionalLoaner.upper() == "N":
            OptionalLoaner = 0
            break
        elif OptionalLoaner.upper() != "Y" or "N":
            print("Invalid input.. Must be Y or N.. Try again")

    while True:
        PayMethod = input("Does the customer want to pay in full or have monthly payments? (F or M): ")
        if PayMethod.upper() == "F":
            PayMethod = "Full"
            break
        elif PayMethod.upper() == "M":
            PayMethod = "Monthly"
            break
        elif PayMethod.upper() != "F" or "M":
            print("Invalid input.. Must be F or M.. Try again")

    f.close()

    # CALCULATIONS

    CustFull = CustFirst + " " + CustLast
    Today = datetime.datetime.now()

    if NumCars == 1:
        PremCost = BAS_PREM
    elif NumCars > 1:
        PremCost = BAS_PREM + (BAS_PREM * ADD_CAR_DIS_RATE) * (NumCars - 1)

    TotExtCost = (ExtraLiability + GlassCoverage + OptionalLoaner) * NumCars
    TotInsPrem = PremCost + TotExtCost
    HST = TotInsPrem * HST_RATE
    TotCost = TotInsPrem + HST
    MonthlyFee = (TotCost + PROCESS_FEE) / 12

    # Formatting

    PremCostStr = "${:,.2f}".format(PremCost)
    PremCostPad = "{:<10}".format(PremCostStr)

    TotExtCostStr = "${:,.2f}".format(TotExtCost)
    TotExtCostPad = "{:<10}".format(TotExtCostStr)

    TotInsPremStr = "${:,.2f}".format(TotInsPrem)
    TotInsPremPad = "{:<10}".format(TotInsPremStr)

    HSTStr = "${:,.2f}".format(HST)
    HSTPad = "{:<10}".format(HSTStr)

    MonthlyFeeStr = "${:,.2f}".format(MonthlyFee)
    MonthlyFeePad = "{:<10}".format(MonthlyFeeStr)

    ExtraLiabilityStr = "${:,.2f}".format(ExtraLiability)
    ExtraLiabilityPad = "{:<10}".format(ExtraLiabilityStr)

    GlassCoverageStr = "${:,.2f}".format(GlassCoverage)
    GlassCoveragePad = "{:<10}".format(GlassCoverageStr)

    OptionalLoanerStr = "${:,.2f}".format(OptionalLoaner)
    OptionalLoanerPad = "{:<10}".format(OptionalLoanerStr)

    f = open('Policies.dat', 'a')
    f.write("{}, ".format(str(POL_NUM)))    # 0
    f.write("{}, ".format(str(CustFirst)))  # 1
    f.write("{}, ".format(str(CustLast)))   # 2
    f.write("{}, ".format(str(StAdd)))      # 3
    f.write("{}, ".format(str(City)))       # 4
    f.write("{}, ".format(str(Prov)))       # 5
    f.write("{}, ".format(str(Postal)))     # 6
    f.write("{}, ".format(str(Phone)))      # 7
    f.write("{}, ".format(int(NumCars)))    # 8
    f.write("{}, ".format(str(PremCost)))   # 9
    f.write("{}, ".format(str(EXT_LIA)))   # 10
    f.write("{}, ".format(str(GLASS_COV))) # 11
    f.write("{}, ".format(str(OPT_LOANER)))# 12
    f.write("{}, ".format(str(TotExtCost)))# 13
    f.write("{}, ".format(str(HST)))       # 14
    f.write("{}, ".format(str(MonthlyFee)))# 15
    f.write("{}\n".format(str(TotInsPrem)))# 16

    POL_NUM += 1

    f.close()

    f = open('OSICDef.dat', 'w')
    f.write("{}\n ".format(str(POL_NUM)))
    f.write("{}\n ".format(float(BAS_PREM)))
    f.write("{}\n ".format(float(ADD_CAR_DIS_RATE)))
    f.write("{}\n ".format(float(EXT_LIA)))
    f.write("{}\n ".format(float(GLASS_COV)))
    f.write("{}\n ".format(float(OPT_LOANER)))
    f.write("{}\n ".format(float(HST_RATE)))
    f.write("{}\n ".format(float(PROCESS_FEE)))
    f.close()

    # Receipt
    print()
    print()
    print(" " * 25, "ONE STOP INSURANCE")
    print(" " * 25, " CUSTOMER RECIEPT")
    print()
    print("=" * 70)
    print()
    print("  Customer Name: {}".format(CustFull))
    print("  Phone number:  {}".format(Phone))
    print("  Address:       {}".format(StAdd))
    print("                 {}      {}, {}".format(City, Prov, Postal))
    print()
    print("-" * 70)
    print(" " * 25, "Extra coverage")
    print()
    print("  Extra Liability Insurance:             {}".format(ExtraLiabilityPad))
    print("  Glass Coverage Protection:             {}".format(GlassCoveragePad))
    print("  Loaner Vehicle Coverage:               {}".format(OptionalLoanerPad))
    print("                                         --------")
    print("  Total Extra Coverage Charges:          {}".format(TotExtCostPad))
    print("  Payment Method:                        {}".format(PayMethod))
    print("  Number of cars insured:      {}         {}".format(NumCars, PremCostPad))
    print()
    print("-" * 62)

    while True:
        Continue = input("Would you like to add another policy? (Y/N): ").upper()
        if Continue == "Y":
            break
        elif Continue == "N":
            print("Thank you for using the One Stop Insurance program.")
            break
    if Continue == "N":
        break

print()
print("ONE STOP INSURANCE COMPANY")
print("Policy listing as of {}".format(datetime.datetime.strftime(Today, "%d-%b-%Y")))
print()
print("POLICY CUSTOMER                  INSURANCE       EXTRA          TOTAL")
print("NUMBER NAME                       PREMIUM        COSTS         PREMIUM")
print("=" * 75)

PremCostAcc = 0
TotExtCostAcc = 0
HSTAcc = 0
MonthlyFeeAcc = 0
TotInsPremAcc = 0

CustCtr = 0
f = open("Policies.dat", "r")
for PolLine in f:
    PolData = PolLine.split(",")
    # print(PolData)
    POL_NUM = PolData[0]
    CustFirst = PolData[1].strip()
    CustLast = PolData[2].strip()
    NumberCarsIns = PolData[8].strip()
    PremCost = float(PolData[9].strip())
    TotExtCost = float(PolData[13].strip())
    HST = float(PolData[14].strip())
    TotInsPrem = float(PolData[16].strip())

    PremCostAcc += PremCost
    TotExtCostAcc += TotExtCost
    HSTAcc += HST
    MonthlyFeeAcc += MonthlyFee
    TotInsPremAcc += TotInsPrem
    CustCtr += 1
    print("{}   {:<8} {:<16} ${:<10,.2f}    ${:<8,.2f}    ${:<5,.2f}".format(POL_NUM, CustFirst, CustLast, PremCost, TotExtCost, TotInsPrem))

print("=" * 75)
print("Total Policies: {}               ${:,.2f}     ${:,.2f}   ${:,.2f}".format(CustCtr, PremCostAcc, TotExtCostAcc, TotInsPremAcc))
print()
print("-" * 75)
f.close()

# Monthly Payment Form

print()
print("ONE STOP INSURANCE COMPANY")
print("Policy listing as of {}".format(datetime.datetime.strftime(Today, "%d-%b-%Y")))
print()
print("POLICY CUSTOMER                  TOTAL       TOTAL       MONTHLY")
print("NUMBER  NAME                    PREMIUM       HST        PAYMENT")
print("=" * 65)

CustCtr = 0
PremCostAcc = 0
TotExtCostAcc = 0
HSTAcc = 0
MonthlyFeeAcc = 0
TotInsPremAcc = 0

f = open("Policies.dat", "r")

for PolLine in f:
    PolData = PolLine.split(",")
    # print(PolData)
    POL_NUM = PolData[0]
    CustFirst = PolData[1].strip()
    CustLast = PolData[2].strip()
    NumberCarsIns = PolData[8].strip()
    PremCost = float(PolData[9].strip())
    HST = float(PolData[14].strip())
    MonthlyFee = float(PolData[15].strip())

    PremCostAcc += PremCost
    TotExtCostAcc += TotExtCost
    HSTAcc += HST
    MonthlyFeeAcc += MonthlyFee
    TotInsPremAcc += TotInsPrem
    CustCtr += 1

    print("{}   {:<8} {:<16}${:<10,.2f} ${:<6,.2f}      ${:<5,.2f}".format(POL_NUM, CustFirst, CustLast, PremCost, HST, MonthlyFee))

print("=" * 65)
print("Total Policies: {}           ${:,.2f}   ${:,.2f}    ${:,.2f} ".format(CustCtr, PremCostAcc, HSTAcc, MonthlyFeeAcc))

f.close()


