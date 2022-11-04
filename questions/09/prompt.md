# Question 9

Create an address book using structs and pointers.

The address book should contain a size, an index, and a pointer to a struct contact. This struct contact should contain a first name, a last name, and an email. The structs are provided below. Implement the following functions.

    struct book * initializeBook(int size);
    struct contact * addContact(struct book * book, char firstName[], char lastName[], char email[]);
    void printContacts(struct book * book);
    void freeBook(struct book * book);

    struct contact {
      char firstName[50];
      char lastName[50];
      char email[20];
    };

    struct book {
      int size;
      int index;
      struct contact * contacts;
    };
