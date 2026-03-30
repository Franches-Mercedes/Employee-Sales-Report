# This opens the SalesData.dat file to read the contents inside the file
inFile = open("SalesData.dat", 'r')

# These are counters to track full-time and part-time employee's
iFull_time = 0
iPart_time = 0
# Tracks the total amount of commissions from every employee
iTotal_Commission = 0

# UI Display to categorize the data in the .dat file
print('               Employee Sales Report\n')
print(f"{'Name':<13} {'Status':<9} {'Rate':<8} {'Sales': <8} {'Commission Earned':<5}")

# From the SalesData.dat file this loop will read the employee's
# Name, Status, and Sales
while True:
    # Grabs data from the .dat file to organize it in a report
    sales = inFile.readline().strip()
    # if the current sequence in the file is empty then the while loop will break
    if sales == '':
        break
    status = inFile.readline().strip()
    sName = inFile.readline().strip()

    # reassigning the variables above that grab specific data like status' and sales to organize it
    iSales = int(sales)
    iStatus = int(status)

    # adds a +1 to the Full-time or part-time counters to track how many people are fulfilling each role
    if iStatus == 1:
        iFull_time += 1
    else:
        iPart_time += 1

    # Based off of the sales number it will give the employee a specific percentage
    if iSales < 2000:
        dRate = 0.01
    elif iSales < 4000:
        dRate = 0.03
    elif iSales < 6000:
        dRate = 0.04
    else:
        dRate = 0.05

    # Multiplies the current sequence of the employee's sales and rate, then rounds up that integer
    iCommission = round(dRate * iSales)
    # Counter for the total amount of commissions out of the 10 employee's
    iTotal_Commission += iCommission

    # organizes the data according to the titles above it for readability
    print(f"{sName:<13} {iStatus:<9} {int(dRate * 100)}%       {iSales:<8} {int(iCommission)}")

# .close() closes the file that was opened at the beginning of the document
inFile.close()

# # Displays the full-time, part-time, and total commissions accumulators
print("\n________________________________________")
print(f"Full-time count: {iFull_time}")
print(f"Part time count: {iPart_time}")
print(f"\nTotal commissions paid out...${iTotal_Commission}")
