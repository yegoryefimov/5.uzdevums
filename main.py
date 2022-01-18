teksts = input ("Ievadi tekstu: ")
def replace0 (teksts):
  if teksts.count("o")>0 or teksts.count("O")>0:
    teksts = teksts.replace("o","%")
    teksts = teksts.replace("O","%")
    print(teksts)
  else: 
    teksts = "nav burtu O vai o"
    print(teksts)
  return teksts
replace0 (teksts)