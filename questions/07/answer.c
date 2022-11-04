#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>

bool equals(char *str1, char *str2){
  /*
  Your code goes here.
  */
  return false;
}

int main(void){
  printf("%d\n", equals("hello", "hello")); // Should print 1
  printf("%d\n", equals("hello", "Hello")); // should print 1
  printf("%d\n", equals("hello", "hellp")); // should print 0
  printf("%d\n", equals("hello", "Hellp")); // should print 0
  return 0;
}