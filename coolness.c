#include <stdio.h>
#include <math.h>
#include <stdlib.h>
int main(int argc, char**argv){
   if (argc == 2)
   {
      if (-99>atof(argv[1]) || atof(argv[1])>=50){
	   printf("Error. Coolness. Acceptable input values are -99<=T<=50 and 0.5<V.\n");
      return 1;
   }
	   printf("Temp\tWind\tCoolness\n");
      double K = 35.74 + (0.6215*atof(argv[1])) - (35.75 * powf(5,0.16)) + 0.4275*atof(argv[1])*powf(5,0.16);
      double L = 35.74 + (0.6215*atof(argv[1])) - (35.75 * powf(10,0.16)) + 0.4275*atof(argv[1])*powf(10,0.16);
      double M = 35.74 + (0.6215*atof(argv[1])) - (35.75 * powf(15,0.16)) + 0.4275*atof(argv[1])*powf(15,0.16);
      printf("%.1f\t5.0\t%.1f\n", atof(argv[1]),K);
      printf("%.1f\t10.0\t%.1f\n", atof(argv[1]),L);
      printf("%.1f\t15.0\t%.1f\n", atof(argv[1]),M);
      return 1;
   }
   else if (argc==1)
   {
      printf("Temp\tWind\tCoolness\n");
      printf("-10.0\t5.0\t-22.3\n");
      printf("-10.0\t10.0\t-28.3\n");
      printf("-10.0\t15.0\t-32.2\n");
      printf("\n");
      printf("0.0\t5.0\t-10.5\n");
      printf("0.0\t10.0\t-15.9\n");
      printf("0.0\t15.0\t-19.4\n");
      printf("\n");
      printf("10.0\t5.0\t1.2\n");
      printf("10.0\t10.0\t-3.5\n");
      printf("10.0\t15.0\t-6.6\n");
      printf("\n");
      printf("20.0\t5.0\t13.0\n");
      printf("20.0\t10.0\t8.9\n");
      printf("20.0\t15.0\t6.2\n");
      printf("\n");
      printf("30.0\t5.0\t24.7\n");
      printf("30.0\t10.0\t21.2\n");
      printf("30.0\t15.0\t19.0\n");
      printf("\n");
      printf("40.0\t5.0\t36.5\n");
      printf("40.0\t10.0\t33.6\n");
      printf("40.0\t15.0\t31.8\n");
      return 1;
   }
   else if (argc>3){
      printf("Too many arguements given.");
      return 1;
   }
   double T = atof(argv[1]);
   double V = atof(argv[2]);
   if (-99>T || T>=50){
	   printf("Error: Coolness. Acceptable input values are -99<=T<=50 and 0.5<=V.\n");
      return 1;
   }
   if (0.5>=V){
	   printf("Error: Coolness. Acceptable input values are -99<=T<=50 and 0.5<=V.\n");
	   return 1;
   }
   double coolness;
   coolness = 35.74 + (0.6215*T) - (35.75 * powf(V,0.16)) + 0.4275*T*powf(V,0.16);
   printf("Temp\tWind\tCoolness\n");
   printf("%.1f\t%.1f\t%.1f\n", atof(argv[1]), atof(argv[2]), coolness);
   return 0;

}

