import sys

def time_on_air(syn_num, preamble_len, sf, bw):
    return ((sym_num + 4.25+preamble_len) * ((2.0**sf)/bw) * 1000)
#if __name__ == '__main__':
    #sym_num = int(sys.argv[1])
    #preamble_len = int(sys.argv[2])
    #sf = int(sys.argv[3])
    #bw = int(sys.argv[4])
time_ms = time_on_air(sym_num, preamble_len, sf, bw)
    
    #((sym_num + 4.25+preamble_len) * ((2.0**sf)/bw) * 1000)
#    sys.stdout.write(str(time_ms))
    #sys.stdout.write(str( (sym_num + 4.25+preamble_len) * ((2.0**sf)/bw) * 1000 )+'\n')
