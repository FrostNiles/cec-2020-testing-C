import subprocess
import multiprocessing
import os
import time

skipped = {}
run_only = {1, 2, 3, 4, 6, 7, 16, 19, 22, 24, 25}

"""
case 1:	
			bent_cigar_func(&x[i*nx],&f[i],nx,OShift,M,1,1);
			f[i]+=100.0;
			break;
		case 2:	
			schwefel_func(&x[i*nx],&f[i],nx,OShift,M,1,1);//F11 in CEC2014
			f[i]+=1100.0;
			break;
		case 3:	
			bi_rastrigin_func(&x[i*nx],&f[i],nx,OShift,M,1,1);//F7 in CEC 2017
			f[i]+=700.0;
			break;
		case 4:	
			hf01(&x[i*nx],&f[i],nx,OShift,M,SS,1,1);//F17 in cec 2014 (hf1 in cec 2014)
           
			f[i]=f[i]+1700.0;
          
//             printf("f[%d]=%f\n",i,1.0);            
			break;
		case 6:
			hf05(&x[i*nx],&f[i],nx,OShift,M,SS,1,1);//F21 in cec 2014 (hf5 in cec 2014)
			f[i]+=2100.0;
			break;
		case 7:	
            grie_rosen_func(&x[i*nx],&f[i],nx,OShift,M,1,1);//f19 in cec2017 
			f[i]+=1900.0;
			break;
		case 16:	
			hf06(&x[i*nx],&f[i],nx,OShift,M,SS,1,1);
			f[i]+=1600.0;
			break;
		case 22:	
			cf02(&x[i*nx],&f[i],nx,OShift,M,1);
			f[i]+=2200.0;
			break;
		case 24:	
			cf04(&x[i*nx],&f[i],nx,OShift,M,1);
			f[i]+=2400.0;
			break;
		case 25:	
			cf05(&x[i*nx],&f[i],nx,OShift,M,1);
			f[i]+=2500.0;
			break;
            
            
            case 19:	
			hf09(&x[i*nx],&f[i],nx,OShift,M,SS,1,1);
			f[i]+=1900.0;
			break;
            this is probably the one not included in the test
"""

# Compile the C++ file
if not os.path.exists('./main'):
    subprocess.run(["g++", "main.cpp", "cec20_test_func.cpp", "-o", "main"], check=True)

def run_test(i):
    for j in [5, 10, 15, 20]:
        for k in range(1, j+1):
            # Set the dimension as a command line argument for the C++ program
            args = [str(i), str(j), str(k)]
            subprocess.run(['python', './run-tests.py'] + args)

if __name__ == '__main__':
    # Create a pool of workers
    with multiprocessing.Pool() as pool:
		# for i in run_only:
        for i in run_only:
            if i in skipped:
                continue
            # Run the test in a separate process
            pool.apply_async(run_test, (i,))

        # Wait for all the tests to finish
        pool.close()
        pool.join()