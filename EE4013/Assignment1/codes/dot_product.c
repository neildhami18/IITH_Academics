#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

//Linked List Data Structure
struct node {
   int data;
   int key;
   struct node *next;
};

// Storage for the data read from a text file
struct list {
    char *string;
};

typedef struct list LIST;

//display the list
void printList(struct node* head1) {
   struct node *ptr = head1;
   printf("\n[ ");
	
   //start from the beginning
   while(ptr != NULL) {
      printf("(%d,%d) ",ptr->key,ptr->data);
      ptr = ptr->next;
   }
	
   printf(" ]");
}

//insert link at the first location
struct node* insertFirst(struct node* head1, int key, int data) {
   //create a link
   struct node *link = (struct node*) malloc(sizeof(struct node));
	
   link->key = key;
   link->data = data;
	
   //point it to old first node
   link->next = head1;
	
   //point first to new first node
   head1 = link;
   return head1;
}

int dot(struct node* List1, struct node* List2)
{
    int product = 0;
    struct node *current_a = List1;
    struct node *current_b = List2;

    while(current_a != 0 && current_b!=0)
    {
        if(current_a->key == current_b->key)
        {
            product = product + current_a->data * current_b->data;
            current_a=current_a->next;
            current_b=current_b->next;
        }
        else if(current_a->key < current_b->key)
        {
            current_a=current_a->next;
        }
        else
        {
            current_b=current_b->next;
        }
    }
    return product;
}



void main() {
   
   struct node *List1, *List2 = NULL;
   
   //SECTION: Manual Inputs (Uncomment below segment for entering manual inputs)
   /*
   List1 = insertFirst(List1,1,10);
   List1 = insertFirst(List1,2,20);
   List1 = insertFirst(List1,3,30);
   
   printf("List 1 : "); 
   printList(List1);

   List2 = insertFirst(List2,1,50);
   List2 = insertFirst(List2,2,30);
   List2 = insertFirst(List2,3,40);
   
   printf("\nList 2: "); 
   printList(List2);
   */
    
   //SECTION: Input from text file
   FILE *f1, *f2; //two vector containing files
   char line[128];
   //LIST *current1, *head1, *current2, *head2;

   //head1 = head2 = current1 = current2 = NULL;
   f1 = fopen("vector1.txt", "r");
   int i1=1;
   while(fgets(line, sizeof(line), f1)){
       LIST *node = malloc(sizeof(LIST));
       node->string = strdup(line);
       int data = atoi(node->string);
       //printf("%d", data);
       List1 = insertFirst(List1,i1,data);
       i1++;
   }
   fclose(f1);
   printList(List1);

   f2 = fopen("vector2.txt", "r");
   int i2=1;
   while(fgets(line, sizeof(line), f2)){
       LIST *node = malloc(sizeof(LIST));
       node->string = strdup(line);
       int data = atoi(node->string);
       //printf("%d", data);
       List2 = insertFirst(List2,i2,data);
       i2++;
   }
   fclose(f2);
   printList(List2);

   int product = dot(List1,List2);
   
   printf("\nDot product: %d",product);

}