#include <cstdio>
#include <cstdlib>
#include <cmath>

const int QUEEN = 8;
const int INITVAL = -1;
int a[QUEEN];

void init() {
  for (int *p = a; p < a+QUEEN; ++p) {
    *p = INITVAL;
  }
}

bool valid(int row, int col) {
  for (int i = 0; i < row; ++i) {
    if (col == a[i] || abs(row - i) == abs(col - a[i])) {
      return false;
    }
  }
  return true;
}

void myprint() {
  for (int i = 0; i < QUEEN; ++i) {
    printf("%d ", a[i]);
  }
  printf("\n");

  for (int i = 0; i < QUEEN; ++i) {
    for (int j = 0; j < QUEEN; ++j) {
      if (a[i] == j) {
	printf("#");
      } else {
	printf(".");
      }
    }
    printf("\n");
  }
}

int queen() {
  int n = 0;			// count of answer
  int i = 0, j = 0;
  while (i < QUEEN) {
    while (j < QUEEN) {
      if (valid(i, j)) {
	a[i] = j;
	j = 0;
	break;			// go to next line
      } else {
	++j;			// try next col
      }
    } // while j

    if (a[i] == -1) {		// fail for line i
      if (i == 0) {		// fail for line 0
	break;			// fail, and should finish
      } else {			// 
	--i;
	j = a[i] + 1;		// restart from j+1
	a[i] = INITVAL;		// return to last line
	continue;		// dont increase i
      }
    } // if a[i] == -1

    if (i == QUEEN-1) {		// reach last line
      printf("answer %d\n", ++n);	// get one answer
      myprint();		// print answer

      j = a[i] + 1;		// check if next col is also answer
      a[i] = INITVAL;
      continue;			// similar to previous line
    }
    ++i;
  }   // while i
}

int main(int, char**) {
  init();
  queen();
  return 0;
}
