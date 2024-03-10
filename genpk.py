
def gen_pk_nvar4(last_pk):
    fp = last_pk[0]
    last_pk = last_pk.strip(fp)
    last_pk = last_pk.lstrip('0')
    last_pk = int(last_pk)
    last_pk += 1 
    last_pk = str(last_pk)
    last_pk = last_pk.rjust(3,'0')
    last_pk = fp+last_pk
    return last_pk

def gen_pk_nvar6(last_pk):
    fp = last_pk[0]
    last_pk = last_pk.strip(fp)
    last_pk = last_pk.lstrip('0')
    last_pk = int(last_pk)
    last_pk += 1 
    last_pk = str(last_pk)
    last_pk = last_pk.rjust(5,'0')
    last_pk = fp+last_pk
    return last_pk
    
 
