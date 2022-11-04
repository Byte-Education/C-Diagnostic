#include <stdio.h>

int len(char *s)
{
  /*
  Your code goes here.
  */
  return 0;
}

int main(void)
{
  char str[] = "Hello World";
  int length = len(str);
  printf("string: %s\nlength: %d\n", str, length);
  printf("string: %s\nlength: %d\n", "You're beautiful", len("You're beautiful"));
  return 0;
}