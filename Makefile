CC=gcc

default: 01 02 03 04 05 06 07 08 09

01:
	$(CC) -o questions/01/01 questions/01/answer.c

02:
	$(CC) -o questions/02/02 questions/02/answer.c

03:
	$(CC) -o questions/03/03 questions/03/answer.c

04:
	$(CC) -o questions/04/04 questions/04/answer.c

05:
	$(CC) -o questions/05/05 questions/05/answer.c

06:
	$(CC) -o questions/06/06 questions/06/answer.c

07:
	$(CC) -o questions/07/07 questions/07/answer.c

08:
	$(CC) -o questions/08/08 questions/08/answer.c

09:
	$(CC) -o questions/09/09 questions/09/answer.c

clean:
	rm -f questions/01/01
	rm -f questions/02/02
	rm -f questions/03/03
	rm -f questions/04/04
	rm -f questions/05/05
	rm -f questions/06/06
	rm -f questions/07/07
	rm -f questions/08/08
	rm -f questions/09/09

test: 01 02 03 04 05 06 07 08 09
	./questions/01/01
	./questions/02/02
	./questions/03/03
	./questions/04/04
	./questions/05/05
	./questions/06/06
	./questions/07/07
	./questions/08/08
	./questions/09/09