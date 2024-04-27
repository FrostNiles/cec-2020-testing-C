/*
  CEC20 Test Function Suite for Single Objective Bound Constrained Numerical Optimization 
*/

#include <WINDOWS.H>    
#include <stdio.h>
#include <math.h>
#include <malloc.h>


void cec20_test_func(double *, double *,int,int,int);

double *OShift,*M,*y,*z,*x_bound;
int ini_flag=0,n_flag,func_flag,*SS;


int main(int argc, char **argv)
{
	int i,j,k,n,m,func_num;
	double *f,*x;
	FILE *fpt, *rst;
	char FileName[50];
	if (argc > 1)
	{
		func_num = atoi(argv[1]);
		n = atoi(argv[2]);
	}
	else
	{
		func_num = 1;
		n=10;
	}
	
	m=2;
	x=(double *)malloc(m*n*sizeof(double));
	f=(double *)malloc(sizeof(double)  *  m);
	for (i = func_num; i < func_num + 1; i++)
	{
		sprintf(FileName, "test_data/shift_data_%d.txt", func_num);
		fpt = fopen(FileName,"r");
		if (fpt==NULL)
		{
			printf("\n Error: Cannot open input file for reading \n");
			printf("main");
		}
		
		if (x==NULL)
			printf("\nError: there is insufficient memory available!\n");

		for(k=0;k<n;k++)
		{
				fscanf(fpt,"%Lf",&x[k]);
				/*printf("%Lf\n",x[k]);*/
		}

		fclose(fpt);

			for (j = 0; j < n; j++)
			{
				x[1*n+j]=0.0;
				/*printf("%Lf\n",x[1*n+j]);*/
			}
		
		
		for (k = 0; k < 1; k++)
		{
			cec20_test_func(x, f, n,m,func_num);
			for (j = 0; j < 1; j++)
			{
				printf(" f%d(x[%d]) = %.10f,",func_num,j+1,f[j]);

				sprintf(FileName, "test_data/current_result_%d.txt", func_num);
				rst = fopen(FileName,"w+");
				if (rst==NULL)
				{
					printf("\n Error: Cannot open input file for reading \n");
				}
				fprintf(rst, " f%d(x[%d]) = %.10f,", func_num, j + 1, f[j]);
				fclose(rst);
			}
			printf("\n");
		}
	
	}
	free(x);
	free(f);
	free(y);
	free(z);
	free(M);
	free(OShift);
	free(x_bound);
	return 0;
}


