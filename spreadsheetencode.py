def spread_sheet_encoder(column):

    if len(column) == 0:
        return 0

    result = (ord(column[0])-64)*(26**(len(column)-1))

    return result + spread_sheet_encoder(column[1:])


print(spread_sheet_encoder('A'))
print(spread_sheet_encoder('AA'))
print(spread_sheet_encoder('ZZ'))
