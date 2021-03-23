/*
Code by Neil
March 23, 2021
DSP Lab, Spring 2021
IIT Hyderabad
*/

# include <stdio.h>
# include <string.h>
# include <stdlib.h>
# include <complex.h>
# include <math.h>

 
const double PI = 3.141592653589793238460;
typedef float complex cplx;


void _fft(cplx buf[], cplx out[], int n, int step) //FFT Algorithm
{
	if (step < n) {
		_fft(out, buf, n, step * 2);
		_fft(out + step, buf + step, n, step * 2);
 
		for (int i = 0; i < n; i += 2 * step) {
			cplx t = cexp(-I * PI * i / n) * out[i + step];
			buf[i / 2]     = out[i] + t;
			buf[(i + n)/2] = out[i] - t;
		}
	}
}
 
void fft(cplx buf[], int n) //FFT Caller function
{
	cplx *out = (cplx *) malloc(n*sizeof(cplx));
	for (int i = 0; i < n; i++) out[i] = buf[i];
	_fft(buf, out, n, 1);

    free(out);
}

void _ifft(cplx buf[], cplx out[], int n, int step) //Inverse-FFT Algorithm
{
	if (step < n) {
		_ifft(out, buf, n, step * 2);
		_ifft(out + step, buf + step, n, step * 2);
 
		for (int i = 0; i < n; i += 2 * step) {
			cplx t = cexp(I * PI * i / n) * out[i + step];
			buf[i / 2]     = out[i] + t;
			buf[(i + n)/2] = out[i] - t;
            
		}
	}
}
 
void ifft(cplx buf[], int n) //IFFT Caller Function
{
    cplx *out = (cplx *) malloc(n*sizeof(cplx));
	for (int i = 0; i < n; i++) out[i] = buf[i];
 
	_ifft(buf, out, n, 1);
	for (int i = 0 ; i < n ; i++){buf[i] /= n;}

    free(out);
}
 
void multiply(cplx* Y,cplx* X,cplx* Hz,int n)
{
	for(int i=0;i<n;i++)
	{
		Y[i] = Hz[i]*X[i];
	}
}
 


int main(){
    
    int n =pow(2,21);
    double *x = (double *) malloc(n*sizeof(double)); //storing input

    FILE *fx, *fX,*fH,*fY,*fy;

    //Allocating Storage for corresponding arrays
    cplx *X = (cplx *) malloc(n*sizeof(cplx));
    cplx *Hz = (cplx *) malloc(n * sizeof(cplx));
    cplx *Y = (cplx *) malloc(n * sizeof(cplx));
    cplx *y = (cplx *) malloc(n * sizeof(cplx));


    fx = fopen("../files/x.dat", "r");
    for(int i=0;i<n;i++) 
    {
        double data;
        fscanf(fx, "%lf", &data);
        x[i] = data;
    }
    fclose(fx);

    
    for(int i = 0; i < n; i++)
    {
        X[i] = x[i];
    }

    fft(X, n);    //X = fft(x)

    fX  = fopen("../files/X.dat","w");
    for(int i = 0; i < n; i++)
    {
        fprintf(fX, "%lf+j%lf\n", creal(X[i]), cimag(X[i]));
	}  
    fclose(fX);

    fH = fopen("../files/Hz.dat","r");
    for(int i=0;i<n;i++) 
    {
        double re,im;
        fscanf(fH, "%lf" "%lf", &re,&im);
        Hz[i] = CMPLX(re,im);
    }
    fclose(fH);

    multiply(Y,X,Hz,n); //Y(k) = H(k) * X(k)
    
    fY = fopen("../files/Y.dat","w");
    for(int i = 0; i < n; i++)
    {
        fprintf(fY, "%lf+j%lf\n", creal(Y[i]), cimag(Y[i]));
    }
    fclose(fY);
    
    
    for(int i=0;i<n;i++)
    {
		y[i] = Y[i];
	}

    ifft(y,n);   // y = ifft(Y)
    
    fy = fopen("../files/y.dat","w");
    for(int i=0;i<n;i++)
    {
		fprintf(fy, "%lf %lf\n", creal(y[i]), cimag(y[i]));
	}
	fclose(fy);

    return 0;
}