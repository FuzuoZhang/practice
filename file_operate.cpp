#include <stdio.h>
#include <stdlib.h>

void fun_1(){
  FILE * pFile;
  int buffer[] = {1, 2, 3, 4};
  if((pFile = fopen ("test.txt", "wb"))==NULL)
  {
      printf("cant open the file");
      exit(0);
  }
  //可以写多个连续的数据(这里一次写4个)
  fwrite (buffer , sizeof(int), 4, pFile);
  fclose (pFile);
  return;
}

void fun_2(){
    FILE * fp;
    int data[5] = {1,2,3,4,5};
    if((fp = fopen("test.txt","wb"))==NULL){
      printf("cant open the file");
      exit(0);
    }
    int i;
    for(i=0;i<5;i++){
      fprintf(fp,"%d ",data[i]);
    }
    fclose(fp);
    return ;
  }

int main ()
{
  fun_1();
  fun_2();
  return 0;
}
