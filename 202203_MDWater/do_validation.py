import validation

#validation.make_fp_pwscf()
jdata, mdata = validation.read_para_machine()
validation.run_fp(jdata, mdata)

