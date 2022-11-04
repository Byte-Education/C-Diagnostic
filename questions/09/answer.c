#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

struct contact
{
  char firstName[50];
  char lastName[50];
  char email[20];
};

struct book
{
  int size;
  int index;
  struct contact *contacts;
};

struct book *initializeBook(int size)
{
  /*
  Your code goes here
  */
}

struct contact *addContact(struct book *book, char *firstName, char *lastName, char *email)
{
  /*
  Your code goes here
  */
}

void printBook(struct book *book)
{
  /*
  Your code goes here
  */
}

void freeBook(struct book *book)
{
  /*
  Your code goes here
  */
}

int main(void)
{
  struct book *book = initializeBook(2);
  addContact(book, "john", "doe", "jdoe@gmail.com");
  addContact(book, "jane", "doe", "jdoe2@gmail.com");
  printBook(book);
  freeBook(book);
  return 0;
}