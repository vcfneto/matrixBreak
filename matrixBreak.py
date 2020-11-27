import numpy as np
from util import *




def ge(mi,list_of_blocks):
    nee = np.sum(mi)
    n1 =0
    mrxnr= 0
    for block in list_of_blocks:
        n1 += np.count_nonzero(block)
        mrxnr += block.size
    nee -=n1
    pee = nee/np.sum(mi)
    #ex = pee
    es = n1/mrxnr
    ge = ((1-pee)+(es))/2

    return ge

def index_to_array(matrix,index):
    return matrix[index[0]:index[1],index[2]:index[3]]

def list_to_alt(matrix,list_index):
    output = []
    [output.append(index_to_array(matrix,ind)) for ind in list_index]
    return output
    
def swap_alt(list_,swap,index):
    c = list_[:index]
    c.extend(swap)
    c.extend(list_[index+1:])
    return c




def matrixBreak(temp_list,matrix,max_ge=0,best_alt=list(),last_ge = 0):
    for p in range(len(temp_list)):
        m_ = temp_list[p]
        rows,cols = m_.shape[0],m_.shape[1]
        for i in range(rows-1):
            for j in range(cols-1):
                temp_list_copy = temp_list.copy()
                alt = [[0,i+1,0,j+1],[i+1,rows,j+1,cols]]
                aa =swap_alt(temp_list_copy,list_to_alt(m_,alt),p)
                #ge_alt = 10
                ge_alt = ge(matrix,aa)
                if ge_alt>max_ge:
                    max_ge,best_alt = ge_alt,aa
                if ge_alt > last_ge:
                    max_ge2,aa2 = matrixBreak(aa,matrix,last_ge = ge_alt)
                    if max_ge2 > max_ge:
                        max_ge,best_alt = max_ge2,aa2

    return max_ge,best_alt  


def oldMatrixBreak(temp_list,matrix,max_ge=0,best_alt=list()):
    for p in range(len(temp_list)):
        m_ = temp_list[p]
        rows,cols = m_.shape[0],m_.shape[1]
        for i in range(rows-1):
            for j in range(cols-1):
                temp_list_copy = temp_list.copy()
                alt = [[0,i+1,0,j+1],[i+1,rows,j+1,cols]]
                aa =swap_alt(temp_list_copy,list_to_alt(m_,alt),p)
                ge_alt = ge(matrix,aa)
                if ge_alt>max_ge:
                   max_ge,best_alt = ge_alt,aa
                max_ge2,aa2 = oldMatrixBreak(aa,matrix,max_ge=max_ge)
                if max_ge2 > max_ge:
                   max_ge,best_alt = max_ge2,aa2

    return max_ge,best_alt  