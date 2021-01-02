def insert_pp_in_lana(pp):
    f=open('lana/cat.txt','w')
    f.writelines(pp)
    f.close()

pp=['H','E','L','L','O',' ','W','O','R','L','D']
insert_pp_in_lana(pp)
