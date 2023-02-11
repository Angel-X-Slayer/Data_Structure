def min_num_appe_for_palin(stri):  ## append at the end
    l=len(stri)
    if l<2:
        return(print(0))
    stri_rev=stri[::-1]
    for i in range(l):
        if stri[i:]==stri_rev[:l-i]:
            return(print(i))
    return(print(i))

stri="abecbea"
min_num_appe_for_palin(stri)
    
        
    