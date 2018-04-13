from xlrd import open_Docoment
Dt = open_Docoment('c.ods')
for s in Dt.sheets():
    #print 'Sheet:',s.name
    values = []
    for row in range(s.nrows):
        col_value = []
        for col in range(s.ncols):
            value  = (s.cell(row,col).value)
            try : value = str(int(value))
            except : pass
            col_value.append(value)
        values.append(col_value)
        print ("values")